# Data Guy Story — Editorial Standards Plan

Updated: 1 October 2026.

Status: proposed editorial and verification standard. Follows the [general website plan](website-general-plan.md), [Wiki coverage plan](wiki-structure-and-coverage-plan.md), and the five learning-path plans. This document guides future writing and review; it does not mark existing pages as reviewed or publish new content.

## 1. What each content type is for

| Type | Reader's reason to open it | Owns | Does not own |
| --- | --- | --- | --- |
| Wiki concept or technology article | Understand, apply, or revisit one subject | Canonical explanation, precise terms, small verified example, limitations and references | Week-by-week course sequence or a complete project assignment |
| Learning-path overview | Decide whether and how to start | Audience, entry check, outcome, pace, guided/final projects, availability and AI setup | Repeated textbook explanations |
| Weekly module | Complete one observable step | Task, local setup when needed, mentor entry, fixture, hints, checks and reflection | A second canonical explanation of SQL, Spark or another reusable topic |
| Project brief | Know what to build and how it will be checked | Business question, source/metric contracts, boundaries, fixtures, deliverables and rubric | Finished transformation logic for an independent project |
| Chuyện thực tế | Learn from a documented engineering decision | Sourced facts, constraints, decision, outcome, uncertainty and interpretation | An invented case presented as a real event |
| Blog | Hear the author's experience or viewpoint | Personal voice, observations and clearly labeled opinion | Unattributed general technical claims treated as established fact |

Canonical Wiki articles may be broader than the paths. A course pack selects and embeds reviewed portions of those articles so an AI mentor can work from actual text; the source article remains authoritative. An old Blog post is historical writing and is not silently rewritten to match current practices.

## 2. Voice and terminology

Write primarily in conversational Vietnamese. Preserve the author's approachable voice: begin with a concrete question or situation, show what happens, then name the general concept. Address the reader as “bạn” where natural; “mình” is appropriate in explanations. Avoid exaggerated claims, career guarantees and unexplained tool names.

Use Vietnamese where it is clear and stable, followed by the familiar English name on first use: “kho dữ liệu (data warehouse).” Retain common code and product names exactly (`order_id`, SQL, PostgreSQL, Spark). Within a page, choose one term for the same concept. Explain “grain” as “mỗi dòng đại diện cho điều gì” before relying on it. Explain `NULL`, missing input and valid empty input as different states. Define business date and timezone whenever time-based metrics appear. Use integer đồng or an explicit decimal rule for money. Do not turn one technology stack into a universal definition of Data Engineering.

The voice differs by section. Wiki articles are careful and reusable; modules are direct and task-oriented; stories separate what a source reports from our interpretation; Blog posts may be informal and opinionated. Do not flatten historical Blog language into textbook prose.

A terminology register should be maintained during authoring, with columns: Vietnamese display term, English term, definition, canonical article, permitted shorthand and known ambiguous usages. Start with data/dữ liệu, pipeline, source, record/row, grain, schema, batch, streaming, warehouse, lakehouse, idempotency, freshness, backfill, checkpoint and deployment. Review it when a new page introduces a competing definition; do not block a useful article solely because the register is incomplete.

## 3. Page templates

### Wiki article

1. **Reader question and scope.** State what the article answers, required prior knowledge and what it leaves to another article.
2. **Concrete case.** Show 2–10 small records or one observable system behavior before expanding to abstractions.
3. **Concept and mechanism.** Define terms, show the sequence or relationship, and explain a common failure.
4. **Try it.** Give a runnable command/query or a hand-checkable exercise with expected output and versioned environment where relevant.
5. **Tradeoff and boundary.** State when the approach is useful, what breaks it, and which alternatives matter.
6. **Next reference.** Link to prerequisites, related subjects and a relevant learning path only when the relationship is real.

Technology articles add tested tool version, OS/runtime assumptions, installation or configuration prerequisites, and error/recovery notes. Stable concepts should not depend on an unpinned product release. Front matter should keep title, description, `draft`, `contentType`, `level`, `topics`, prerequisites and related links consistent with existing Hugo conventions. Confirm exact accepted fields in the theme/metadata implementation before bulk migration.

### Weekly module

Open with a stakeholder question and a small input. State the observable checkpoint. The mentor source map lists actual Wiki sections used during the task; direct reading links are available without becoming a separate mandatory course. Provide local setup steps when the tool first appears, including OS selection, expected command output, one likely fault and restart instructions. Then give the learner task, progressive hints, fixture IDs, checks, a changed follow-up case and journal prompt. Show whether the module is available, in pilot or planned. A published module must have all required artifacts and links.

### Project brief

Use one-page decision fields before implementation: report user; two or three questions; source grain/keys; timestamps/timezone/cutoff; metric formulas and denominators; missing/empty/invalid behavior; change/replay policy; expected outputs; acceptance scenarios; out-of-scope ideas. Supply a tiny independently verified fixture, a larger practice fixture and a rubric. Final briefs omit completed domain transformations while retaining enough exact contract detail for fair assessment. AI can help brainstorm optional emphasis, but cannot silently change required reference metrics.

### Story and Blog

Stories begin with the organization/system and the specific engineering problem, cite primary source material as near as practical to factual claims, identify what the original source actually measured, then discuss alternatives and our interpretation. Include publication date and event date when different. If a useful conclusion is inferred, label it as inference. Never reproduce large blocks from a source. Blog posts retain the author/date/context and distinguish personal experience from generalizable advice; refresh outdated technical claims with a note or a new post instead of rewriting history without explanation.

## 4. Examples and technical correctness

An example is publishable only when its inputs, assumptions, commands/code, expected output and failure conditions can be checked. Keep synthetic examples free of real customer data and secrets. Version fixtures and answer files; assign a stable fixture ID so a learner, mentor and reviewer are discussing the same case. For a numerical result, independently calculate a tiny case by hand or with a separate reference implementation. A check generated from the same production logic is insufficient as the only oracle.

For SQL/data examples, state each table's grain and keys before a multi-table join. Test multi-row joins, `NULL`, duplicate keys, zero denominators, missing periods, timezone boundaries and corrected input where relevant. For pipelines, test repeat runs and failure before/after the commit boundary. For streaming, state identity, event time, arrival time, watermark, late policy and sink guarantee. For distributed work, record input size, plan and local machine limits before claiming a performance improvement.

Code blocks declare language and, where necessary, shell, operating system, database engine and version. Commands that modify data use a disposable fixture or a clearly labeled scratch environment. Example output reflects an executed version of the published command. Keep code and answer files in the course starter where appropriate; prose shows enough to understand them without burying an entire lab inside a Wiki article.

## 5. Evidence, attribution and AI use

For changing technical behavior, consult primary documentation at authoring/review time and record the tested version and review date. Link directly to the supporting page. Product APIs, supported versions and install commands must be rechecked before release and on a scheduled maintenance pass. Explain how a source supports a claim; a link alone is not verification.

AI may outline, draft, translate, generate sample data, propose code and help review. The human author owns the final claim and example. Before publishing AI-assisted material: check the referenced Wiki concept, run the code, verify every reported number against the reference fixture, inspect links and read the Vietnamese prose for tone and ambiguity. Do not cite an AI conversation as proof of technical behavior. Keep a short editorial note for material corrections or contested tradeoffs; no need to label every sentence by drafting method.

The learner-facing mentor should cite imported section names, distinguish known facts from hypotheses, ask for local results, and avoid claiming access to a learner's machine unless the specific assistant tool has it. Course packs include actual reviewed content and version IDs. A stale or missing pack section must not be presented as a completed lesson.

## 6. Review and publication gates

| Gate | Required check |
| --- | --- |
| Scope | One reader question, correct content type, no duplicate canonical article |
| Meaning | Terms defined before use, claims bounded, assumptions and exceptions explicit |
| Example | Fixture version and expected output verified independently; commands tested in documented environment |
| Source | Factual external claims supported by primary source; dates/versions recorded where behavior may change |
| Navigation | Prerequisites and related links resolve; no draft-only page is a required published step |
| Experience | Vietnamese readable on mobile; code/tables accessible; alt text or text equivalent for meaningful diagrams |
| AI/course pack | Selected sections and contracts included with revision IDs; import tested when a pack is published |
| Release | Preview with drafts and production build without drafts; review rendered page and route/metadata changes |

Use a light two-pass review: first technical correctness and source/fixture evidence, then prose, learner flow and rendered page. The same reviewer may do both for a small page, but must record what was checked. High-impact corrections to metric contracts or runnable examples require rerunning dependent course acceptance fixtures and regenerating packs. Editorial spelling fixes need a normal page review and pack rebuild only if included text changed.

`draft: false` means the source is configured for publication, not that these checks have passed. Track review state separately in an editorial inventory (path, owner, last technical check, last render check, fixture/version, pack inclusion and next review trigger). Do not present placeholder Wiki articles as available teaching sources.

## 7. Maintenance and delivery sequence

1. Create the terminology register and page/checklist templates using two existing Bắt đầu articles, one Data Engineering article and one old Blog post. Preserve the Blog's historical voice.
2. Verify the introductory path's first fixture, environment recipe, mentor source selections and two-week pilot. Use the results to adjust these standards.
3. Apply the templates only when authoring or materially revising a page; avoid a bulk rewrite that produces cosmetic churn without review evidence.
4. Build an editorial inventory and check required links, draft state and pack manifest during each release. Update or withdraw broken instructions promptly.
5. Review each path pack when source articles, fixtures, metric contracts or supported tool versions change. Keep older pack versions accessible long enough for a learner to finish an active course version.
6. Schedule periodic review of installation commands, tool compatibility and source links; trigger immediate review after an observed failure or material upstream change.

The first deliverable is a small reviewed pilot set, not a claim that the whole Wiki is approved. Existing plans remain proposals until their materials pass the relevant gates.
