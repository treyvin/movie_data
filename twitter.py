#print(sys.path)
# sys.path.append('/home/trey/.local/bin')
# sys.path.append('/home/trey/.local/lib')
# sys.path.append('/home/trey/.local')
# sys.path.append('/home/trey/market_data_infra')

import sys
import os
import config
import tweepy

def auth():
    key = None
    secret = None
    print(tweepy.__file__)
    auth = tweepy.OAuthHandler(config.twitter_api_key, config.twitter_api_secret)
    auth.set_access_token(key, secret)
    api = tweepy.API(auth)  
    return api

def get_tweets(query, api):
    for tweet in tweepy.Cursor(api.search_tweets, q=query, lang='en').items(10):
        print(tweet.text)

if __name__ == '__main__':
    api = auth()
    get_tweets('Dune', api)
