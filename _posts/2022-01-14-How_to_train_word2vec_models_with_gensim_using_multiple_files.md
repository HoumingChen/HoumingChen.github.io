---
title: How to train word2vec models with gensim using multiple files
date: 2022-01-14 20:13:09 +/-2429
categories: [Blogs, Machine Learning & Data Science]
tags: [machine learning, NLP, tutorial]
pin: false
comments: false
toc: false
mermaid: false
math: false
---

<!--
    Post Name:How_to_train_word2vec_models_with_gensim_using_multiple_files
    Post File dir: /mnt/projects/site_tmp/HoumingChen.github.io/assets/post_files/How_to_train_word2vec_models_with_gensim_using_multiple_files
-->

When we are training word2vec models with gensim, sometimes we might face the trouble that our training data are in multiple files and the files are so large that we cannot load them to RAM all at once.

This can be easily fixed by defining a iterator to iterate through those files.

Here is a very short colab tutorial:
<a href = "https://colab.research.google.com/drive/1pPq0rP2zGuv9p3Qt4RHgDETowEdPckHZ"> link </a>
