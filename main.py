from back import searchtweet as ST
from back import azure_sentiment_analysis as ASA

df_result = ST.tweet_search('ps5')

client = ASA.authenticate_client()

df_final = ASA.sentiment_analysis(client, df_result)

