pip install -r requirements.txt

-------------------------------------
-- general info
db { host: 'dev.findmine.us',
     user: 'andrew',
     password: 'andrew',
     database: 'andrew' }

-- connect (enter password "andrew")
mysql -u andrew -p -h dev.findmine.us andrew

-- scratch & replace table
drop table if exists link_edges;
create table link_edges (
  url_from TEXT,
  url_to TEXT
);


