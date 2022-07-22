import csv
from multiprocessing.connection import Client
import os
import tweepy
import ssl
from dotenv import load_dotenv
load_dotenv()

ssl._create_default_https_context = ssl._create_unverified_context

# Oauth and client creation
bearer_token = os.getenv("bearer_token")
client = tweepy.Client(bearer_token)

# update these for the tweet you want to process replies to 'name' = the account username and you can find the tweet id within the tweet URL
#name = 'Trainwreckstv'
#tweet_id = '1549842583316209664'
q = 'conversation_id:1549842583316209664'

for tweet_batch in tweepy.Paginator(client.search_recent_tweets, query=q,
                                    tweet_fields=['context_annotations','created_at', 'public_metrics', 'author_id'], 
                                    user_fields=['name','username','location','verified','description'],
                                    max_results=100, expansions='author_id'):
                                        tweets = tweet_batch.data
                                        users = tweet_batch.includes["users"]

users = {user["id"]: user for user in users}
print(len(tweets),len(users))
with open('replies_clean.csv', 'w') as f:
    csv_writer = csv.DictWriter(f, fieldnames=('user', 'text'))
    csv_writer.writeheader()
    for tweet in tweets:
        user = users[tweet.author_id]
        row = {'user': '@' + user.username, 'text': tweet.text.replace('\n', ' ')}
        csv_writer.writerow(row)