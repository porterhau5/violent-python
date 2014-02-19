#!/usr/bin/python
# -*- coding: utf-8 -*-
import mechanize


def testProxy(url, proxy):
    browser = mechanize.Browser()
    browser.set_proxies(proxy)
    page = browser.open(url)
    source_code = page.read()
    print source_code


url = 'http://ip.nefsc.noaa.gov/'
# Proxy found by using: http://www.hidemyass.com
# List maintained: http://rmccurdy.com/scripts/proxy/good.txt
hideMeProxy = {'http': '201.221.132.22:8080'}

testProxy(url, hideMeProxy)
