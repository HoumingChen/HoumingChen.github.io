---
layout: project
title: "ICA-SeFa: Interpretable Image Controls"
order: 1
course: EECS 545 Machine Learning
period: "2021–2022"
context: Course project with subsequent independent research
independent: true
summary: Discovering interpretable editing directions in pretrained image generators using independent component analysis.
description: A course project and independent continuation on interpretable editing directions in pretrained image generators.
report: /assets/projects/ica-sefa/course-report-2021.pdf
team_label: 2021 course team
authors:
  - Houming Chen
  - Le Qin
  - Yutong Bi
  - Jiaxi Chen
  - Dongyang Zhao
---

ICA-SeFa explores how to find understandable editing controls in a pretrained image generator. Building on SeFa, it applies independent component analysis to generator weights to discover directions that change properties such as expression, hair color, and lighting, without retraining the generator.

I proposed the method and its mathematical rationale, shared the implementation, and developed a CLIP-based evaluation of intended changes and effects on other attributes. The work began in EECS 545 in 2021 and continued independently through 2022.

<figure class="project-figure">
  <img src="{{ '/assets/projects/ica-sefa/mouth-traversal.jpg' | relative_url }}" width="776" height="260" alt="Three generated portraits of the same face, with the mouth closed, partly open, and widely open.">
  <figcaption>Mouth-opening edits from Figure 1 of the 2021 course report. The middle image is the starting point; the outer images follow the same editing direction in opposite ways.</figcaption>
</figure>

This selected example illustrates a useful image control. Evaluating changes to unrelated attributes remains part of the disentanglement problem.
