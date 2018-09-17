#!/usr/bin/env python
# -*- coding: utf-8 -*-
# this script
#
# Author :  Ahmed A
# Las Update: Sun Jun 10 13:32:29 +03 2018
#
from __future__ import print_function
from twitter import Twitter, OAuth, TwitterHTTPError
import os
import sys
import time
import random
import tweepy
import datetime
import MySQLdb
import json
import argparse
from newspaper import Article


# Connect to MySQL
# Update Connection details
db=MySQLdb.connect(host="localhost",database="reactapp",user="<dbuser>",password='<dbpass>',unix_socket='/var/run/mysqld/mysqld.sock', charset = 'utf8')
cursor=db.cursor()



class TwitterClient:
    def __init__(self, config_file="config.txt"):
        # this variable contains the configuration for the bot
        self.BOT_CONFIG = {}

        self.setup(config_file)

        # Used for random timers
        random.seed()


    def setup(self, config_file="config.txt"):
        """
            Reads in the bot configuration file and sets up the bot.

            Defaults to config.txt if no configuration file is specified.

            If you want to modify the bot configuration, edit your config.txt.
        """

        with open(config_file, "r") as in_file:
            for line in in_file:
                line = line.split(":")
                parameter = line[0].strip()
                value = line[1].strip()

                if parameter in ["USERS_KEEP_FOLLOWING", "USERS_KEEP_UNMUTED", "USERS_KEEP_MUTED"]:
                    if value != "":
                        self.BOT_CONFIG[parameter] = set([x for x in value.split(",")])
                    else:
                        self.BOT_CONFIG[parameter] = set()
                elif parameter in ["FOLLOW_BACKOFF_MIN_SECONDS", "FOLLOW_BACKOFF_MAX_SECONDS"]:
                    self.BOT_CONFIG[parameter] = int(value)
                else:
                    self.BOT_CONFIG[parameter] = value

        # make sure that the config file specifies all required parameters
        required_parameters = ["OAUTH_TOKEN", "OAUTH_SECRET", "CONSUMER_KEY",
                               "CONSUMER_SECRET", "TWITTER_HANDLE",
                               "ALREADY_FOLLOWED_FILE",
                               "FOLLOWERS_FILE", "FOLLOWS_FILE"]

        missing_parameters = []

        for required_parameter in required_parameters:
            if (required_parameter not in self.BOT_CONFIG or
                    self.BOT_CONFIG[required_parameter] == ""):
                missing_parameters.append(required_parameter)

        if len(missing_parameters) > 0:
            self.BOT_CONFIG = {}
            raise Exception("Please edit %s to include the following parameters: %s.\n\n"
                            "The bot cannot run unless these parameters are specified."
                            % (config_file, ", ".join(missing_parameters)))

        # make sure all of the sync files exist locally
        for sync_file in [self.BOT_CONFIG["ALREADY_FOLLOWED_FILE"],
                          self.BOT_CONFIG["FOLLOWS_FILE"],
                          self.BOT_CONFIG["FOLLOWERS_FILE"]]:
            if not os.path.isfile(sync_file):
                with open(sync_file, "w") as out_file:
                    out_file.write("")

        # check how old the follower sync files are and recommend updating them
        # if they are old
        if (time.time() - os.path.getmtime(self.BOT_CONFIG["FOLLOWS_FILE"]) > 86400 or
                time.time() - os.path.getmtime(self.BOT_CONFIG["FOLLOWERS_FILE"]) > 86400):
            print("Warning: Your Twitter follower sync files are more than a day old. "
                  "It is highly recommended that you sync them by calling sync_follows() "
                  "before continuing.", file=sys.stderr)

        # # create an authorized connection to the Twitter API
        # self.TWITTER_CONNECTION = Twitter(auth=OAuth(self.BOT_CONFIG["OAUTH_TOKEN"],
        #                                              self.BOT_CONFIG["OAUTH_SECRET"],
        #                                              self.BOT_CONFIG["CONSUMER_KEY"],
        #                                              self.BOT_CONFIG["CONSUMER_SECRET"]))
    def wait_on_action(self):
        min_time = 0
        max_time = 0
        if "FOLLOW_BACKOFF_MIN_SECONDS" in self.BOT_CONFIG:
            min_time = int(self.BOT_CONFIG["FOLLOW_BACKOFF_MIN_SECONDS"])

        if "FOLLOW_BACKOFF_MAX_SECONDS" in self.BOT_CONFIG:
            max_time = int(self.BOT_CONFIG["FOLLOW_BACKOFF_MAX_SECONDS"])

        if min_time > max_time:
            temp = min_time
            min_time = max_time
            max_time = temp

        wait_time = random.randint(min_time, max_time)

        if wait_time > 0:
            print("Choosing time between %d and %d - waiting %d seconds before action" % (min_time, max_time, wait_time))
            time.sleep(wait_time)

        return wait_time


def getArticle(link):    
    article1=Article(link)
#    try:
    article1.download()
#    except:
#        downloading = False
#    if downloading:
    article1.parse()
    title = article1.title
        
    image = article1.top_image
    url = article1.url
    return (title, image)


def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

def get_users():
    # Get the User object for twitter...
    for userId in my_bot.BOT_CONFIG['USERS_KEEP_FOLLOWING']:
        user = api.get_user(userId)
        print (user.screen_name)
        print (user.followers_count)
        for friend in user.friends():
            print (friend.screen_name)

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():

    # parse user input
    options = argparse.ArgumentParser()

    #file related args
    options.add_argument("-l", "--language",   default="ara", help="language to process (ara/eng)")
    
    options.parse_args()

    args = options.parse_args()

    print("Processing "+args.language+" ....")
    #my_bot = TwitterClient()
    my_bot = TwitterClient("config_"+args.language+".txt")

    auth = tweepy.OAuthHandler(my_bot.BOT_CONFIG["CONSUMER_KEY"], my_bot.BOT_CONFIG["CONSUMER_SECRET"])
    auth.set_access_token(my_bot.BOT_CONFIG["OAUTH_TOKEN"], my_bot.BOT_CONFIG["OAUTH_SECRET"])

    api = tweepy.API(auth)

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)

    #for follower in limit_handled(tweepy.Cursor(api.followers).items()):
    #    if follower.friends_count < 300:
    #        print follower.screen_name


    startDate = datetime.datetime(2018, 6, 7, 0, 0, 0)
    endDate =   datetime.datetime(2918, 6, 10, 0, 0, 0)


    tweets = []

    while(True):
        for username in my_bot.BOT_CONFIG['USERS_KEEP_FOLLOWING']:
            try:
                tmpTweets = api.user_timeline(username)
            except Exception:
                continue
            for tweet in tmpTweets:
                if tweet.created_at < endDate and tweet.created_at > startDate:
                    #tweets.append(tweet)
                    (twimag,twttle) = ('','')
                    if(len(json.dumps(tweet._json))>11990):
                        continue
                    #print("In0 Tweet:",tweet.__dict__['_json']['entities'])
                    try:
                        twurl = tweet.__dict__['_json']['entities']['urls'][0]['expanded_url']
                        (twttle,twimag) = getArticle(twurl)
                    except Exception as e:
                        #print("urls0-URLS:",tweet.__dict__['_json'])
                        continue
                    if(twimag==''):
                        try:
                            twimag = tweet.__dict__['_json']['entities']['media'][0]['media_url']
                            twttle = tweet.__dict__['_json']['text']
                        except Exception as e:
                            #print("media0-URLS:",tweet.__dict__['_json'])
                            continue

                    #print("TW0",twimag,' Title:',twttle)
                    #exit(0)
                    twimag = (twimag[:290]) if len(twimag) > 290 else twimag # Check the field length in the DB
                    twttle = (twttle[:490]) if len(twttle) > 490 else twttle # Check the field length in the DB
                    print("1",username,tweet.__dict__['_json']['id'],tweet.__dict__['_json']['created_at'],twttle,twimag) #,tweet._json['text']
                    cursor.execute('''INSERT into tweets_'''+args.language+''' (tweet_id, date, tweet,screen_name,title,image)
                        values (%s, %s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE tweet=values(tweet) ''',
                        (tweet.__dict__['_json']['id'], datetime.datetime.strptime(tweet.__dict__['_json']['created_at'],'%a %b %d %H:%M:%S %z %Y'),json.dumps(tweet._json).encode('utf-8'),username,twttle,twimag))
                    db.commit()
            if(len(tmpTweets)<2):
                continue
            try:

                while (tmpTweets[-1].created_at > startDate):
                    tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id)
                    for tweet in tmpTweets:
                        if tweet.created_at < endDate and tweet.created_at > startDate:
                            #tw.append(tweet)
                            if(len(json.dumps(tweet._json))>11990):
                                continue
                            #print("In1 Tweet:",tweet.__dict__['_json']['entities'])
                            try:
                                twurl = tweet.__dict__['_json']['entities']['urls'][0]['expanded_url']
                                (twttle,twimag) = getArticle(twurl)
                            except Exception as e:
                                #print("urls1-URLS:",tweet.__dict__['_json'])
                                continue
                            if(twimag==''):
                                try:
                                    twimag = tweet.__dict__['_json']['entities']['media'][0]['media_url']
                                    twttle = tweet.__dict__['_json']['text']
                                except Exception as e:
                                    #print("media1-URLS:",tweet.__dict__['_json'])
                                    continue
                            
                            #print("TW1",twimag,' Title:',twttle)
                            #exit(0)
                            twimag = (twimag[:290]) if len(twimag) > 290 else twimag # Check the field length in the DB
                            twttle = (twttle[:490]) if len(twttle) > 490 else twttle # Check the field length in the DB
                            print("2",username,tweet.__dict__['_json']['id'],tweet.__dict__['_json']['created_at'],twttle,twimag) #,tweet._json['text']
                            cursor.execute('''INSERT into tweets_'''+args.language+''' (tweet_id, date, tweet,screen_name,title,image)
                            values (%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE tweet=values(tweet) ''',
                            (tweet.__dict__['_json']['id'], datetime.datetime.strptime(tweet.__dict__['_json']['created_at'],'%a %b %d %H:%M:%S %z %Y'),json.dumps(tweet._json).encode('utf-8'),username,twttle,twimag))
                            db.commit()
            except Exception:
                continue
        #for tweet in tweets:
        #    print("Tweet:",tweet)

        stime=my_bot.wait_on_action()
        eprint("Sleep time",stime)

    db.close()
    return



if __name__ == '__main__':
    main()
