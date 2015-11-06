import requests
from lxml import html, etree
from urlparse import urlparse
import re

""" Get the html as a tree from a url """
def getHtml(url_str):
    s = _getHtmlText(url_str)
    return html.fromstring(s)

""" Get the html as a string from a url (internal use only) """
def _getHtmlText(url_str):
    r = requests.get(url_str)
    #todo: check type? (url header?)
    return r.text

""" Pretty print an html tree (not used, test purpose only) """
def printHtml(html):
    result = etree.tostring(html, pretty_print=True, method='html')
    print result

""" 
    Get the domain from a url string
    Returns:
        only the last two subparts of the hostname, OR
        an empty string, if the url has no domain
    Note: urls w/o hostnames include images, other sources
"""
def domain(url_str):
    try:
        p = urlparse(url_str)
        pure_domain_list = p.hostname.split('.')[-2:] #only last 2 sections of domain matter
        return '.'.join(pure_domain_list)
    except:
        return ''

"""
    Check if one domain name is within another
    Arguments:
        d1 -- the outer domain as a string
        d2 -- the inner domain as a string
    Note: if the inner domain is empty string, then it is w/in the outer domain
          if the outer domain is empty string, something is wrong

    todo: catch exception if d1 is empty string
"""

def domain_eq(d1, d2):
    if d2 is '' or d1 is '':
        return True

    return d1 == d2

