"""This module fetches tweets using snscrape module and stores the results in a pandas DataFrame."""
import pandas as pd
import snscrape.modules.twitter as sntwitter
import pytz

QUERIES = {"Thread": "(from:NikkiSiapno) until:2023-03-28 since:2022-04-01 -filter:replies",
           "Tweet": "(from:NikkiSiapno) (to:NikkiSiapno) until:2023-03-28 since:2022-04-01"}
utc = pytz.UTC
ist = pytz.timezone('Asia/Kolkata')  # Set the timezone to IST

# Define empty list to store the tweets
tweets_list = []

# Loop through the queries and the tweets returned by snscrape
for label, query in QUERIES.items():
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        # Extract the required information from the tweet object
        tweet_content = tweet.rawContent 
        tweet_url = tweet.url
        tweet_date = tweet.date
        tweet_id = tweet.id
        # Convert the tweet datetime to UTC timezone
        tweet_date_utc = tweet_date.astimezone(utc)

        # Convert the tweet datetime to IST timezone
        tweet_date_ist = tweet_date_utc.astimezone(ist)

        # Format the tweet datetime as required
        tweet_date_formatted = tweet_date_ist.strftime('%d-%m-%Y %I:%M:%S %p')
        # Append the information to the tweets list as a dictionary
        tweets_list.append({
            'Post': tweet_content,
            'URL': tweet_url,
            'Type': label,
            'Date': tweet_date_formatted,
            'ID': tweet_id
        })

# Create a pandas DataFrame from the tweets list
tweets_df = pd.DataFrame(tweets_list, columns=['Post', 'URL', 'Type', 'Date', 'ID'])
tweets_df.to_csv('notion.csv', index=False)
