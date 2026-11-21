#!/usr/bin/env python3
"""Refresh the website's PDF and readable CV from the main DB resume only."""
from html import escape
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
from xml.etree import ElementTree as ET
from zipfile import ZipFile
import hashlib
import shutil

SITE = Path(__file__).resolve().parents[1]
SOURCE = SITE.parent / 'resume/drafts/research-internship/DB/resume.docx'
PDF = SOURCE.with_suffix('.pdf')
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'

def local_url(url):
    parsed = urlsplit(url)
    if parsed.hostname == 'houmingchen.github.io':
        return urlunsplit(('', '', parsed.path or '/', parsed.query, parsed.fragment))
    return url

def run_html(run):
    content = ''.join(escape(t.text or '') for t in run.iter(W+'t'))
    if not content:
        return ''
    props = run.find(W+'rPr')
    if props is not None:
        for tag, html in [('i', 'em'), ('b', 'strong')]:
            flag = props.find(W+tag)
            if flag is not None and flag.get(W+'val') not in ('0', 'false', 'off'):
                content = f'<{html}>{content}</{html}>'
    return content

def inline_html(paragraph, links):
    columns = ['']
    for child in paragraph:
        if child.tag == W+'r':
            if child.find(W+'tab') is not None:
                columns.append('')
            columns[-1] += run_html(child)
        elif child.tag == W+'hyperlink':
            label = ''.join(run_html(r) for r in child.findall(W+'r'))
            url = links[child.get(R+'id')]
            columns[-1] += f'<a href="{escape(local_url(url), quote=True)}">{label}</a>'
    if len(columns) == 1:
        return columns[0]
    return '<span>'+columns[0]+'</span><span class="cv-row-detail">'+''.join(columns[1:])+'</span>'

def main():
    if not SOURCE.is_file() or not PDF.is_file():
        raise SystemExit('Export the main DB resume DOCX/PDF before synchronizing the website.')
    with ZipFile(SOURCE) as archive:
        document = ET.fromstring(archive.read('word/document.xml'))
        relationships = ET.fromstring(archive.read('word/_rels/document.xml.rels'))
    links = {r.get('Id'): r.get('Target') for r in relationships if r.get('Type', '').endswith('/hyperlink')}
    paragraphs = document.find(W+'body').findall(W+'p')
    lines = ['<!-- Generated from the main DB resume by tools/sync_resume.py. Edit the DOCX, then regenerate. -->', '<div class="cv-content">']
    section_open = False
    list_open = False
    for index, paragraph in enumerate(paragraphs):
        text = ''.join(t.text or '' for t in paragraph.iter(W+'t'))
        if index == 0 or text == 'RESEARCH (CONTINUED)':
            continue  # The page header owns the name; a continuous web view needs no page-break heading.
        props = paragraph.find(W+'pPr')
        style_node = props.find(W+'pStyle') if props is not None else None
        style = style_node.get(W+'val') if style_node is not None else ''
        bullet = props is not None and props.find(W+'numPr') is not None
        if list_open and not bullet:
            lines.append('</ul>')
            list_open = False
        content = inline_html(paragraph, links)
        has_tab = any(r.find(W+'tab') is not None for r in paragraph.findall(W+'r'))
        if style == 'CVSection':
            if section_open:
                lines.append('</section>')
            slug = 'cv-'+'-'.join(text.lower().split())
            lines.append(f'<section aria-labelledby="{slug}"><h2 id="{slug}">{escape(text.title())}</h2>')
            section_open = True
        elif bullet:
            if not list_open:
                lines.append('<ul class="cv-contributions">')
                list_open = True
            lines.append(f'<li>{content}</li>')
        elif style in ('CVProject', 'CVSchool'):
            classes = 'cv-project' + (' cv-row' if has_tab else '')
            lines.append(f'<h3 class="{classes}">{content}</h3>')
        else:
            classes = []
            if has_tab: classes.append('cv-row')
            if style == 'CVCitation': classes.append('cv-citation')
            if style == 'CVAffiliation': classes.append('cv-appointment')
            if index == 1: classes.append('cv-contact')
            if index == 2: classes.append('cv-interests')
            attr = f' class="{" ".join(classes)}"' if classes else ''
            lines.append(f'<p{attr}>{content}</p>')
    if list_open: lines.append('</ul>')
    if section_open: lines.append('</section>')
    lines.append('</div>')
    output = SITE/'_includes/resume-content.html'
    output.write_text('\n'.join(lines)+'\n', encoding='utf-8')
    target = SITE/'assets/pdf/Houming_Chen_CV.pdf'
    shutil.copyfile(PDF, target)
    print('Synchronized the main DB resume: readable HTML and PDF.')
    print('PDF SHA-256:', hashlib.sha256(target.read_bytes()).hexdigest())

if __name__ == '__main__':
    main()
