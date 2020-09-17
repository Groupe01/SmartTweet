from back import searchtweet as ST
from back import azure_sentiment_analysis as ASA
from back import database as db

HASHTAG = input("Quel produit voulez vous tester? (ne pas insérer le caractère #) : ")

df_result = ST.tweet_search(HASHTAG)

client = ASA.authenticate_client()

df_final = ASA.sentiment_analysis(client, df_result)

db.insert(df_final, HASHTAG)