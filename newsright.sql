use newsright

CREATE TABLE IF NOT EXISTS half_life_count
(
storykey int,
count int,
half_life float,
PRIMARY KEY (storykey)
);

LOAD DATA INFILE '/home/ubuntu/newsright/halflifedata/halflifeinfo_run1.txt'
INTO TABLE half_life_count
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n';


CREATE TABLE IF NOT EXISTS zipcodes
(
storykey int,
zipcode int
);

LOAD DATA INFILE '/home/ubuntu/newsright/halflifedata/zips_run1.txt'
INTO TABLE zipcodes
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n';

CREATE TABLE IF NOT EXISTS categories
(
storykey int,
category varchar(64)
);

LOAD DATA INFILE '/home/ubuntu/newsright/halflifedata/story_category_run1.csv'
INTO TABLE categories
FIELDS TERMINATED BY '|'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n';


