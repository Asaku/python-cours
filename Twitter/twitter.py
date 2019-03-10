#!/usr/bin/env python
# coding: utf-8

from requests_html import HTMLSession

url = "https://twitter.com/esd_academy"

session = HTMLSession()

r = session.get(url)

about = r.html.find('.js-tweet-text-container')

for p in about:
    print(p.text)
