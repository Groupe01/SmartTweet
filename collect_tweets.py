
import tweepy
import csv
import json
import os
#
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
# Open/Create a file to append data
with open('tweets.csv', 'w') as csvFile:
    for Tweet in tweepy.Cursor(api.search,q="#EnseignementSup",count=20,\
                           since_id=None).items():
        print("ID", Tweet.id)
        print("created:", Tweet.created_at)
        print ("Text:", Tweet.text)
        csvFile.write( str(Tweet.id) + ';' + Tweet.created_at + ';' + Tweet.text + '\n')
    #
   # with open('tweets.csv', 'w') as csvFile:

   # csvWriter.writerow([Tweet.created_at, Tweet.text.encode('utf-8')])