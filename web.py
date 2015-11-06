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
    p = urlparse(url_str)
    return p.hostname

def domain_eq(d1, d2):
    if d2 is None or d1 is None:
        return True

    d1 = re.sub(r'^www.', '', d1)
    d2 = re.sub(r'^www.', '', d2)
    return d1 == d2

