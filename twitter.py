#print(sys.path)
# sys.path.append('/home/trey/.local/bin')
# sys.path.append('/home/trey/.local/lib')
# sys.path.append('/home/trey/.local')
# sys.path.append('/home/trey/market_data_infra')

import sys
import os
import config
import tweepy
import pandas as pd
from textblob import TextBlob


def auth():
    key = None
    secret = None
    print(tweepy.__file__)
    auth = tweepy.OAuthHandler(config.twitter_api_key, config.twitter_api_secret)
    auth.set_access_token(key, secret)
    api = tweepy.API(auth)  
    return api

def get_tweets(query, api):
    rlist = []
    for tweet in tweepy.Cursor(api.search_tweets, q=query, lang='en').items(10):
        rlist.append(tweet.text)

    return rlist

def load_train_data():
    cols=['target','ids','date','flag','user','text']
    encoding = "ISO-8859-1"
    df = pd.read_csv('/home/trey/movie_data/data/training/training.1600000.processed.noemoticon.csv', encoding=encoding, names=cols)

    return df

def data_prep(tweets):
    data = []

    for x in tweets:
        lem_words = []
        t = TextBlob(x.lower())
        words = t.words
        sen = t.sentiment.subjectivity
        pol = t.sentiment.polarity
        for word in words:
            lem_words.append(word.lemmatize())
        data.append([x, pol, sen, words, lem_words])

    df = pd.DataFrame(data, columns = ['tweet', 'polarity', 'subjectivity', 'words', 'lem_words'])
    
    return df

if __name__ == '__main__':
    api = auth()
    tweets = get_tweets('Dune', api)
    df = data_prep(tweets)
    print(df)