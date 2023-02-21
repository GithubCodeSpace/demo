"""This module fetches tweets using snscrape module and stores the results in a pandas DataFrame."""
import snscrape.modules.twitter as sntwitter
import pandas as pd
QUERY = "(websites) (from:Prathkum) until:2023-02-19 since:2023-02-01 -filter:replies"
LIMIT = 5000

try:
    tweets = [[tweet.rawContent, tweet.url, tweet.date]
              for tweet in sntwitter.TwitterSearchScraper(QUERY).get_items()][:LIMIT]
except AttributeError:
    print(f"An error occurred: This may be due to a rate limit error or other issue.")
    tweets = []

df = pd.DataFrame(tweets, columns=['Tweet', 'URL', 'Date'])
df.to_csv('tweets.csv', index=False)


# import snscrape.modules.twitter as sntwitter
# import pandas as pd

# query = "(websites) (from:Prathkum) until:2023-02-19 since:2023-02-01 -filter:replies"
# tweets = []
# limit = 5000


# for tweet in sntwitter.TwitterSearchScraper(query).get_items():
#     # print(vars(tweet))
#     # break
#     if len(tweets) == limit:
#         break
#     else:
#         tweets.append([tweet.rawContent, tweet.url, tweet.date])

# df = pd.DataFrame(tweets, columns=['Tweet', 'URL', 'Date'])
# print(df)

# # to save to csv
# df.to_csv('tweets.csv')
