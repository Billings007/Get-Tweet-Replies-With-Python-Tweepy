import csv
from multiprocessing.connection import Client
import tweepy
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Oauth and client creation
bearer_token = "AAAAAAAAAAAAAAAAAAAAAEcyeAEAAAAAYVElWMuD5xJSfb6nbkMX%2BuQguVU%3DROs4CCVh9uIfEsZdGm5CokvXLk1EKNc55lwsWtkP3To5t7Fumf"
client = tweepy.Client(bearer_token)

# update these for the tweet you want to process replies to 'name' = the account username and you can find the tweet id within the tweet URL
name = 'Trainwreckstv'
#tweet_id = '1549842583316209664'
query = 'conversation_id:1549842583316209664'

replies=[]
for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, tweet_fields=['context_annotations', 'created_at'],user_fields=['profile_image_url'], expansions='author_id', max_results=100):
    print(tweet.author_id)
    if hasattr(tweet, 'in_reply_to_user_id": "3256068152"'):
        #if (tweet.in_reply_to_status_id_str==tweet_id):
            replies.append(tweet)

with open('replies_clean.csv', 'w') as f:
    csv_writer = csv.DictWriter(f, fieldnames=('user', 'text'))
    csv_writer.writeheader()
    for tweet in replies:
        row = {'user': tweet.author_id, 'text': tweet.text.replace('\n', ' ')}
        csv_writer.writerow(row)
