import sys
import crawl
import db_conn

"""
    Crawl a webpage's links within its domain
    Usage:
        python main "http://www.example.com"

    Terminates on completion or keyboard interrupt
"""
def main(argv=None):
    try:
        db_cnx = db_conn.db_conn()
        url = sys.argv[1]

        crawl.crawl(url, db_cnx)

        db_cnx.close()
    except IndexError:
        print "Please run with a url (ex. \"python main.py http://www.example.com\")"
    except KeyboardInterrupt:
        print "Stopped crawling on interrupt."
        db_cnx.close()

if __name__ == "__main__":
    sys.exit(main())
