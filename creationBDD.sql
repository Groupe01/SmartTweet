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