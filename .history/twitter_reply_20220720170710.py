import csv
import tweepy
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Oauth keys
consumer_key = "eVdQenJiM1NoNEl3elh3bHNzbEk6MTpjaQ"
consumer_secret = "1PYu6gOHRZOTfiHxYM3TXHdLgFGNo1iVnyaDwjxETAZYderZWE"
access_token = "1132951742-oIOZAX0BXXdz5ghtn4nldViQXL4Q0Jd5xu1lUCU"
access_token_secret = "8wkiGUInnNicaFt6BcPIPJP6c3i4tOyz16rGaL4XPQ174"

# Authentication with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# update these for the tweet you want to process replies to 'name' = the account username and you can find the tweet id within the tweet URL
name = 'Trainwreckstv'
tweet_id = '1549842583316209664'

replies=[]
for tweet in tweepy.Cursor(api.search_tweets,q='to:'+name, result_type='recent', timeout=99999).items(1000):
    if hasattr(tweet, 'in_reply_to_status_id_str'):
        if (tweet.in_reply_to_status_id_str==tweet_id):
            replies.append(tweet)

with open('replies_clean.csv', 'w') as f:
    csv_writer = csv.DictWriter(f, fieldnames=('user', 'text'))
    csv_writer.writeheader()
    for tweet in replies:
        row = {'user': tweet.user.screen_name, 'text': tweet.text.replace('\n', ' ')}
        csv_writer.writerow(row)
