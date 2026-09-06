# Content migration plan

This phase adds draft Wiki hubs, concepts, and learning paths while retaining the published homepage letter. Existing article URLs are preserved. No existing article was moved or deleted.

## Scaffold decisions

- The draft reference taxonomy is nested below `content/wiki/`, giving it one Hextra sidebar tree. Its reader-facing name is “Sổ tay Data Engineering,” while `/wiki/` remains the stable technical URL. Lộ trình học, Chuyện thực tế, and Blog are separate top-level destinations. The main menu is ordered as Sổ tay, Lộ trình học, Chuyện thực tế, and Blog; search and social icons remain utility actions. The former root Wiki section URLs have aliases to their new hubs, including `/bat-dau/` → `/wiki/bat-dau/`. The short-lived `/wiki/stories/` URL redirects to `/stories/`.
- `content/_index.md` retains the original published welcome letter. Its overview and cards now introduce the four content areas: Sổ tay, Lộ trình học, Chuyện thực tế, and Blog. The linked scaffold pages remain drafts until they are ready to publish.
- Use `content/wiki/nen-tang/database/database-index.md` instead of the requested `index.md`. Hugo reserves `index.md` for leaf bundles; it cannot serve as an ordinary concept article alongside a section's `_index.md`. Its future URL is `/wiki/nen-tang/database/database-index/`.
- Hextra already renders page titles as H1 headings. Placeholder bodies start with introductions and H2 sections to avoid duplicate titles. The existing theme's default templates render the new `hub`, `concept`, and `learning-path` types; no custom layouts are needed.
- All new content is `draft: true`. Local development enables drafts through `config/development/hugo.yaml`, so `hugo server` serves `/wiki/bat-dau/`, `/learning-paths/`, `/wiki/nen-tang/`, `/wiki/data-engineering/`, `/wiki/technologies/`, and `/stories/` without extra flags. Production builds intentionally omit the scaffold. Add public navigation only when the destination pages are ready to publish.
- Metadata relationships remain empty pending editorial review. Internal navigation uses Hugo `relref` links to real source files. Learning paths contain reading sequences, not copies of Wiki articles. Stories contain category hubs only.

## Existing content inventory

Suggested paths are editorial proposals only, not redirects or instructions to move files now. High risk means a published URL or homepage would change; medium risk includes section navigation, internal links, images, or overlapping content that needs review. Pages marked “keep” remain in their current section.

| Existing page | Current path | Suggested new section | Suggested future path | Migration risk | Notes |
| --- | --- | --- | --- | --- | --- |
| 👋 | `content/_index.md` | Homepage (keep) | `content/_index.md` | Low | Keep the audience letter and maintain its links as the site structure evolves. |
| Về tui | `content/about.md` | About (keep) | `content/about.md` | Low | Keep author profiles and URL. |
| Câu chuyện về các bạn user kì cục | `content/blog/2021-05-29-cau-chuyen-ve-cac-ban-user-ki-cuc.md` | Blog (keep) | `content/blog/2021-05-29-cau-chuyen-ve-cac-ban-user-ki-cuc.md` | Low | Keep the personal/career story, current URL, author attribution, and image paths; no clear Wiki migration is required. |
| Tại sao data engineer cần biết Docker | `content/blog/2022-06-18-tai-sao-data-engineer-can-biet-docker.md` | Blog (keep) | `content/blog/2022-06-18-tai-sao-data-engineer-can-biet-docker.md` | Low | Keep the personal/career story, current URL, author attribution, and image paths; no clear Wiki migration is required. |
| Đọc vị manager trong 10 phút | `content/blog/2025-02-20-doc-vi-manager-trong-10-phut.md` | Blog (keep) | `content/blog/2025-02-20-doc-vi-manager-trong-10-phut.md` | Low | Keep the personal/career story, current URL, author attribution, and image paths; no clear Wiki migration is required. |
| Lời nhắn nhủ và cách học hành | `content/blog/2025-03-30-loi-nhan-nhu-va-cach-hoc-hanh.md` | Blog (keep) | `content/blog/2025-03-30-loi-nhan-nhu-va-cach-hoc-hanh.md` | Low | Keep the personal/career story, current URL, author attribution, and image paths; no clear Wiki migration is required. |
| Giao việc cho sếp | `content/blog/2025-06-01-giao-viec-cho-sep.md` | Blog (keep) | `content/blog/2025-06-01-giao-viec-cho-sep.md` | Low | Keep the personal/career story, current URL, author attribution, and image paths; no clear Wiki migration is required. |
| 📘 Sổ tay Data | `content/docs/_index.md` | Wiki entry / Bắt đầu | `content/wiki/bat-dau/_index.md` | High | Preserve the existing introduction; decide how to retain the personal narrative before any consolidation. |
| Kiến thức nâng cao | `content/docs/advanced/_index.md` | Công nghệ | `content/wiki/technologies/_index.md` | Medium | Current scope spans multiple technologies; review each topic before consolidating. |
| Nền tảng - Hành trang cho người mới | `content/docs/foundation/_index.md` | Nền tảng | `content/wiki/nen-tang/_index.md` | High | Reconcile reading order and existing child links before merging hubs. |
| 4. Các loại dữ liệu | `content/docs/foundation/cac-loai-du-lieu.md` | Nền tảng | `content/wiki/nen-tang/cac-loai-du-lieu.md` | High | Suggested future article is outside this scaffold; preserve reading-sequence links. |
| 2. Data Engineer là gì? | `content/docs/foundation/data-engineer-la-gi.md` | Bắt đầu | `content/wiki/bat-dau/data-engineer-la-gi.md` | High | Clear match. Existing article remains canonical for now; new draft only points to it. Merge into the scaffold only in a future migration. |
| 1. Data là gì? | `content/docs/foundation/data-la-gi.md` | Nền tảng | `content/wiki/nen-tang/data-la-gi.md` | High | Suggested future article is outside this scaffold; retain the current beginner explanation. |
| 3. Vòng đời của Data | `content/docs/foundation/vong-doi-cua-data.md` | Nền tảng | `content/wiki/nen-tang/vong-doi-cua-data.md` | High | Suggested future article is outside this scaffold; preserve reading-sequence links. |
| Giới thiệu | `content/docs/introduction.md` | Bắt đầu | `content/wiki/bat-dau/_index.md` | Medium | Existing draft references the homepage and old docs hub; review links and avoid duplicating introductions. |
| Học từ những người đi trước | `content/docs/real-world/_index.md` | Chuyện thực tế | `content/stories/_index.md` | Medium | Introduction only; do not turn its examples into unsourced case studies. |

## Validation

Run `hugo --gc --minify` for the production build and `hugo --environment development --gc --minify` for the complete scaffold. A plain `hugo server` also uses the development environment and includes drafts. Verify both the database hub and database index article have separate outputs, and check learning-path links in the development build. Existing article content must remain byte-for-byte unchanged. The baseline build emits a Hextra `.Site.Data` deprecation warning; upgrading the theme is outside this task.
