# Streaming Engineering — Learning Path Plan

Updated: 1 October 2026. Status: proposed curriculum following the [general plan](website-general-plan.md) and [Data Engineering thực chiến](data-engineering-thuc-chien-plan.md). This plan specifies teaching and assessment; executable labs and fixtures remain to be built.

## Audience and outcome

For learners who can operate a batch pipeline, state source identities and time rules, and recover a failed run. Spark & Lakehouse is useful preparation but not required. Entry challenge: deduplicate versioned records, distinguish event time from arrival time and explain an idempotent replay; provide short remediation using the relevant Wiki material.

Completion outcome: build and operate a continuous event pipeline with Kafka and Flink on the learner's computer; define event-time windows, late-data policy, state and checkpoint behavior; diagnose duplicates, lag and backpressure; and demonstrate recovery with a trustworthy output contract. Proposed **8 weeks, 8–10 hours each**, including two final-project weeks. Pilot setup load and memory before promising this pace.

## AI-guided local environment

All required data services run locally: a pinned Kafka broker, Flink job manager and task managers, event generator, local checkpoint/savepoint storage, and a small output database or file sink. Author and test one container profile with persistent volumes and a lower-resource sequential profile only if it preserves the required checkpoints. The mentor asks OS, architecture, available RAM/disk and installed container runtime, then guides installation/configuration one step at a time. The learner executes health checks, creates a topic, produces and consumes a sample, submits a tiny Flink job, and verifies checkpoint persistence after restart. Debugging uses exact redacted commands, logs, configs and observed output; the mentor proposes one diagnostic check at a time. Record versions, ports, volumes and restart commands in the setup journal. One deliberate bad broker address or checkpoint path becomes a guided recovery exercise. Setup is part of week 1. The AI companion may be online.

Kafka offset and consumer concepts use the [Kafka documentation](https://kafka.apache.org/documentation/). Flink's [event-time documentation](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/time/) and [checkpoint documentation](https://nightlies.apache.org/flink/flink-docs-stable/docs/ops/state/checkpoints/) inform the labs. Pin compatible release documentation and connectors when authoring; these references do not constitute a tested local bundle.

## Guiding project: Theo dõi đơn giao hàng theo thời gian sự kiện

A fictional delivery service emits order-created, accepted, pickup, location and delivered/cancelled events. An operations view asks how many active orders are waiting, which promised deliveries became late, and how far behind the system is. Supply a deterministic event generator plus replayable event log: small hand-checkable script, larger disorder/lag script, and exact expected answers for fixed cutoffs.

Events carry `event_id`, `order_id`, `event_type`, source version, event timestamp with offset, ingestion timestamp, schema version and payload. Use `Asia/Ho_Chi_Minh` to display business dates; compare timestamps as instants. An event is deduplicated by `event_id` plus version; a repeated order can have many valid events. Order state transitions are explicit: created → accepted → picked up → delivered, with cancellation allowed before delivery. Invalid transitions and conflicting equal versions go to a visible quarantine stream. An order becomes late if its promise time passes before delivered/cancelled; report late-at-cutoff and eventual late delivery separately.

The main view updates counts by region and 15-minute event-time window, plus current active and overdue order state. Define the watermark, permitted lateness and correction behavior in the contract; a late event within the bound updates the result, an event beyond the bound is quarantined for explicit replay or adjustment. Missing events are not invented. Output includes watermark, last input event time, last processed time, broker lag and last successful checkpoint. An output is provisional until its window closes under the chosen policy.

A checkpoint restores Flink state and source position together within the tested connector. The course must not promise end-to-end exactly-once from checkpoints alone: the chosen sink must be idempotent or transactional, and learners demonstrate its behavior with duplicates and injected failure. Keep an append-only audit of input event IDs and a materialized current view with stable keys. If a sink cannot satisfy the required behavior in the pilot, change it before release.

## Weekly journey

| Week | Work | Completion evidence |
| --- | --- | --- |
| 1 — First event | AI-guided install and service checks; produce/consume, inspect keys, partitions and offsets. | Local health checks, setup journal, tiny event trace. |
| 2 — Consumer and state | Build event validation, deduplication and order-state transitions; explain partition-key choice. | Repeat and invalid-transition fixtures pass without losing audit events. |
| 3 — Event time | Implement windows, watermark and bounded lateness; compare arrival time and event time. | Out-of-order fixture matches reference, late policy visible. |
| 4 — Recovery | Enable checkpointing; fail and restart job; verify source position and sink behavior. | Before/after state and result agreement; no extra counted orders. |
| 5 — Operation | Measure lag and backpressure, vary input rate, inspect metrics and choose a response; rehearse savepoint-based change. | A short incident note with measured evidence and safe restart. |
| 6 — Serve and explain | Publish a readable operations view with freshness/provisional status, runbook and schema-change policy. | Clean local restart, changed schema fixture, alert for stalled processing. |
| 7 — Final design/build | Choose domain with AI, define events/state/time, implement first correct slice. | Confirmed brief, tiny answer fixture, state diagram. |
| 8 — Final verification | Inject duplicates, disorder, late events and failure; demonstrate recovery and walkthrough. | Acceptance matrix, reproducible run, unseen event variation. |

Use one question, prediction, local attempt, Wiki explanation and evidence review each week. AI can help with code and diagnosis, but the learner must predict and verify event behavior. Week 5 includes an explicit statement of the hardware limit: several local containers do not demonstrate multi-machine fault tolerance.

## Final projects

All options use synthetic, bounded events, one keyed state machine, one event-time aggregate and a late-event/recovery challenge. Reuse generic setup and metric reporter, not a completed domain job.

| Option | Required output and edge case |
| --- | --- |
| **Workshop check-in** | Unique attendees by 15-minute window and current admission state; duplicate scans and delayed cancellation. |
| **Bike station availability** | Station-level available-bike state and shortage windows; out-of-order dock/undock and missing event quarantine. |
| **Payment authorization** | Approved/declined counts and pending-authorizations state; repeated attempts share an order but retain unique transaction IDs, delayed reversal changes state. |

The mentor helps choose and bound the brief, identify event identity, key, ordering, watermark, state transitions and output contract. Author-verified fixtures remain fixed. Deliver a versioned local job, state diagram, output, tests, checkpoint/restart evidence, lag investigation, runbook and explanation of an AI suggestion verified or corrected. Optional ideas follow only after core acceptance.

Score 0–2 for eight dimensions: event identity, state correctness, event-time correctness, late policy, source/sink recovery, observability, reproducibility, and explanation. Proposed pass **13/16**, with state, time, and recovery each at 2. Verify a previously unseen event sequence. AI scoring is advisory.

## Wiki and release work

Reuse [batch versus streaming](../content/wiki/data-engineering/batch-vs-streaming.md), [stream processing](../content/wiki/data-engineering/stream-processing.md), [Kafka overview](../content/wiki/technologies/kafka/overview.md), [topic/partition](../content/wiki/technologies/kafka/topic-partition.md), [offsets](../content/wiki/technologies/kafka/offset.md), [consumer groups](../content/wiki/technologies/kafka/consumer-group.md), [Flink overview](../content/wiki/technologies/flink/overview.md), [event time](../content/wiki/technologies/flink/event-time.md), [watermarks](../content/wiki/technologies/flink/watermark.md), [state](../content/wiki/technologies/flink/state.md), [checkpoints](../content/wiki/technologies/flink/checkpoint.md) and [backpressure](../content/wiki/technologies/flink/backpressure.md). Existing technology files are scaffolds until reviewed and expanded. Add canonical explanations for event identity, state transition contracts, sink guarantees, late-event repair and schema compatibility. The course pack embeds reviewed text, contracts, hints and answers for small cases.

Release gates: pin and pilot the local stack; verify weeks 1–3 fixtures; exercise failure/restart and sink guarantees for weeks 4–6; pilot each final option within two weeks. Test on declared hardware sizes, including volume persistence and port-conflict recovery. Partial releases must label available milestones.
