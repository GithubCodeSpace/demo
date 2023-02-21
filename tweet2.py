"""This module fetches tweets using snscrape module and stores the results in a pandas DataFrame."""
import snscrape.modules.twitter as sntwitter
import pandas as pd

username = "Prathkum"
since_date = "2023-02-16"
until_date = "2023-02-17"

# Construct the query to fetch tweets by the specified user during the specified time period
query = f"from:{username} since:{since_date} until:{until_date}"

# Create an empty list to store the tweets
tweets = []

# Use a for loop to iterate through each tweet returned by the scraper
for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    # Check if the tweet is a reply to another tweet in the list
    if hasattr(tweet, "inReplyToId") and any(t["id"] == tweet.inReplyToId for t in tweets):

        # If the tweet is a reply, add it to the thread of the original tweet
        for t in tweets:
            if t["id"] == tweet.inReplyToId:
                t["thread"].append(tweet.rawContent)
                break

    else:
        # If the tweet is not a reply, add it to the list of tweets
        tweets.append({
            "id": tweet.id,
            "content": tweet.rawContent,
            "thread": [],
            "date": tweet.date,
            "URL": tweet.url
        })

# Create a DataFrame from the tweets list
df = pd.DataFrame(tweets, columns=["id", "content", "thread", "date", "URL"])

# Write the DataFrame to a CSV file
df.to_csv('tweets.csv', index=False)
df.to_json('tweets.json', orient='records')
