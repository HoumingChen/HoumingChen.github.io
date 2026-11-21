---
layout: project
title: Evaluating LLMs on Distributed-System Specifications
order: 3
course: EECS 591 Distributed Systems
period: Fall 2023
context: Team course project
summary: Testing whether LLMs can recognize distributed protocols and explain logical errors in TLA+ specifications.
description: A distributed systems course project evaluating LLM understanding of TLA+ and explanations of protocol bugs.
report: /assets/projects/llms-distributed-systems/course-report-2023.pdf
authors:
  - Houming Chen
  - Daniel Hou
  - Oh Jun Kweon
---

This team project evaluated LLM understanding of TLA+, a language for specifying how systems behave. We tested protocol recognition after removing name clues, and the detection and explanation of logical errors in two-phase commit, Paxos, and Raft specifications.

The team reviewed 440 responses from GPT-3.5, GPT-4, PaLM, and Llama-2. The evaluation distinguished flagging a bug from correctly explaining it.

<figure class="project-result">
  <table>
    <caption>Llama-2: identifying a bug versus explaining it</caption>
    <thead><tr><th scope="col">Response</th><th scope="col">Trials</th></tr></thead>
    <tbody>
      <tr><th scope="row">Flagged the specification as incorrect</th><td>79 / 80</td></tr>
      <tr><th scope="row">Included an accepted bug explanation</th><td>15 / 80</td></tr>
    </tbody>
  </table>
  <figcaption>2023 results for two-phase commit and Paxos: ten buggy specifications each, tested four times, with manual grading (Tables 4–5).</figcaption>
</figure>

Flagging a problem did not reliably mean explaining it. All inputs in this comparison contained bugs, so these counts measure responses to buggy specifications, not overall detector accuracy or formal verification.
