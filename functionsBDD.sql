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