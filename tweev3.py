"""This module fetches tweets using snscrape module and stores the results in a pandas DataFrame."""
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Define the search queries
search_queries = [
    "(from:Prathkum) since:2023-03-03 until:2023-03-04 -filter:replies",
    "(from:Prathkum) (to:Prathkum) until:2023-03-03 since:2023-03-02"
]

# Create a list to hold the tweets
tweets_list = []

# Loop through each query and scrape tweets for that query
for query in search_queries:
    # Loop through each tweet and append it to the list
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        tweets_list.append([tweet.rawContent, tweet.url, tweet.date])

# Convert the list of tweets into a pandas dataframe
tweets_df = pd.DataFrame(tweets_list, columns=["Text", "URL", "Date"])

# Save the dataframe as a CSV file
tweets_df.to_csv("tweets.csv", index=False)
