import csv
import tweepy
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Oauth keys
consumer_key = "iw9671nIIGXTB0v2kVsR7VVS7"
consumer_secret = "e3zN1ath4rz8Q4cPkMhr3xXCdbR0HdJAykx8sdg33q8V3tgWFp"
access_token = "1132951742-rJVrQcl8HC17qybZ3LvpGHsGw7mY5YIfRijA6sB"
access_token_secret = "0XPHhXSHBbchY6nItpPlEVJyP4fgybT88OuAVkZdAUexO"

# Authentication with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# update these for the tweet you want to process replies to 'name' = the account username and you can find the tweet id within the tweet URL
name = 'Trainwreckstv'
tweet_id = '1549842583316209664'

replies=[]
for tweet in tweepy.Cursor(api.search_tweets,q='to:'+name, result_type='recent', timeout=999999).items(1000):
    if hasattr(tweet, 'in_reply_to_status_id_str'):
        if (tweet.in_reply_to_status_id_str==tweet_id):
            replies.append(tweet)

with open('replies_clean.csv', 'w') as f:
    csv_writer = csv.DictWriter(f, fieldnames=('user', 'text'))
    csv_writer.writeheader()
    for tweet in replies:
        row = {'user': tweet.user.screen_name, 'text': tweet.text.replace('\n', ' ')}
        csv_writer.writerow(row)
