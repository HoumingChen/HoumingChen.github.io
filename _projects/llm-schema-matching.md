---
layout: project
title: LLM-Based Schema Matching
order: 2
course: EECS 584 Advanced Database Systems
period: Fall 2023
context: Team course project
summary: Comparing prompting strategies for matching database fields from schema metadata.
description: A graduate database course project evaluating LLM prompting strategies for schema matching.
report: /assets/projects/llm-schema-matching/course-report-2023.pdf
authors:
  - Houming Chen
  - Zhuocheng Sun
  - Yifan Zhu
---

Schema matching identifies fields that represent the same concept across databases. This team project explored whether LLMs could match fields from schema metadata without task-specific training.

We compared GPT-3.5 and GPT-4 using direct prompts, in-context examples, step-by-step prompting, and self-refinement, alongside traditional schema matchers. The main evaluation matched Schema.org to 12 metadata schemas in the RDA Crosswalk benchmark.

<figure class="project-result">
  <table>
    <caption>GPT-4 prompting comparison</caption>
    <thead><tr><th scope="col">Prompting strategy</th><th scope="col">Mean F1</th></tr></thead>
    <tbody>
      <tr><th scope="row">Direct prompting</th><td>0.835</td></tr>
      <tr><th scope="row">In-context examples</th><td>0.868</td></tr>
      <tr><th scope="row">Self-refinement</th><td>0.782</td></tr>
    </tbody>
  </table>
  <figcaption>Reported means across the 12 schemas in the 2023 course experiment (Table 3). Higher F1 is better.</figcaption>
</figure>

Examples improved matching in this comparison, while self-refinement did not. More elaborate prompting was not consistently better; some model outputs also required manual parsing.
