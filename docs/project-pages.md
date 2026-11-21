# Project pages

The four concise course-project pages live in `_projects/`. Each Markdown file owns its title, course, dates, summary, team, report link, and page text. Jekyll's `projects` collection generates `/projects/<filename>/`.

- `_layouts/project.html` is the shared detail-page layout.
- `_layouts/projects.html` builds the index from the same metadata, sorted by editorial importance using `order`: ICA-SeFa, schema matching, distributed systems, then compilers. The listing omits dates; detail pages retain them, as requested on November 17.
- The homepage, sidebar, and current research-resume PDF link to these pages. The CV PDF is synchronized from the main DB resume; see the repository README.
- `_layouts/projects-archive.html` preserves the earlier projects index at `/projects/archive/`.
- Project images and report PDFs are in `assets/projects/`. They are served locally with the pages; no login is needed.

## Preview

Use the repository's pinned Jekyll dependencies (`bundle install`), then:

```sh
bundle exec jekyll serve --host 127.0.0.1 --port 4000
```

Open `http://localhost:4000/projects/`. This command does not deploy or push. The November 17 review server uses a temporary dependency installation and build directory. To restart that exact preview while those files remain available, run from this repository:

```sh
env BUNDLE_PATH=/tmp/website-project-pages-2026-11-17/bundle \
  BUNDLE_APP_CONFIG=/tmp/website-project-pages-2026-11-17/bundle-config \
  BUNDLE_FROZEN=true BUNDLE_WITHOUT=test \
  bundle exec jekyll serve --host 127.0.0.1 --port 4000 \
  --destination /tmp/website-project-pages-2026-11-17/site --disable-disk-cache
```

The preview was checked in Chromium at desktop and mobile widths, including image loading, local links and PDFs, menu navigation, and horizontal overflow. Windows also returned HTTP 200 for `http://localhost:4000/projects/`.

## Source and accuracy notes

Created November 17, 2026, from the owner's archived reports and contribution records in `../resume/background/`.

- **ICA-SeFa:** 2021 `Final_Report.pdf` from `~/old_projects/ica_sefa/ICA-SeFa_Archive/github/EECS-545-Project-ICA-SeFa-A-New-Efficient-Algorithm-to-do-Latent-Semantics-Factorization-in-GANs/working_tree/`. The mouth image is an unchanged JPEG stream from Figure 1, extracted with `pdfimages`. The 2021 course authors are credited separately from the independent continuation through 2022. No anonymous 2022 manuscript or private implementation archive is included. Historical evaluation caveats favor qualitative illustration over a superiority metric.
- **Distributed systems:** `~/old_projects/EECS_591/report_source/midterm_report.tex`, a combined proposal, midterm, and final-extension source despite its filename. Displayed Llama-2 counts come from Tables 4–5: 80 trials on buggy two-phase-commit/Paxos specifications, manual grading. The full multi-model study had 440 responses. No personal protocol assignment is inferred.
- **Schema matching:** `~/old_projects/SchemaMatching_Chen_Sun_Zhu/report_source/EECS591_final_report.tex`; its metadata identifies EECS 584, Fall 2023. GPT-4 means (0.835 / 0.868 / 0.782) come from Table 3, on 12 RDA Crosswalk metadata schemas. This course study is distinct from ConStruM. The report retains its original placeholder ACM boilerplate and is labeled an archived course report, not a publication.
- **Compilers:** `~/old_projects/EECS_583/report_source/main.tex`. Figure 1 is the unchanged `selective_flow.png`. Methods are prior work implemented/evaluated by a course team; Houming's supporting role remains in the internal contribution record; the page describes team work without attributing leadership. Faster runtimes came with substantial errors, so the page avoids an unqualified speedup claim.

The three TeX reports were rendered from temporary copies without changing the original archives. For compilers, only the undefined author macro, duplicate bibliography-style declaration, and mismatched citation key were repaired in the temporary copy. The TLA+ build tolerated original unitless spacing and duplicate labels; BibTeX skipped duplicate entries in the TLA+ and schema bibliographies. Rendered PDFs have resolved citations. Full rendering records were retained under `/tmp/website-project-pages-2026-11-17/` during this session.

Keep report versions, evaluation conditions, and individual/team attribution intact when revising these pages. The pages are intentionally short; longer technical detail belongs in the linked reports.


## November 20 resume preview

The current CV page renders the main DB resume as readable HTML and offers its matching PDF; the homepage identifies ConStruM as accepted at SIGMOD 2027. The portfolio pages and their importance order are preserved. The November 20 preview uses the existing dependency installation above, with output under `/tmp/website-resume-update-2026-11-20/site` and port 4000. The owner subsequently approved this preview for publication on November 20, 2026, and requested that the local preview server be stopped.
