import csv
import tweepy
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Oauth keys
#consumer_key = "XXX"
#consumer_secret = "XXX"
#access_token = "XXX"
#access_token_secret = "XXX"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAEcyeAEAAAAAYVElWMuD5xJSfb6nbkMX%2BuQguVU%3DROs4CCVh9uIfEsZdGm5CokvXLk1EKNc55lwsWtkP3To5t7Fumf"

# Authentication with Twitter
auth = tweepy.OAuth2BearerHandler(bearer_token)
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
