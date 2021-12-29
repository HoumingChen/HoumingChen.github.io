---
title: How to find a math problem whose answer is a specific value?
date: 2021-12-28 17:03:20 +/-8538
categories: [Blogs, Math]
tags: [math, somthing fun]
pin: false
comments: false
toc: false
mermaid: false
math: true
---

*I'm writing a short blog to see if math formulas could be show correctly.*

### Intro
Tomorrow is 12/29. It would be cool if I can come up with some math questions whose answers are 1229.

A more general problem would be: given an integer \\(x\\), how can we find an interesting math question whose answer is exactly \\(x\\). 

<br>

### What questions are interesting?
It is very easy to construct a simple question whose answer is 1229. For example 
\\[\text{What is the value of } 723 + 506 \text{?}\\]

However, this question is not interesting enough, It is *easy*, since it can be solved by simple calculation. It is also *not elegant*, because there are two strange numbers "726" and "506" which seems coming from nowhere.

However, could we find some questions which are more interesting?

How about this:
\\[\text{How many prime numbers are less than } 10000 \text{?}\\]

This question cannot be solved instantly, and there are not any strange numbers or formulas in the question.

You might find it surprising that the answer of this question is indeed 1229. You can check this by this one-line python code.

```python
>>> len([num for num in range(2, 10000) if all(num % i for i in range(2, num))])
1229
```

<br>

### How could we find those interesting questions?

This is the key part of this blog.

The trick is to use a website called <a href="https://oeis.org/"> The On-Line Encyclopedia of Integer Sequences</a>, or simply <a href="https://oeis.org/">OEIS</a>

This is a website which stores many integer sequences. It also allows you to search for interesting sequences with a given number or some given numbers. 

![img](oeis.png)