use newsright


CREATE TABLE IF NOT EXISTS half_life_count
(
storykey int,
count int,
half_life float,
PRIMARY KEY (storykey)
);

CREATE TABLE IF NOT EXISTS zipcodes
(
storykey int,
zipcode VARCHAR(16) 
);

CREATE TABLE IF NOT EXISTS categories
(
storykey int,
category varchar(64)
);

CREATE TABLE IF NOT EXISTS story_info
(
storykey int,
website varchar(64),
creator varchar(64)
);

-- RUN 1
/*
LOAD DATA INFILE '/home/ubuntu/newsright/halflifedata/halflifeinfo_run1.txt'
INTO TABLE half_life_count
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n';

LOAD DATA INFILE '/home/ubuntu/newsright/halflifedata/zips_run1.txt'
INTO TABLE zipcodes
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n';

LOAD DATA INFILE '/home/ubuntu/newsright/halflifedata/story_category_run1.csv'
INTO TABLE categories
FIELDS TERMINATED BY '|'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n';

LOAD DATA INFILE '/home/ubuntu/newsright/halflifedata/storyinfo_run1.csv'
INTO TABLE story_info 
FIELDS TERMINATED BY '|'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;
*/

-- RUN 2
/*
LOAD DATA INFILE '/home/ubuntu/newsright/halflifedata/halflifeinfo_run2.txt'
INTO TABLE half_life_count
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n';

LOAD DATA INFILE '/home/ubuntu/newsright/halflifedata/zips_run2.txt'
INTO TABLE zipcodes
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n';

LOAD DATA INFILE '/home/ubuntu/newsright/halflifedata/story_category_run2.csv'
INTO TABLE categories
FIELDS TERMINATED BY '|'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE '/home/ubuntu/newsright/halflifedata/storyinfo_run2.csv'
INTO TABLE story_info 
FIELDS TERMINATED BY '|'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;
*/
