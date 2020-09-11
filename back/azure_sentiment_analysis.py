"""Sentiment analysis
"""
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


def authenticate_client():
    """This function logs the user on Azure's API
    """
    ENDPOINT = "https://cs-groupe-un.cognitiveservices.azure.com/"
    KEY = "7b3d4c450fd84d3485f41b09087d5038"
    
    ta_credential = AzureKeyCredential(KEY)
    text_analytics_client = TextAnalyticsClient(
            endpoint=ENDPOINT, credential=ta_credential)
    print("Azure authentification successful.")
    return text_analytics_client

def sentiment_analysis(client, df):
    """This function analyses the sentiments of the tweets present in the DataFrame
    """
    for i in range(len(df)):
        df['result'] = "waiting"
        df['confidence'] = 0
        text = df["text"][i]
        documents = [text]
        response = client.analyze_sentiment(documents = documents)[0]
        df["result"][i] = response.sentiment
        liste_result = [response.confidence_scores.positive,
                        response.confidence_scores.neutral,
                        response.confidence_scores.negative]
        df["confidence"][i] = max(liste_result)
        if i % 500 == 0:
            print(f"{i} tweets analysed.")

    print("Analysis ending.")

    return df

