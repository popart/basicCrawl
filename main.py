import sys
import crawl
import db_conn

def main(argv=None):
    try:
        db_cnx = db_conn.db_conn()
        url = sys.argv[1]

        crawl.crawl(url, db_cnx)

        db_cnx.close()
    except IndexError:
        print "Please run with a url (ex. \"python main.py http://www.example.com\")"

if __name__ == "__main__":
    sys.exit(main())
