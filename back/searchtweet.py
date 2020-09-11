import requests
import pandas as pd
import json

def tweet_search(hashtag):
  '''
    This function allows you to retrieve the tweets of the last week according to a chosen hashtag. 
  '''
  bearertoken = 'AAAAAAAAAAAAAAAAAAAAAOuOHQEAAAAAdCYvOyCRPFuDaYlZisar99fsn54%3D1fYrjnxRipezCSHCme16XF2AySm2tdTliwEH0hcRb016C01KvN'
  hashtag = '%23'+hashtag+' -RT'

  url = f"https://api.twitter.com/2/tweets/search/recent?max_results=100&query={hashtag}&tweet.fields=created_at,lang"

  payload = {}
  headers = {'Authorization': f'Bearer {bearertoken}',}

  response = requests.request("GET", url, headers=headers, data = payload).json()
  df = pd.json_normalize(response['data']).set_index('id')

  while 'next_token' in response['meta'].keys() and len(df)<5000 :
    next_token = response['meta']['next_token']
    url = f"https://api.twitter.com/2/tweets/search/recent?max_results=100&next_token={next_token}&query={hashtag}"
    response = requests.request("GET", url, headers=headers, data = payload).json()
    nextdf = pd.json_normalize(response['data']).set_index('id')
    df = pd.concat([df,nextdf])

  return df

# df = tweet_search('ps5')
# print (df.head)
# print (df.shape)





