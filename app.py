import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob


class TwitterClient(object):
    """ 
	Generic Twitter Class for sentiment analysis. 
	"""

    def __init__(self):
        """ 
		Class constructor or initialization method. 
		"""
        # keys and tokens from the Twitter Dev Console
        consumer_key = "o74hsg2mOi4M7YWN3NloQf6W8"
        consumer_secret = "8biZKnNd9MO0Ds5eCxpDrEB72z9GFwrXmx1LnQBibxu7Fd7RDz"
        access_token = "4694554466-Z5w860QTkrlfLx4xoXKBfbjD3jMridxEgKwFZ9y"
        access_token_secret = "O7f2aJ1ZWV1lzfJy000AQJTvWoc8vEViqezUGMQJv5iSq"

        # attempt authentication
        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):

        """ 
            Utility function to clean tweet text by removing links, special characters 
            using simple regex statements. 
            """
        return " ".join(
            re.sub(
                "(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet
            ).split()
        )

    def get_tweet_sentiment(self, tweet):
        """ 
		Utility function to classify sentiment of passed tweet 
		using textblob's sentiment method 
		"""

        analysis = TextBlob(self.clean_tweet(tweet))
        if analysis.sentiment.polarity > 0:
            return "positive"
        elif analysis.sentiment.polarity == 0:
            return "neutral"
        else:
            return "negative"

    def get_tweets(self, query, count=10):
        """ 
		Main function to fetch tweets and parse them. 
		"""
        tweets = []

        try:
            fetched_tweets = self.api.search(q=query, count=count)

            for tweet in fetched_tweets:
                parsed_tweet = {}
                parsed_tweet["text"] = tweet.text
                parsed_tweet["sentiment"] = self.get_tweet_sentiment(tweet.text)

                if tweet.retweet_count > 0:
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))
