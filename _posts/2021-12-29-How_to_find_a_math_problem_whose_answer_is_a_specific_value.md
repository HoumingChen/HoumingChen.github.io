---
title: How to find a math problem whose answer is a specific value 
date: 2021-12-29 00:03:47 +/-0357
categories: [Blogs, Math]
tags: [math, somthing fun]
pin: false
comments: false
toc: false
mermaid: false
math: true
---

<!-- 
    Post Name:How_to_find_a_math_problem_whose_answer_is_a_specific_value
    Post File dir: /mnt/projects/site_tmp/HoumingChen.github.io/assets/post_files/How_to_find_a_math_problem_whose_answer_is_a_specific_value
-->


*I'm writing a short blog to see if math formulas could be show correctly.*

### Intro
Today is 12/29 (Dec 29th). It would be cool if I can come up with some math questions whose answers are 1229.

A more general problem would be: given an integer \\(x\\), how can we find an interesting math question whose answer is exactly \\(x\\). 

<br>

### What questions are interesting?
It is very easy to construct a simple question whose answer is 1229. For example:
\\[\text{What is the value of } 723 + 506 \text{?}\\]

However, this question is not interesting enough, It is *easy*, since it can be solved by simple calculation. It is also *not elegant*, because there are two strange numbers "726" and "506" which seems coming from nowhere.

However, could we find some questions which are more interesting?

How about this:
\\[\text{How many prime numbers are less than } 10000 \text{?}\\]

This question is interesting. It cannot be solved instantly, and it doesn't contain any strange numbers or formulas in the question.

You might find it surprising that the answer of this question is indeed 1229. You can check this by this one-line python code.

```python
>>> len([num for num in range(2, 10000) if all(num % i for i in range(2, num))])
1229
```

<br>

### How could we find those interesting questions?

How did I find such a question whose answer is exactly 1229? This is the key part of this blog. The trick is to use a website called <a href="https://oeis.org/"> The On-Line Encyclopedia of Integer Sequences</a>, or simply <a href="https://oeis.org/">OEIS</a>

This website stores many integer sequences. It also allows you to search for interesting sequences which contains a given number. 

<img src="../../assets/post_files/How_to_find_a_math_problem_whose_answer_is_a_specific_value/OEIS.png" width="80%">

Here we use OEIS to search for sequences that contains "1229".

<img src="../../assets/post_files/How_to_find_a_math_problem_whose_answer_is_a_specific_value/Search_result.png" width="60%">

Among the results, we notice that this <a href="https://oeis.org/A006880">A006880</a> might bring us an interesting question whose answer is 1229. According to the website, <a href="https://oeis.org/A006880">A006880</a> is "Number of primes < 10^n." That is, there are exactly 1229 prime numbers which are less than \\(10^4\\). Therefore, we can easily construct the question: 
\\[\text{How many prime numbers are less than } 10000 \text{?}\\]\
And the answer of this question is 1229.

<br>
Using this method, we can also constuct questions like:

\\[\text{What is the number of disconnected graphs with 8 nodes? }\\] 
<center>(<a href="https://oeis.org/A000719">A000719</a>)</center>

<br>

\\[\text{What is the number of strict integer partitions of 59 with no adjacent parts having quotient} \geq 2 \text{?}\\] 
<center>(<a href="https://oeis.org/A342097">A342097</a>)</center>
