# from datetime import datetime
import pandas as pd
import snscrape.modules.twitter as sntwitter
import pytz

QUERIES = ["(from:Prathkum) until:2023-03-04 since:2023-03-03 -filter:replies",
           "(from:Prathkum) (to:Prathkum) until:2023-03-04 since:2023-03-03"]
utc = pytz.UTC
ist = pytz.timezone('Asia/Kolkata')  # Set the timezone to IST

# Define empty list to store the tweets
tweets_list = []

# Loop through the tweets returned by snscrape
for query in QUERIES:
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        # Extract the required information from the tweet object
        tweet_content = tweet.rawContent  # type: ignore
        tweet_url = tweet.url
        tweet_date = tweet.date  # type: ignore # Convert UTC to IST datetime
        tweet_id = tweet.id
        # Convert the tweet datetime to UTC timezone
        tweet_date_utc = tweet_date.astimezone(utc)

        # Convert the tweet datetime to IST timezone
        tweet_date_ist = tweet_date_utc.astimezone(ist)

        # Format the tweet datetime as required
        tweet_date_formatted = tweet_date_ist.strftime('%d-%m-%Y %I:%M:%S %p')
        # Append the information to the tweets list as a dictionary
        tweets_list.append({
            'Tweet': tweet_content,
            'URL': tweet_url,
            'Date': tweet_date_formatted,
            'ID': tweet_id
        })

# Create a pandas DataFrame from the tweets list
tweets_df = pd.DataFrame(tweets_list, columns=[
                         'Tweet', 'URL', 'Date', 'ID'])
tweets_df.to_csv('notion.csv', index=False)
