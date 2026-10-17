# Data Guy Story: General Website Plan

Updated: 27 September 2026.

Status: general planning baseline. This supersedes the earlier detailed editorial strategy and its six-path proposal. Weekly curricula, article inventories, project specifications, and website changes will be developed in separate component plans.

## 1. Purpose

Build a Vietnamese-language resource that helps readers understand data engineering, practice it through projects, and return for reference as their work becomes more advanced.

Serve two complementary needs:

- Guided learning through weekly modules, projects, and measurable progress.
- Independent learning and reference through a broad, systematically organized Wiki.

Keep the author's conversational Vietnamese voice. Explain technical terms carefully, use concrete examples, and develop engineering judgment alongside implementation skills.

## 2. Main Website Components

Retain the existing four main destinations.

| Component | Purpose | Contains |
| --- | --- | --- |
| Sổ tay / Wiki | Systematic knowledge and reference | Fundamentals, engineering concepts, technology explanations, examples, and technical references |
| Lộ trình học | Structured learning through practice | Five weekly paths, guiding projects, milestones, and independent final projects |
| Chuyện thực tế | Learn from real engineering decisions | Sourced stories about architecture, incidents, migrations, and scaling |
| Blog | Learn from the author's experience | Personal perspectives on learning, careers, collaboration, and engineering work |

Learning paths draw from the Wiki. Stories show ideas in real settings. Blog articles add personal perspective. Each component remains useful on its own.

## 3. Wiki Structure and Scope

Keep the current top-level Wiki structure.

| Category | Reader question | Scope |
| --- | --- | --- |
| Bắt đầu | What is this profession, and where do I begin? | Roles, responsibilities, data flow, collaboration, and orientation |
| Nền tảng | What underlying knowledge do I need? | SQL, programming, databases, modeling, distributed systems, and relevant computing foundations |
| Data Engineering | What engineering problems must I understand? | Ingestion, processing, storage, quality, reliability, orchestration, metadata, governance, and architecture concepts |
| Công nghệ | How does a particular technology work? | Tool-specific architecture, use, configuration, troubleshooting, and operation |

### Coverage Principles

- The Wiki is broader than the learning paths. Not every article needs to appear in a path.
- Develop systematic coverage within each category, including advanced and reference material.
- Add missing subcategories as needed while preserving the top-level structure.
- Maintain one canonical explanation per concept and link to it from paths and related articles.
- State prerequisites and distinguish introductory material from advanced explanations.
- Define clear boundaries: orchestration as a concept belongs in Data Engineering; a particular orchestrator's implementation belongs in Công nghệ.
- Treat completeness as a long-term coverage goal within a defined scope. Completing the entire Wiki is not a prerequisite for publishing a learning path.

The Wiki component plan will define subcategories, coverage gaps, article inventories, and review priorities. This general plan does not prescribe individual article assignments.

## 4. Five Weekly Learning Paths

| Path | Audience and purpose | Completion outcome |
| --- | --- | --- |
| Nhập môn Data Engineering | Beginners learning the profession and essential technical skills | Build and explain a small end-to-end pipeline using basic SQL, Python, databases, and modeling |
| Data Engineering thực chiến | Readers with introductory foundations who want to build a complete analytical warehouse | Integrate changing sources; model facts, dimensions and history; schedule, verify and recover a local warehouse |
| Data Engineering nâng cao: Spark & Lakehouse | Readers ready to reason about distributed batch processing and table formats | Build and troubleshoot a local distributed Spark lakehouse, including replay, performance and recovery |
| Streaming Engineering | Readers ready to process events continuously | Build and reason about an event pipeline, including state, late data, duplicate delivery, and recovery |
| Data Platform Engineering | Readers ready to build shared capabilities for data teams | Build a small reusable platform with provisioning, access control, deployment workflows, observability, and onboarding |

Reader-facing description for **Data Engineering thực chiến**: "Học cách thiết kế, xây dựng và vận hành hệ thống dữ liệu qua một dự án hoàn chỉnh."

### Progression

```text
Nhập môn Data Engineering
          ↓
Data Engineering thực chiến
          ├──→ Data Engineering nâng cao: Spark & Lakehouse
          ├──→ Streaming Engineering
          └──→ Data Platform Engineering
```

Spark & Lakehouse, Streaming, and Platform Engineering are distinct branches after Thực chiến. Readers may take them in any order; Spark is not a prerequisite for Streaming or Platform. Experienced readers may enter by demonstrating each path’s prerequisite challenge. All required infrastructure runs locally with AI-guided setup and troubleshooting.

Nhập môn Data Engineering provides orientation and introductory technical foundations through a small project. Data Engineering thực chiến is the main, more advanced data engineering learning journey: readers deepen their understanding of the discipline and apply it to designing and building complete data systems.

Its scope includes requirements and architecture, ingestion and integration, analytical storage, data modeling, transformations, processing approaches, orchestration, quality, and engineering tradeoffs. Testing, deployment, monitoring, and recovery are parts of this broader curriculum, not its defining scope. The component plan will decide the depth and sequence of these subjects and which technologies support the learning goals.

Data Engineering thực chiến develops the ability to deliver data systems for business needs. Data Platform Engineering specializes in shared infrastructure and capabilities that help multiple engineers or teams deliver those systems. Streaming Engineering specializes in continuous event processing. The advanced depth of Data Engineering thực chiến describes progression beyond the introduction, not a promise of senior professional status.

Spark is the central processing engine of the advanced lakehouse path; Kafka and Flink support Streaming Engineering. The Wiki remains the canonical home for technology explanations and may cover more tools than the paths require.

### Duration

Every path will have a defined number of weeks. Final durations will be set in the individual component plans after estimating reading, setup, practice, and project effort.

Current component plans propose 6 weeks for Nhập môn and 8 weeks each for Thực chiến, Spark & Lakehouse, Streaming, and Platform. Each includes final-project time. These are estimates to validate with learner pilots; setup and debugging time count within the schedule.

Weeks describe a recommended pace. Readers can progress at their own speed.

## 5. Common Learning-Path Structure

**Cost rule:** All required articles, course packs, synthetic datasets and lab software are free to access or install. No paid cloud account, hosted CI plan or AI subscription is a prerequisite. AI-assisted lessons should work within a free-access option when available and provide a direct website route when AI access or quotas are unavailable. Verify service limits and availability before release. Learners provide their own computer and internet access for downloads and an online AI companion.

Each path contains three connected elements.

| Element | Role |
| --- | --- |
| Wiki source material | Supply the canonical explanations the AI mentor uses as tasks require them; direct reading remains available |
| Guiding project | Provide a supported project that develops through weekly milestones |
| Final project | Ask readers to apply their skills independently to a different problem or requirement |

### Weekly Modules

Each weekly page contains:

1. Learning goal: what the reader should be able to do afterward.
2. Prerequisites: knowledge and environment needed before starting.
3. AI mentor entry: a concrete question, one task and the Wiki material it uses; targeted reading is offered when helpful.
4. Local setup or project work: instructions, expected behavior and troubleshooting checks.
5. Milestone check: observable output and an explanation of what was verified.
6. Reflection and next step: a small changed case, a progress note and the next module.

A milestone is a checkpoint inside a path, not another path or navigation system. Each week produces an observable result; larger checkpoints can combine several weeks of work.

The path owns project instructions, integration tasks, and assessment. The Wiki owns reusable explanations. Weekly pages connect the mentor and project work to canonical Wiki sources without repeating entire articles. Learners start with AI, execute locally and verify results; direct reading remains a supported route.

### Local setup with AI guidance

All course data infrastructure runs on the learner’s computer. Learners follow AI guidance to install, configure, verify and troubleshoot tools using tested course recipes. The mentor checks the operating system and existing environment, explains one step at a time, and diagnoses problems from commands, logs and observed results. Courses supply configuration templates and expected checks; learners carry out setup and record how to restart and reproduce it. Installation and debugging count toward the learning schedule. No cloud deployment or hosted CI service is required. The AI companion itself may be an online service; local model installation is not a course prerequisite.

### Guiding Project

- Use one coherent project throughout each path.
- Introduce capabilities as the reader learns the necessary concepts.
- Provide starter material, understandable sample data, expected results, and troubleshooting guidance.
- Demonstrate successful behavior and relevant failure scenarios.
- Keep setup and resource requirements appropriate to the audience.
- Reuse a familiar business domain across paths when useful, but make each project reproducible without requiring artifacts from a previous course.

### Final Project

- Provide a brief, requirements, constraints, deliverables, and assessment rubric.
- Change a meaningful requirement or dataset so readers must make decisions independently.
- Allow AI, Wiki and documentation help while the learner owns decisions, runs checks, explains the result and adapts to a changed case. Do not supply a finished step-by-step implementation as the assignment.
- Assess correctness, reproducibility, reasoning, and the operational skills taught in that path.
- Reserve adequate time within the weekly schedule and publish clear completion criteria.

Detailed project designs belong in the individual path plans.

## 6. Supporting Content

### Chuyện Thực Tế

Keep the existing categories: architecture, incidents, migrations, and scaling.

Stories identify the original source, explain the problem and constraints, examine the engineering decision, and distinguish reported facts from the author's interpretation. They link to relevant Wiki explanations and may be recommended within a path.

The component plan will define source selection, attribution, story structure, and initial topics.

### Blog

Preserve the personal voice and existing articles. Focus on learning, collaboration, career development, and reflections from engineering work.

Blog articles can support a path without becoming required technical prerequisites. The component plan will define themes and a sustainable publishing approach.

## 7. Reader Experience

Make two choices easy: follow a learning path or explore the Wiki.

- The homepage clearly explains these entry points.
- The learning-path hub presents five paths with their audiences, prerequisites, outcomes, and availability.
- Each path overview shows the weekly sequence, guiding project, final project, workload, and completion expectations.
- Weekly pages show the reader's place in the sequence and the next step.
- Wiki hubs organize subjects for learning and reference without imposing the weekly curriculum on the entire library.
- Required links lead to available content. Unfinished sections are clearly identified and do not create broken journeys.

The website-experience component plan will address page templates, navigation, progress display, and reconciliation of existing draft paths. Preserve published URLs or deliberately plan redirects when changes are needed.

## 8. Shared Quality Principles

- One clear purpose per article or module.
- Explicit prerequisites and explanations of unfamiliar terms.
- Concrete examples with visible inputs, outputs, and assumptions.
- Consistent technical vocabulary and readable Vietnamese prose.
- Executable examples verified in a documented environment.
- Exercises that demonstrate understanding rather than copying alone.
- Clear attribution and separation of evidence from opinion.
- Working links, readable mobile layouts, and no unfinished material presented as complete.

Reusable writing templates, example conventions, technical review, and publication checks will be defined in an editorial standards plan.

## 9. Delivery Approach

1. Define the Nhập môn path's audience, outcomes, guiding project, workload, and weekly outline.
2. Map its required readings to the existing Wiki and identify missing prerequisites.
3. Write or improve those Wiki articles alongside the corresponding project milestones.
4. Review the sequence with beginner readers and adjust unclear steps.
5. Release coherent learning units, clearly describing partial availability until the whole path is ready.
6. Develop Data Engineering thực chiến, then pilot the Spark & Lakehouse, Streaming, and Platform branches separately.
7. Continue expanding and maintaining the broader Wiki, stories, and Blog alongside the paths.

Near-term writing priorities may follow the first path. The Wiki coverage plan must still account for subjects outside that curriculum.

## 10. Smaller Plans to Develop

The component plans below define proposed curricula; executable lessons, datasets and labs are separate authoring work.

| Component plan | Decisions to make |
| --- | --- |
| Wiki structure and coverage | Category boundaries, subcategories, article inventory, gaps, and reference relationships |
| [Nhập môn Data Engineering](nhap-mon-data-engineering-plan.md) | Six-week AI-first introductory journey, guided café project and three final options |
| [Data Engineering thực chiến](data-engineering-thuc-chien-plan.md) | Proposed eight-week AI-assisted-first journey, multi-source café-chain guiding project, three final-project options, Wiki source map, and assessment |
| [Data Engineering nâng cao: Spark & Lakehouse](data-engineering-nang-cao-spark-lakehouse-plan.md) | Local Spark/Iceberg project, distributed processing and performance, three final options |
| [Streaming Engineering](streaming-engineering-plan.md) | Local Kafka/Flink event pipeline, time/state/recovery, three final options |
| [Data Platform Engineering](data-platform-engineering-plan.md) | Local self-service platform for two teams, access/release/operation, three final options |
| [Website experience](theme-and-website-experience-plan.md) | Hubs, weekly navigation, availability labels, existing draft-path reconciliation, and URL handling |
| [Editorial standards](editorial-standards-plan.md) | Templates, terminology, verified examples, attribution, AI review, and maintenance |
| Chuyện thực tế | Source policy, story format, category coverage, and initial selection |
| Blog | Themes, relationship to technical content, and publishing priorities |

Next implementation work: author and pilot the introductory setup and first project slice, then develop later paths in coherent units. Reconcile the expanded five-path roadmap with Wiki priorities as lessons are written.

## 11. Decisions and Boundaries

Agreed direction: five primary weekly paths; a guiding project and an independent final project in each; links to canonical Wiki content; a Wiki broader than the paths; and preservation of the current top-level Wiki structure.

To validate before publication: proposed workloads, hardware requirements, pinned compatible tool versions, datasets, executable labs and learner outcomes. The component plans provide the current curriculum decisions.

Earlier content, migration, AI-writing, and editorial strategy drafts are absent from this working tree. Do not treat their old references as active requirements; use the component plans linked above and reconcile any recovered material against the five-path roadmap.

This general plan does not rename pages, publish drafts, implement navigation, or change website behavior.
