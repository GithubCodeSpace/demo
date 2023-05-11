"""This module fetches tweets using snscrape module and stores the results in a pandas DataFrame."""
import pandas as pd
import snscrape.modules.twitter as sntwitter

QUERIES = ["(from:Prathkum) until:2023-03-03 since:2023-03-02",
           "(from:NikkiSiapno) (to:NikkiSiapno) until:2023-03-03 since:2023-03-02"]

# Define empty list to store the tweets
tweets_list = []

# Loop through the tweets returned by snscrape
for query in QUERIES:
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        # Extract the required information from the tweet object
        tweet_content = tweet.rawContent
        tweet_url = tweet.url
        tweet_username = tweet.user.username
        tweet_date = tweet.date.strftime('%d/%m/%Y')

        # Append the information to the tweets list as a dictionary
        tweets_list.append({
            'Tweet': tweet_content,
            'URL': tweet_url,
            'Username': tweet_username,
            'Date': tweet_date,
            'Query': query
        })

# Create a pandas DataFrame from the tweets list
tweets_df = pd.DataFrame(tweets_list, columns=[
                         'Tweet', 'URL', 'Username', 'Date', 'Query'])
tweets_df.to_csv('notion.csv', index=False)
