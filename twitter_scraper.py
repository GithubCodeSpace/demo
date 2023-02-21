import sys
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Get the command line arguments
username = sys.argv[1]
query = sys.argv[2]
start_date = sys.argv[3]
end_date = sys.argv[4]
limit = int(sys.argv[5])

# Construct the query string
query_str = f'({query}) until:{end_date} since:{start_date} filter:twimg'

# Scrape tweets using snscrape
tweets = []
for tweet in sntwitter.TwitterSearchScraper(query_str).get_items():
  if len(tweets) == limit:
    break
  else:
    tweets.append([tweet.date, tweet.content])

# Save the tweets to a CSV file
df = pd.DataFrame(tweets, columns=['Date', 'Tweet'])
df.to_csv(f'{username}_tweets.csv', index=False)
