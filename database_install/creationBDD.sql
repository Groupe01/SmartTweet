CREATE TABLE IF NOT EXISTS "hashtag" (
"id_hashtag" SERIAL PRIMARY KEY NOT NULL,
"hashtag" TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS "feeling" (
"id_feeling" SERIAL PRIMARY KEY NOT NULL,
"feeling" TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS "tweet" (
"id_tweet" TEXT PRIMARY KEY NOT NULL,
"text" TEXT NOT NULL,
"date" TIMESTAMP,
"lang" TEXT,
"confidence" REAL,
"fk_hashtag_id" INTEGER REFERENCES hashtag(id_hashtag),
"fk_feeling_id" INTEGER REFERENCES feeling(id_feeling)
);

INSERT INTO feeling(feeling) VALUES
    ('positive'),
    ('neutral'),
    ('negative'),
    ('mixed');
	
CREATE OR REPLACE FUNCTION feeling_by_day(myhashtag TEXT)
RETURNS TABLE (
    hashtag TEXT,
    day DATE,
    feeling TEXT,
    nb_tweets BIGINT
)
LANGUAGE plpgsql
AS
$$
BEGIN
RETURN QUERY
    SELECT hashtag.hashtag, date(tweet.date) as day, feeling.feeling, COUNT(tweet.id_tweet)
    FROM hashtag, tweet, feeling
    WHERE tweet.fk_feeling_id = feeling.id_feeling
    AND tweet.fk_hashtag_id = hashtag.id_hashtag
    AND hashtag.hashtag = myhashtag
    GROUP BY hashtag.hashtag, day, feeling.feeling
    ORDER BY hashtag.hashtag, day, feeling.feeling
;
END;
$$

CREATE OR REPLACE FUNCTION get_feeling(
v_hashtag text)
    RETURNS TABLE(hashtag text, v_positive numeric, v_negative numeric, v_neutral numeric, v_mixed numeric)
    LANGUAGE 'plpgsql'

    
AS $BODY$
declare
v_positive numeric(5);
v_negative numeric(5);
v_neutral numeric(5);
v_mixed numeric(5);
begin
select
count(id_tweet) into v_positive
from tweet join hashtag on tweet.fk_hashtag_id = hashtag.id_hashtag
join feeling on tweet.fk_feeling_id = feeling.id_feeling
where
     hashtag.hashtag = v_hashtag and feeling.feeling ='positive';
select
count(id_tweet) into v_negative
from tweet join hashtag on tweet.fk_hashtag_id = hashtag.id_hashtag
join feeling on tweet.fk_feeling_id = feeling.id_feeling
where
     hashtag.hashtag = v_hashtag and feeling.feeling ='negative';

select
count(id_tweet) into v_neutral
from tweet join hashtag on tweet.fk_hashtag_id = hashtag.id_hashtag
join feeling on tweet.fk_feeling_id = feeling.id_feeling
where
     hashtag.hashtag = v_hashtag and feeling.feeling ='neutral';
select
count(id_tweet) into v_mixed
from tweet join hashtag on tweet.fk_hashtag_id = hashtag.id_hashtag
join feeling on tweet.fk_feeling_id = feeling.id_feeling
where
     hashtag.hashtag = v_hashtag and feeling.feeling ='mixed';

return query
select v_hashtag,
      v_positive ,
  v_negative ,
  v_neutral,
  v_mixed;
end;
$BODY$;