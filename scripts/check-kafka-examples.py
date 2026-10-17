"""Check the Kafka 4.0.2 intro with an isolated one-node KRaft broker.
Usage: JAVA_HOME=/path/to/jdk17 python3 scripts/check-kafka-examples.py /path/to/kafka_2.13-4.0.2
Binds loopback ports 19092/19093, uses temporary storage, stops only its own broker.
Not a multi-broker failover or transactional sink test.
"""
from pathlib import Path
import json
import os
import re
import subprocess
import sys
import tempfile
import time

KAFKA = Path(sys.argv[1]).resolve()
ROOT = Path(__file__).resolve().parents[1]
article = (ROOT / 'content/wiki/technologies/kafka/overview.md').read_text()
records = [json.loads(line) for line in re.search(r'```json\n(.*?)```', article, re.S).group(1).splitlines()]

def cli(name, *args, input=None, timeout=35):
    result = subprocess.run([str(KAFKA/'bin'/name), *map(str,args)], cwd=KAFKA,
        input=input, capture_output=True, text=True, timeout=timeout)
    if result.returncode: raise RuntimeError((name, result.stdout, result.stderr[-3000:]))
    return result.stdout

with tempfile.TemporaryDirectory(prefix='dgs-kafka-check-') as tmp:
    tmp = Path(tmp)
    config = tmp/'server.properties'
    source_config = re.search(r'```properties\n(.*?)```', article, re.S).group(1)
    config.write_text(source_config.replace('log.dirs=./cafe-data-v1', 'log.dirs='+str(tmp/'data')))
    cluster_id = cli('kafka-storage.sh','random-uuid').strip().splitlines()[-1]
    cli('kafka-storage.sh','format','--standalone','-t',cluster_id,'-c',config)
    log = (tmp/'broker.log').open('w+')
    broker = None
    def start():
        process = subprocess.Popen([str(KAFKA/'bin/kafka-server-start.sh'),str(config)],cwd=KAFKA,stdout=log,stderr=subprocess.STDOUT)
        deadline=time.monotonic()+60
        while time.monotonic()<deadline:
            log.flush()
            if process.poll() is not None: raise RuntimeError((tmp/'broker.log').read_text()[-5000:])
            if 'Kafka Server started' in (tmp/'broker.log').read_text(): return process
            time.sleep(.5)
        process.terminate();process.wait(timeout=20)
        raise TimeoutError('Broker not ready')
    def stop(process):
        process.terminate()
        try: process.wait(timeout=25)
        except subprocess.TimeoutExpired: process.kill();process.wait()
    endpoint='localhost:19092'
    try:
        broker=start()
        cli('kafka-topics.sh','--bootstrap-server',endpoint,'--create','--topic','cafe-v1','--partitions','1','--replication-factor','1')
        cli('kafka-console-producer.sh','--bootstrap-server',endpoint,'--topic','cafe-v1',input='\n'.join(json.dumps(r) for r in records)+'\n')
        def consume(group):
            output=cli('kafka-console-consumer.sh','--bootstrap-server',endpoint,'--topic','cafe-v1','--group',group,'--from-beginning','--max-messages','2','--timeout-ms','20000')
            return [json.loads(line) for line in output.splitlines() if line.startswith('{')]
        assert consume('cafe-reader-v1')==records
        print('PASS produce/read ordered events',flush=True)
        assert consume('cafe-reader-replay')==records
        print('PASS independent group replay',flush=True)
        stop(broker);broker=None
        log.seek(0);log.truncate();log.flush()
        broker=start()
        assert consume('cafe-reader-after-restart')==records
        print('PASS broker restart retains records',flush=True)
    finally:
        if broker is not None: stop(broker)
        log.close()
