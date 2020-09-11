
import tweepy
import csv
import json
import os
import pandas as pd
#
# twitter creditianls
consumer_key = 'Q4ucPCmZETeOdQ1w1Yg18XYkb'
consumer_secret = 'rnRCb6Z2WN0S33UBQ51rGrWE4nGBLNNIynraNSg56imsxMhhEM'
access_token = '1301874176110866435-fgSYnNGgPo7M0xzNKVGedGgEaiGlk1'
access_token_secret = 'BBGzRRlOJQdUP4UplnIyHAliZ4kMjC158q9RnjfkIkshp'
#
# l'authentification
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#
# /Create function collect_tweets data

#
#q ='mot_cle'- 'RT'   
# 
def collect_tweets(hashtag):
    
    csvFile = open('tweets.csv', 'a') 
    csvWriter = csv.writer(csvFile)
    for Tweet in tweepy.Cursor(api.search,q = hashtag).items():
    #         print("ID", Tweet.id)
    #         print("created:", Tweet.created_at)
    #         print ("Text:", Tweet.text)
            if 'RT @' not in Tweet.text:
                csvWriter.writerow( [Tweet.id, Tweet.created_at, Tweet.text.encode('utf-8').decode("ascii", "ignore")])
    with open('tweets.csv', 'r') as file:
        datatweet_frame = pd.read_csv(file, names=["Tweet.id", "Tweet.created_at", "Tweet.text"])
    return datatweet_frame
    # Filter out unwanted data
df=collect_tweets('EnseignementSup')
#print(df.head())
#
    #
    # print(datatweet_frame.shape)
    # print(datatweet_frame.head())
#    