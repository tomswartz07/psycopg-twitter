#!/usr/bin/env python
"Download all user tweets into csv"
# encoding: utf-8

import csv
import tweepy #https://github.com/tweepy/tweepy

#Twitter API credentials
consumer_key = "supersecret"
consumer_secret = "supersecret"
access_key = "supersecret"
access_secret = "supersecret"


def get_all_tweets(screen_name):
    "Twitter only allows access to a users most recent 3240 tweets with this method"

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []

    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.favorites(screen_name=screen_name, count=200)

    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        #print("getting tweets before %s" % (oldest))

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.favorites(screen_name=screen_name, count=200, max_id=oldest)

        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        #print("...%s tweets downloaded so far" % (len(alltweets)))
    print("Processing %s tweets" % (len(alltweets)))

    #transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.id_str, tweet.created_at, tweet.user.screen_name, tweet.user.name,
                  tweet.text.encode("utf-8")] for tweet in alltweets]

    #write the csv
    with open('/home/tom/git/python-twitter/%s_favorite_tweets.csv' % screen_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "user", "name", "text"])
        writer.writerows(outtweets)
    pass


if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("supersecret")
