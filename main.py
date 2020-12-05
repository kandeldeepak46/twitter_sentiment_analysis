from app import TwitterClient


def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    tweets = api.get_tweets(query="programming", count=200)
    ptweets = [tweet for tweet in tweets if tweet["sentiment"] == "positive"]
    print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))
    ntweets = [tweet for tweet in tweets if tweet["sentiment"] == "negative"]
    print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))
    print(
        "Neutral tweets percentage: {}".format(
            100 * (len(tweets) - (len(ntweets) + len(ptweets))) / len(tweets)
        )
    )

    # printing first 5 positive tweets
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
        print(tweet["text"])

    # printing first 5 negative tweets
    print("\n\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet["text"])


if __name__ == "__main__":
    # calling main function
    main()
