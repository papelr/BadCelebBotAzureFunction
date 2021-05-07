# Libraries ----
import random_name_gen_bot
import name_twit_handle_select as dc
import celeb_pic_scrape
import slack_notifications
import twitter_push
import remove_jpgs
from all_keys import consumer_key, consumer_secret, access_token, access_token_secret
#import azure.functions as func
#from azure.identity import DefaultAzureCredential, ClientSecretCredential
#import datetime
#import logging


# TO-DO: notification & error handling, cloud deployment, timer (3x/day)
# WELL, probably have to re-up in an Azure function...
# For that medium article:
    # 1) copy docker file (and modify)
    # 2) fix chromedriver path in scrape function
    # 3) add libraries from init.py, but switch namee to main.py in function.json
        # a. Redo the timer/scraper script -> sep. timer function
        # b. make sure libraries are positioned correctly (no need for sep folder!)
    # 4) add in that hostfile.json
    # 5) add stuff to requirements.txt from site

# Setting up Azure Function timer ----
# def main(mytimer: func.TimerRequest) -> None:
#     utc_timestamp = datetime.datetime.utcnow().replace(
#         tzinfo=datetime.timezone.utc).isoformat()

#     if mytimer.past_due:
#         logging.info('The timer is past due!')

#     logging.info('Python timer trigger function ran at %s', utc_timestamp)


        # Class instantiation for the handling celeb name/twitter username ----
name_handle_instance = dc.NameHandle()


        # Call random name generator script ----
random_gen = random_name_gen_bot.name_gen()


        # Pull in randomly choosen celeb name and twitter handle + sentence ----
celeb_tweet = name_handle_instance.name_and_handle(random_gen)
print(celeb_tweet)


        # Use the name_insurance function in the scraping script ----
plain_name = name_handle_instance.name_insurance()
print(plain_name)


        # Attach photo of the random celeb (with error handling & notifs) ----
attempts = 0
while attempts < 2:
    try:
        celeb_pic = celeb_pic_scrape.pic_scrape(plain_name)
        slack_notifications.scrape_worked()
        break
    except:
        attempts += 1
        slack_notifications.scrape_failed()


        # Call twitter push script (with error handling & notifs) ----
while attempts < 2:
    try:
        twitter_push.twit_push(consumer_key, consumer_secret,
                                access_token, access_token_secret,
                                celeb_tweet, celeb_pic)
        slack_notifications.post_worked()
        break
    except:
        attempts += 1
        slack_notifications.post_failed()


        # Remove image files from project folder ----
remove_jpgs.remove_jpg()
