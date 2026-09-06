# AI-friendly content guidelines

The site exposes three machine-discovery layers:

- `/sitemap.xml` lists canonical HTML pages for search crawlers.
- `/llms.txt` provides a concise, curated content map for assistants.
- Every published content page also has a Markdown alternative. For example, `/blog/example/` is HTML and `/blog/example.md` is clean source content. HTML pages advertise this using `rel="alternate" type="text/markdown"` and point back to `/llms.txt` with `rel="describedby"`.

Drafts remain excluded from production HTML, Markdown, the sitemap, and `llms.txt`. Local `hugo server` includes them through the development configuration.

## Authoring requirements

Every published page should have a specific `title` and a one-sentence `description`. Start with a direct definition or summary, use descriptive headings, explain abbreviations on first use, and link prerequisite and related concepts. Set `llms: false` only when a utility page should be excluded from the AI index.

Do not create parallel prose for assistants. The Markdown alternative uses the same source as the human-readable page, so corrections remain consistent across both formats.

## Chuyện thực tế

Create curated stories with `hugo new --kind story stories/<category>/<slug>.md`. Before publishing, populate:

- `original_title`
- `source_url`
- `source_publisher`
- `source_author`, when known
- `source_published`, when known
- `topics` and `technologies`

Clearly distinguish facts reported by the original engineering team from Data Guy Story’s interpretation. Link the original article visibly, paraphrase rather than reproduce it, and record meaningful secondary sources. The page description should state the company, system, and engineering problem so humans and assistants can identify the article without relying on its title alone.

Story articles are excluded from the Hextra sidebar. The sidebar shows only the four category hubs; each category page automatically lists its published stories through the `story-list` shortcode.
