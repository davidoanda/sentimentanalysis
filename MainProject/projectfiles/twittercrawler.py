import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'K709NnBB1ZNxI0HASOkxb8vfI'
consumer_secret = '7pVoyn4fMnbgJP0QDPeGo2aj1719D1bOogBWfuAurjNNl8E4MT'
access_token = '1036999904877531136-1dN8kpEgNWt2uJqSU2cCTppIn8YKnC'
access_token_secret = 'deUKZNORxOyc7M4ibXUkcQdEKObzRHICzVG58CtqHOZQr'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
with open('crawledtweets.csv', mode='w', encoding='utf-8') as csvFile:
    #Use csv Writer
    csvWriter = csv.writer(csvFile,lineterminator = '\n')

    csvWriter.writerow(['ID', 'Date', 'Text', 'Username', 'Location'])
    for tweet in tweepy.Cursor(api.search,q="buhari",
                               lang="en", tweet_mode='extended',
                               since="2018-12-25").items(1000):
        if 'retweeted_status' not in dir(tweet):
            csvWriter.writerow([tweet.id, tweet.created_at, tweet.full_text, tweet.user.screen_name, tweet.user.location])      
        #else:
        #print (tweet.created_at, tweet.text)
            #csvWriter.writerow([tweet.created_at, tweet.full_text.encode('utf-8'), tweet.user.screen_name])