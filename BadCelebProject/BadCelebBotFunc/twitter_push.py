#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 17:26:39 2021

@author: robertpapel
"""

import tweepy

# Twitter connection ----
def twit_push(consumer_key, consumer_secret,
              access_token, access_token_secret,
              tweet_text, celeb_jpg):

    # authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # push
    # api.update_status(tweet_text, tweet_mode = 'extended')
    api.update_with_media(celeb_jpg, tweet_text, tweet_mode = 'extended')

# Main function ----
if __name__ == '__main__':
    twit_push()

