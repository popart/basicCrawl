pip install -r requirements.txt

-------------------------------------
db { host: 'dev.findmine.us',
     user: 'andrew',
     password: 'andrew',
     database: 'links' }

mysql -u andrew -p -h dev.findmine.us andrew
# enter password "andrew"

-- scratch old
drop table if exists link_edges;
create table link_edges (
  url_from TEXT,
  url_to TEXT
);


