import lxml
import web
import db_conn

# in memory index (for now) (ok w/ multithreads?)
links_found = set()

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

        if domain_n == domain:
            print url_str + " -> " + url_str_n + ": " + domain_n
            db_cnx.insert_link_edge(url_str, url_str_n)
            if (url_str_n not in links_found):
                crawl(url_str_n, db_cnx) # <- will go deep into 1st link, should multithread
