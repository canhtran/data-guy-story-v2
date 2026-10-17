# Data Guy Story — Theme and Website Experience Plan

Updated: 27 September 2026.

Status: implementation started 1 October 2026. The first local prototype is in the repository; remaining phases and visual review are open. Nothing has been deployed by this task.

Follows the [general website plan](website-general-plan.md), [Wiki structure and coverage plan](wiki-structure-and-coverage-plan.md), and [Nhập môn Data Engineering plan](nhap-mon-data-engineering-plan.md). Curriculum details remain owned by those plans.

## 1. Direction

Maintain a Data Guy Story design layer in this repository, using Hextra as the initial foundation. Own our visual identity, content conventions, and learning-specific templates. Keep using upstream features where they satisfy our requirements.

Do not fork Hextra or create a separate theme package initially. Reconsider that boundary after implementing a representative learner journey and measuring the maintenance burden.

The experience should make three facts immediately clear: learning is free, readers can follow a learning path, and they can explore the Wiki. Preserve the author's conversational Vietnamese voice and make long technical articles comfortable to read.

## 2. Current baseline

- Hugo imports Hextra, pinned to v0.12.1 in `go.mod`.
- The homepage now has two primary entry points, with custom site styling on top of Hextra.
- The learning-path hub now shows the five planned paths; all five path overviews are published with honest planned/authoring labels. The introductory first module is a clearly labeled draft prototype. Older technology-specific draft pages remain unlinked pending reconciliation.
- Existing customizations include a story-list shortcode, metadata links in the custom head partial, and machine-readable outputs.
- Development configuration includes drafts. Production preview checks must therefore run separately from the development preview.
- Netlify configuration specifies Hugo 0.156.0. Before implementation, inspect the GitHub Pages workflow and identify the active deployment route and any version differences.

Preserve existing custom behavior while introducing templates. Generated output directories are not the source of design changes.

## 3. Ownership and boundaries

| Area | Initial ownership |
| --- | --- |
| Colors, typography, spacing, reading width, component appearance | Data Guy Story |
| Homepage and section hubs | Data Guy Story |
| Path overview, weekly module, project and milestone presentation | Data Guy Story |
| Content metadata and relationships | Data Guy Story, independent of Hextra |
| Documentation shell, search, code presentation, theme switching | Hextra where suitable; verify behavior in our pages |
| Curriculum, assessment, AI mentor instructions and pack generation | Separate content work; theme presents available artifacts |

Initial implementation excludes accounts, a hosted AI chat service, server-side progress storage, and an LMS. Position in a path is part of navigation; recorded learner completion is a separate optional feature.

## 4. Page requirements

| Page | Required experience |
| --- | --- |
| Homepage | Short introduction; prominent learning-path and Wiki entry points; secondary stories and Blog links; truthful availability |
| Learning-path hub | Five primary paths, audience, prerequisites, outcomes, and availability; duration only when validated |
| Path overview | Outcomes, prerequisites, workload, ordered modules, guiding project, final project, and an available starting point |
| Weekly module | Goal, AI-guided local setup/prerequisites, mentor source references, project work, milestone evidence, reflection, current position, previous/next available module |
| Wiki hub/category | Clear subject grouping, introductory entry points, and reference navigation without forcing a curriculum sequence |
| Wiki article | Readable prose, code and tables; prerequisites, table of contents where useful, related concepts and relevant paths |
| Story and Blog | Preserve distinct editorial roles; readable lists and articles; visible sources for stories |

For every path, accommodate an AI-companion start panel, local setup guidance and course-pack download when those resources exist. Explain how to continue directly on the website. The theme must not imply an AI integration or downloadable pack is available before it is delivered.

## 5. Design principles and components

Define a small set of design tokens before styling individual pages: semantic colors for both themes, typography supporting Vietnamese diacritics, spacing, widths, borders, radii, and focus states. Start with the existing font setup and assess readability before adding font downloads.

Build reusable components for:

- Fully clickable path cards with audience, outcome, free-access message, and availability; each opens a detail page.
- Prerequisite and workload summaries.
- Ordered module lists with current position and availability.
- Mentor source references with targeted reading available when useful.
- Project briefs and milestone checklists.
- Previous/next navigation within a path.
- Available AI-companion and course-pack links.
- Related Wiki articles and source references.

Use restrained visual hierarchy and real Vietnamese sample content. Availability must be conveyed in text, not color alone. Preserve semantic headings, visible keyboard focus, sufficient contrast, and usable controls on small screens. Wide tables and code blocks should scroll within their containers rather than overflow the page.

## 6. Template and content approach

Keep CSS in the supported custom stylesheet entry point, initially `assets/css/custom.css`. Keep shared presentation in site partials and use explicit page layouts for learning experiences. Override upstream templates only where needed, recording why each override exists.

Before choosing exact template filenames, verify Hugo's layout lookup against the pinned runtime and existing `type`, `layout`, `contentType`, and cascade values. A `contentType` field alone must not be assumed to select a template.

Propose a minimal content contract, confirmed during the first prototype:

| Entity | Proposed metadata |
| --- | --- |
| Path | Stable identifier, audience, outcomes, prerequisites, availability, optional validated workload, ordered module references |
| Module | Path identifier, sequence, goals, prerequisite references, reading references, milestone, availability |
| Related resource | Internal page reference or explicit external URL; meaningful label |
| Course pack | Available artifact URL, version, and updated date |

Keep substantial teaching content in Markdown rather than large front-matter structures. Resolve internal relationships through Hugo page references instead of hard-coded domain URLs. Treat the ordered module list as the source of sequence and validate any module-level sequence metadata against it.

Separate publication from reader-facing availability. Hugo `draft` controls build inclusion; an availability label describes what readers can use. A published overview may describe a planned module without linking to its excluded draft. Missing required references should be caught during validation, not silently produce broken links.

Retain the existing published URL structure where possible. Inventory published routes before restructuring draft paths; add redirects if a published route must change. Preserve Markdown outputs, `llms.txt`, alternate links, and sitemap/robots behavior during template changes.

## 7. Delivery phases

### Phase 1 — Requirements and visual baseline

Inventory current templates, shortcodes, content types, routes, deployment settings, and existing theme dependencies. Capture representative pages in both themes and at mobile and desktop widths.

Produce a short design specification, token proposal, page wireframes, and metadata contract. Use the introductory path as the concrete learner journey; represent its proposed duration as provisional until validated.

Exit condition: each requirement has a target page/component, and the first prototype has realistic sample content with no dependency on completing the entire curriculum.

### Phase 2 — Three-page prototype

Implement the homepage, one introductory path overview, and one weekly module in a local or draft-enabled preview. Introduce only the tokens and components needed for these pages.

Demonstrate a journey from homepage to path, module, Wiki reading, and back to the module. Use real available articles and clearly identified draft material. Check keyboard use, mobile navigation, dark mode, code, tables, and long Vietnamese titles.

Exit condition: the journey works, the design is coherent, and the Hextra review in section 9 supports continuing or identifies a concrete blocker.

### Phase 3 — Shared navigation and content coverage

Extend the approved components to the five-path hub, Wiki hubs, Wiki articles, and remaining learning templates. Align homepage and hub descriptions with the general plan. Reconcile the old Kafka, Spark, and Flink draft-path entries with their role as Wiki technology subjects.

Apply shared typography and components to stories and Blog while preserving their editorial differences. Add AI-companion and download controls only for resources actually delivered by the curriculum work.

Exit condition: all main page families share the design, navigation reflects the agreed structure, and unavailable content is handled consistently.

### Phase 4 — Production verification and rollout

Build with the production draft policy and active deployment runtime. Review the generated site, check internal links and assets, and inspect the route inventory for unintended changes. Verify search, mobile menus, theme switching, machine-readable outputs, and existing custom shortcodes.

Ship theme changes in reviewable increments: design tokens, prototype templates, wider rollout, and final navigation reconciliation. Keep a known-good revision for rollback and document any redirect changes. Deploy only when implementation scope includes publishing.

Exit condition: production checks pass and no excluded draft is presented as an accessible required step.

## 8. Acceptance checks

- A new reader can identify the Wiki and learning-path entry points and reach a usable starting page.
- A module clearly shows its goal, project task, checkpoint, and next available step.
- All required source references and downloads resolve in the production build.
- Planned modules remain understandable without broken links or misleading start buttons.
- Representative pages work at approximately 360px, 768px, and 1440px widths, in both themes and with keyboard navigation.
- Long Vietnamese titles, diacritics, code blocks, tables, and empty/partial content states remain readable.
- Search returns published content as expected and does not expose excluded draft content.
- Existing published URLs and machine-readable outputs remain usable, or intentional changes have explicit redirects.
- Compare page weight and basic performance with the baseline; investigate material regressions before rollout.

Automate content-reference and template checks where they protect meaningful behavior. Use visual and keyboard review for presentation. A production Hugo build is required for implementation changes; writing this plan alone does not require one.

## 9. When to reconsider Hextra

Review after the three-page prototype and again after the wider rollout. Record the overridden templates, private upstream classes relied upon, duplicated navigation behavior, and effort needed for a trial upstream update.

Continue with Hextra when our pages can be expressed through a small, understandable set of extensions. Consider an independent theme when core navigation or layout must be repeatedly replaced, overrides spread across most page families, or upgrades require substantial repairs to our experience.

If that point is reached, write a migration proposal covering feature parity, accessibility, search, build outputs, URLs, maintenance cost, and rollback. Reuse our tokens, components, and content contracts. Do not make a full fork an automatic consequence of visual customization.

## 10. Maintenance and next step

Keep the upstream version pinned and update deliberately. For each upgrade, review upstream changes, run production checks, and inspect representative pages in both themes. Document custom template responsibilities and avoid editing downloaded module files.

Phase 1 inventory and the first content/styling prototype have begun. The next implementation work is to inspect the homepage, hub, introductory overview and draft module at mobile and desktop widths in both themes; then add the first executable learner fixture and tested setup recipe before describing the module as available. Continue Phase 3 only after that visual and learner-flow review. Calendar estimates should follow the remaining template and content inventory.

Reference: [Hextra customization documentation](https://imfing.github.io/hextra/docs/advanced/customization/). Verify extension points against our pinned version during implementation.

## 11. Prototype implementation record — 1 October 2026

- Added a five-path data file and a reusable fully clickable path-card shortcode; each card opens a detail overview.
- Replaced old homepage and hub descriptions with the agreed AI-first, locally executed learning journey.
- Added published overviews for all five paths, including a shared free-access note, with the introductory overview marked “Đang biên soạn” and a draft week-one page marked as a preview; no course pack or complete lab is advertised. Published the Chuyện thực tế hub with a clear coming-soon message so the homepage and navigation links resolve.
- Added semantic light/dark color tokens and responsive card/button styles in `assets/css/custom.css`; Hextra remains the navigation and documentation shell.
- Production and draft builds pass with local Hugo 0.160.1; the production entry links were checked under a subpath base URL. The deployment workflow pins Hugo 0.156.0, so the exact CI build still needs verification. Browser automation failed to initialize during this task; visual, keyboard, search and mobile checks remain open.

### Follow-up — free access and path details

The homepage and learning-path hub now state that required content, datasets and lab software are free. A reusable note on each detail page explains that an AI free-access option may have usage limits and that the website remains usable directly. Every path card is one keyboard-focusable link to a detail page. Detail pages use the same sections for audience, outcome, guided project, weekly progression, final choices and current availability. Production build and link checks were repeated after this change.

### Follow-up — learning-path navigation

The learning-path hub, five detail overviews and draft week-one module now set Hextra’s `sidebar.hide` page parameter. This hides the redundant left sidebar at desktop widths while retaining the mobile navigation drawer. Wiki pages keep their topic sidebar. Path cards and return links provide navigation within the learning-path area; add module-specific previous/next navigation when full weekly lessons are published. The production build and generated sidebar classes were checked after this change.

### Follow-up — Chuyện thực tế

The story hub now introduces the author’s approach: source context, engineering decisions/results, and the author’s interpretation. Four category cards show the planned coverage; a category becomes a link only when it has published stories. The recent-story list includes source publisher and date and collects stories across categories. The empty state disappears automatically when articles are available. The story archetype now prompts source attribution, unknowns, tradeoffs and the author’s view. Production build, empty state and populated state were checked with an isolated temporary article; screenshot review remains pending.

### Follow-up — Wiki and story sidebars

The Wiki landing page hides its desktop sidebar. Wiki sections show their own child topics; articles show their parent topic’s articles with a return link to Sổ tay and `aria-current` on the active page. The site overrides Hextra v0.12.1’s sidebar partial only to select that navigation root and add the topic header/semantic active state; review this file during upstream upgrades. Shared CSS aligns spacing, hover and current-page styles with the site’s teal tokens. Story descendants inherit the hidden-sidebar setting. Production/draft builds and rendered navigation scoping were checked; visual review remains pending.

### Follow-up — Blog

Site-owned `layouts/blog/list.html` and `single.html` replace the Hextra Blog presentation while preserving its base shell, mobile navigation, pagination and comments. The index has a personal introduction, compact date/topic/excerpt rows and links to existing tag pages. Articles use a centered reading width, author/date metadata, return link and three latest other posts under “Đọc tiếp.” No new topic classifications or article rewrites were applied. Production and draft builds pass, internal links across the index and five existing posts resolve under a subpath base URL, and the article source files are unchanged. Visual review remains pending.

### Navigation and list pagination

The menu now places Lộ trình học before Wiki. Navigation and current learning-page links use the Wiki label; the original introduction keeps its personal wording. Blog and Stories paginate at 10 posts per page, including story topic indexes. Stories render pagination in the list template so page two shows a different set of posts. Production and development builds pass; temporary content verified distinct second pages and navigation for both sections and a story topic.

### Website sources for NotebookLM

Each of the five learning paths now links to a published `hoc-cung-ai/` source page. Per the user's correction, there are no downloadable packs. Each source page embeds the selected available Wiki articles, the path outline, a small conceptual exercise, local setup preflight checks, a Vietnamese mentor prompt and progress handoff instructions. A shared guide explains importing one public URL and then pasting the prompt into chat; website imports do not crawl linked articles. Localhost links cannot be imported by Google's service, so the public URLs need the website update to be published before use. No deployment was performed.

Sources are configured in `data/notebooklm.yaml`; the shortcode reads live published Hugo pages and fails builds if references are missing or draft. Relative links and heading IDs are rebased for embedded content. The mentor distinguishes preview reading from unavailable course labs, waits for actual local results, asks about OS/tools before setup, and does not claim to operate the learner's computer. Production/development builds and five pages' embedded content/links/anchors were checked. Actual authenticated NotebookLM import and mentor behavior have not been tested.

### NotebookLM v0.2 usability and first session

Source pages now lead with import steps, a public URL copy button, and six prompt modes (start, setup, debug, review, final project, resume). The repeated full parent overview was removed from the source-page opening. Prompts render server-side with readable text and a copy fallback when clipboard access is denied. Introductory source includes an executable Python/SQLite first session, expected results and failure/correction cases, a six-stage checkpoint map and final-project brief guidance. Full PostgreSQL course labs remain explicitly unfinished. Verified live HTML, copy handler success/fallback and the four local exercise outcomes.
