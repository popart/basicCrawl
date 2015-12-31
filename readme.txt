python 2.7

-------------------------------------
pip install -r requirements.txt

-------------------------------------
-- general db info
db { host: '...',
     user: '...',
     password: '...',
     database: '...' }

-- connect (enter password "andrew")
mysql -u $USER -p -h $HOST $DB

-- scratch & replace table
drop table if exists link_edges;
create table link_edges (
  url_from TEXT,
  url_to TEXT
);


