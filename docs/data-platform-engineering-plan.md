# Data Platform Engineering — Learning Path Plan

Updated: 1 October 2026. Status: proposed curriculum following the [general plan](website-general-plan.md) and [Data Engineering thực chiến](data-engineering-thuc-chien-plan.md). This defines a learner journey; no lab or publication is implied.

## Audience and outcome

For learners who can build and operate one data pipeline and want to provide repeatable services for other engineers. Streaming and Spark are optional branches, not prerequisites. Entry challenge: reproduce a batch pipeline from a clean checkout, identify its secrets and permissions, and explain one failure/recovery run. Supply a short terminal, Git, container and networking preparation lab for gaps.

Completion outcome: design, build and operate a small **self-service local data platform** for two fictional teams. A team can request a workspace, obtain a database/schema and job template with least-privilege access, run checks and release a pipeline, inspect health, and recover or revoke its resources. The learner explains platform interfaces, ownership, compatibility and operational cost. Proposed **8 weeks at 8–10 hours** including two final-project weeks; pilot setup and teardown time before publishing.

## AI-guided local setup

All required services run on the learner's computer: container runtime, PostgreSQL, a local scheduler/job runner, local Git repository, and a metrics/logs dashboard chosen and pinned during lab authoring. Provisioning uses versioned scripts or a small local CLI; a locally hosted Git server and Kubernetes are optional expansions, not requirements. CI-style checks run locally. The AI mentor asks OS, architecture, memory/disk and installed tools, then guides installation and verification one step at a time. The learner runs health checks, creates an isolated test workspace, verifies permitted and denied database actions, restarts services and reads logs. The mentor diagnoses redacted commands/output and waits for one check before another suggestion. Save versions, ports, persistent volume paths and restart procedures in a setup journal. Setup is a week-1 checkpoint. AI hosting is independent of the local data platform.

Provisioning commands must be safe to retry and have a documented rollback/cleanup path. Use fixture credentials only; never put secrets in Git or the course pack. The course provides tested OS-specific recipes and expected command results. A local setup demonstrates interfaces and failure behavior; it does not claim the availability, isolation or security of a production multi-host platform.

## Guiding project: Nền tảng tự phục vụ cho hai data team

The fictional Sales and Operations teams each maintain one pipeline. Today each engineer hand-copies a Compose file, database credentials, job schedule and dashboard. The platform learner provides a versioned **workspace template and request interface**. Team A's café sales pipeline and Team B's delivery-summary pipeline are supplied as tiny workloads; the platform must support both without per-team code edits to the platform core.

A workspace request declares team ID, project name, dataset contract version, schedule and resource limits. The platform validates it, creates a team-owned namespace/schema and database role, renders job configuration from a pinned template, registers a local schedule, and emits metadata (owner, version, source, output, run link). A local catalog page or generated Markdown index is sufficient. A team can run `init → validate → plan → apply → run → inspect → retire` through documented commands. `plan` shows intended changes before applying. Apply records resource IDs so repeat requests converge on the same state; retirement disables jobs and revokes access, with retained data/export policy stated explicitly.

Access contract: Sales can read/write its own staging and marts, Operations can read/write its own, and a shared read-only report role can read only published marts. A test must show a denied cross-team read and a successful permitted read. A local development admin role is separated from team credentials. Resource quotas are simulated/enforced within available tools and documented honestly; no claim of hard isolation on a single host.

Operational contract: each workspace reports last run, last successful run, freshness, row/check status, job version and owner. Logs and metrics use stable team/project/run labels. Alert rules flag stale output and failed runs to a local console or file sink; no external notification account is required. Runbooks cover bad config, failed release, changed dataset contract, database restart and revocation. Support one backward-compatible template change and one breaking change requiring explicit migration. A failed apply leaves the previous working workspace discoverable and repeatable.

## Weekly journey

| Week | Guided work | Completion evidence |
| --- | --- | --- |
| 1 — Understand the user | AI-guided local setup; interview two supplied team personas, inventory repeated work and define the platform contract. | Healthy stack, setup journal, service brief and user journey. |
| 2 — Reproducible workspace | Build request schema, template and `validate/plan/apply` flow for one team. | Clean workspace created twice with stable state; invalid request rejected. |
| 3 — Access and secrets | Add separate roles, schema permissions, redacted config and credential rotation exercise. | Positive and negative permission tests; rotation without committing a secret. |
| 4 — Delivery workflow | Provide local checks, versioned job template, release and rollback for both team workloads. | Two teams onboard through the same interface; broken release does not replace last good one. |
| 5 — Operation and observation | Add run metadata, logs, freshness and failure dashboard, local alert sink. | Team can identify a stale or failed pipeline and locate its run/owner. |
| 6 — Lifecycle and compatibility | Retire a workspace, migrate a template version, restore from failed apply and write an operations runbook. | No orphan schedule or active credential after retire; compatible migration demonstrated. |
| 7 — Final design/build | Select platform extension with AI, define user and acceptance tests, implement thin slice. | Confirmed brief and first user workflow. |
| 8 — Final verification | Onboard a new supplied team, inject failure, test denied access and demonstrate rollback/retirement. | Acceptance matrix, clean setup and unseen request variation. |

Every milestone asks the learner to state who benefits, what the interface promises and how its behavior is verified. AI can draft scripts and documentation, but a real team-workload fixture and negative tests determine completion. The mentor asks for local output before declaring a checkpoint passed.

## Final projects

Choose one extension. Reuse the local platform and two baseline teams, but implement the extension's policy and workflow independently. Each option includes a third synthetic team and an author-verified acceptance script.

| Option | User need and required hard case |
| --- | --- |
| **Dataset onboarding** | A team registers a source/owner/schema and receives validation plus a catalog entry. A breaking field change must fail with a migration path; an optional field addition proceeds. |
| **Safe release service** | A team promotes a checked pipeline version through local development and release environments. A failed post-deploy check restores the previous runnable version and its visible status. |
| **Operational console** | A team sees freshness, failures, last good artifact and owner across projects. A job succeeds while source data is stale; the console flags the stale source independently. |

The AI mentor helps choose, define the platform user, draft an interface and identify positive/negative checks. The learner approves a bounded brief and implements it in the final two weeks. Deliver request/config schema, local CLI or scripts, versioned templates, access tests, operational view, runbook, migration/rollback demonstration and one AI suggestion verified or corrected. Optional extra services are out of the core assessment.

Score 0–2 for eight dimensions: user contract, repeatable provisioning, access control, release safety, observability, lifecycle/cleanup, reproducibility and explanation. Proposed pass **13/16** with provisioning, access, release safety and lifecycle each at 2. An unseen third-team request tests generality. AI scoring is advisory.

## Wiki and release work

Reuse [pipeline](../content/wiki/data-engineering/data-pipeline.md), [contract](../content/wiki/data-engineering/data-contract.md), [catalog](../content/wiki/data-engineering/data-catalog.md), [metadata](../content/wiki/data-engineering/metadata.md), [lineage](../content/wiki/data-engineering/data-lineage.md), [observability](../content/wiki/data-engineering/data-observability.md), [idempotency](../content/wiki/data-engineering/idempotency.md) and [retry](../content/wiki/data-engineering/retry.md). Add canonical articles on self-service platform users/interfaces, tenancy and least privilege, local provisioning, release/rollback, contract migration, ownership and service levels. Add tool-specific setup under Công nghệ only when the tested stack is chosen. The course pack embeds actual reviewed excerpts, user contracts, scripts and checks rather than bare links.

Release gates: tested local stack and first-team onboarding; second-team provisioning and access denial; failure/rollback/retirement drills; each final option piloted with a new team request. Publish tested machine requirements, expected outputs and time costs. A partial release lists available milestones explicitly.
