import lxml
import web
import db_conn

""" 
    In memory index to prevent crawling duplicates 
    (Could be replaced or augmented with the db)
"""
links_found = set()

"""
    Crawl a web domain recursively
    Inserts associative links (url_from, url_to) for url links in each page into a db

    Arguments:
    url_str -- the url to be crawled from
    db_cnx  -- the db connection to write to

    todo: make this iterative (using a while loop) 
          (but maybe python can optimize on its own, since it's tail-recursive)
    todo: multithread the recursive calls to the links, using first-in-time calls
          (recommend using asyncio)
"""
def crawl(url_str, db_cnx):
    links_found.add(url_str)
    domain = web.domain(url_str)
    try:
        html = web.getHtml(url_str)
        links = html.iterlinks()
    except:
        links = []

    for link in links:
        _, _, url_str_n, _ = link
        domain_n = web.domain(url_str_n)

        if web.domain_eq(domain_n, domain):
            # print url_str + " -> " + url_str_n
            db_cnx.insert_link_edge(url_str, url_str_n)
            if (url_str_n not in links_found):
                crawl(url_str_n, db_cnx) # <- may go deep into 1st link, should multithread
