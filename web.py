import requests
from lxml import html, etree
from urlparse import urlparse
import re

# string -> etree
def getHtml(url_str):
    s = getHtmlText(url_str)
    return html.fromstring(s)

# string -> string
def getHtmlText(url_str):
    r = requests.get(url_str)
    #todo: check type (url header?)
    return r.text

# etree -> io(string)
def printHtml(html):
    result = etree.tostring(html, pretty_print=True, method='html')
    print result

# string -> string
def domain(url_str):
    try:
        p = urlparse(url_str)
        pure_domain_list = p.hostname.split('.')[-2:] #only last 2 sections of domain matter
        return '.'.join(pure_domain_list)
    except:
        return ''

def domain_eq(d1, d2):
    if d2 is '' or d1 is '':
        return True

    return d1 == d2

