# Load Library  for the code 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Key and endpoint Azure Text Analytics API service
key = '7b3d4c450fd84d3485f41b09087d5038'
endpoint ='https://cs-groupe-un.cognitiveservices.azure.com/'

#Authenticate Client
def authenticate_client ():
    """
    Create a function to instantiate the TextAnalyticsClient object with your key AND endpoint. Then create a new client.
    Créer une fonction pour instancier un objet TextanalyticsClient avec la clé API Azure.
    """
    cl_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(endpoint, cl_credential)
    return text_analytics_client
client = authenticate_client()

# Sentiment Analysis:
def comments_sentiment_analysis(client, file):
    """
    """
    tweets_df = pd.read_csv(file,  names=["id_tweet", "date_tweet", "tweet", "sentiment","indice_confiance"])

    # senti_results = {'Positive':0,'Neutral':0,'Negative':0,'Unknown':0}
    for i in range(len(tweets_df)):
        documents = tweets_df['tweet'][i]
        comment_list =[documents]
        response = client.analyze_sentiment(documents = comment_list)[0]
        tweets_df['sentiment'][i] = response.sentiment
        indice_list=[response.confidence_scores.positive,response.confidence_scores.neutral,response.confidence_scores.negative]
        tweets_df['indice_confiance'][i]= max(indice_list)

        
        # if response == "positive":
        #     senti_results['Positive'] += 1 
        # elif response == "neutral":
        #     senti_results['Neutral'] += 1
        # elif response == "negative":
        #     senti_results['Negative'] += 1
        # else: 
        #     senti_results['Unknown'] +=1
    return tweets_df
      
df_tweet_final= comments_sentiment_analysis(client, "tweets.csv")
# df_tweet_final.to_csv('tweets_analysis.csv')
print(df_tweet_final)