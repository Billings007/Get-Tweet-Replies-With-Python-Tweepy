import csv
from multiprocessing.connection import Client
import tweepy
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Oauth and client creation
bearer_token = "AAAAAAAAAAAAAAAAAAAAAEcyeAEAAAAAYVElWMuD5xJSfb6nbkMX%2BuQguVU%3DROs4CCVh9uIfEsZdGm5CokvXLk1EKNc55lwsWtkP3To5t7Fumf"
client = tweepy.Client(bearer_token)

# update these for the tweet you want to process replies to 'name' = the account username and you can find the tweet id within the tweet URL
#name = 'Trainwreckstv'
#tweet_id = '1549842583316209664'
query = 'conversation_id:1549842583316209664'

tweets= client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'],user_fields=['profile_image_url', 'username'], expansions='author_id')
users = {u["id"]: u for u in tweets.includes['users']}

with open('replies_clean.csv', 'w') as f:
    csv_writer = csv.DictWriter(f, fieldnames=('user', 'text'))
    csv_writer.writeheader()
    for tweet in tweets.data:
        if users[tweet.author_id]:
            user = users[tweet.author_id]
        row = {'user': '@' user.username, 'text': tweet.text.replace('\n', ' ')}
        csv_writer.writerow(row)
