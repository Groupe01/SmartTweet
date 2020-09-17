# SmartTweet

## Informations générales 
Le but de ce projet est d'analyser le contenu de tweets et de les classer selon le sentiment qu'ils renvoient. Ensuite, ces résultats seront affichés dans une page web.

## Prérequis
- Copiez le contenu du repository sur votre ordinateur
- Installer Python3 ainsi que les librairies présentes dans le fichier requirements.txt
- Une instance de ElephantSQL

## Installation
- Pour créer la base de données, rendez vous dans le browser d'Elephant SQL et entrez les commandes suivantes :
```SQL
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
```
- Ensuite, pour créer les fonctions, éxécutez les commandes suivantes :
```SQL
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
```

- Pour charger vos différents produits dans la base de données, éxécutez le fichier main.py autant de fois qu'il y a de produits à tester. La base de données fournie est préchargée avec les produits PS5, XBOXSERIESX, Iphone11 et GalaxyZFold2.

\\ lancement du serveur back et front

## Utilisation
Il vous suffit de vous rendre sur la page **__inserer l'url__**.
Pour voir le résultat des différentes analyses, il suffit de cliquer sur le bouton contenant le nom du produit choisi une première fois afin de demander les résultats. Ensuite, appuyez sur ce bouton une deuxième fois afin d'afficher les graphiques.


