#!/bin/bash
bundle exec jekyll build
git add -A
git commit -m 'update'
git push
cp -r _site ..
git checkout gh-pages
