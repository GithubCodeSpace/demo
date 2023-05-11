"""This module fetches tweets using snscrape module and stores the results in a pandas DataFrame."""
import snscrape.modules.twitter as sntwitter
import pandas as pd
import json

QUERY = "(websites) (from:Prathkum) until:2023-02-19 since:2023-02-01 -filter:replies"
LIMIT = 5000

try:
    tweets = [[tweet.url] for tweet in sntwitter.TwitterSearchScraper(QUERY).get_items()][:LIMIT]
except AttributeError:
    print(f"An error occurred: This may be due to a rate limit error or other issue.")
    tweets = []

with open('tweets.json', 'w') as f:
    json.dump(tweets, f)
