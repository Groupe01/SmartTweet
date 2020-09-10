import tweepy
import csv
import pandas as pd


consumer_key = 'wvmPoGr45XpkjlXnkc5XVqoTG'
consumer_secret = 'vuyFTIw16n3ZpItONp26qNVU1PAfJ9HvKAMy9uhRFWBkfCoNWY'
access_token = '1301583918056050688-GfRQOc1N6OroeuMAfEHQbLN96Y89CB'
access_token_secret = 'sS65Y8W0iA1fmODF0YODm2Q8ohLnYuiDYQcZM6sBQ2bPi'



def get_hashtag_tweets (csv_file, hash_tag):    
    """
    """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    csvfile = open(csv_file, 'a')
    csvwriter = csv.writer(csvfile)

    for tweet in tweepy.Cursor(api.search,q= hash_tag).items():
        if 'RT @' not in  tweet.text:
            csvwriter.writerow([tweet.id_str,tweet.created_at, tweet.text.encode('utf-8').decode("ascii","ignore")])

get_hashtag_tweets('tweets.csv',"#GalaxyZFold2")

    


# tweets = api.home_timeline()
# for tweet in tweets:
#     print(tweet.text)

# user = api.get_user('@mohamed_el_arbi')
# print(user.screen_name)
# print(user.followers_count)
# for friend in user.friends():
#     print(friend.screen_name)



