import requests
from lxml import html, etree
from urlparse import urlparse

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
    return p.netloc



