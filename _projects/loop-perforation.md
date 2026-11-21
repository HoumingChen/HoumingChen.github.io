---
layout: project
title: Compiler Optimization through Loop Perforation
order: 4
course: EECS 583 Advanced Compilers
period: Winter 2024
context: Team course project
summary: Studying how compiler transformations trade numerical accuracy for reduced execution time.
description: A graduate compiler course project comparing greedy and selective loop perforation in LLVM.
report: /assets/projects/loop-perforation/course-report-2024.pdf
authors:
  - Yuhang Ning
  - Chen Huang
  - Yuanzhe Zheng
  - Houming Chen
  - Yucheng Huo
---

Loop perforation reduces computation by skipping some loop work, accepting a change in the result. This team project implemented two existing approaches in LLVM: skipping whole iterations and selectively skipping instructions within them. We compared execution time and numerical accuracy.

The evaluation used four small benchmarks: summation, nested loops, matrix multiplication, and convolution.

<figure class="project-figure">
  <img src="{{ '/assets/projects/loop-perforation/selective-workflow.png' | relative_url }}" width="1872" height="735" alt="Workflow diagram from the report showing analysis and transformation steps for selective loop perforation." loading="lazy">
  <figcaption>Selective loop perforation (report, Figure 1): green marks computations selected for skipping; red marks pointer and loop-control instructions that remain.</figcaption>
</figure>

Faster execution often came with substantial output error. The report evaluates both together, showing why a speedup alone is insufficient to judge an approximate compiler transformation.
