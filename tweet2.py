"""This module fetches tweets using snscrape module and stores the results in a pandas DataFrame."""
import datetime
import json
import snscrape.modules.twitter as sntwitter

QUERY = "(websites) (from:Prathkum) until:2023-02-19 since:2023-02-01 -filter:replies"

try:
    tweets = []
    for tweet in sntwitter.TwitterSearchScraper(QUERY).get_items():
        date_str = tweet.date.strftime('%d/%m/%Y')
        tweets.append([tweet.rawContent, tweet.url, tweet.user.username, date_str])
except AttributeError:
    print(f"An error occurred: This may be due to a rate limit error or other issue.")
    tweets = []

# with open('tweets.json', 'w') as f:
#     json.dump(tweets, f)

for tweet in tweets:
    print("\n".join(tweet))
    print()
