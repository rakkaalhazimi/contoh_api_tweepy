import tweepy
from datetime import datetime
from pprint import pprint

consumer_key = "eLTnOpMoAH0ZmCYBONvzkwlFL"
consumer_secret = "m83eCknhZz4gFof74JTrFW9ob5A8n2VmIKyLaLTjnjcZU1sRQt"
access_token = "1097359730710704128-zqnaYi2aGEOKobo3ocsE5tkVOTFJGm"
access_token_secret = "ZZpfsQYkwBzSgsPyShXLnCUHZDBfFCpeCZMBGFclzJciy"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# followers = api.followers()

# followers
# for follower in followers:
    # print(follower.name)

# iterate through all of the authenticated user's friend
# for friend in tweepy.Cursor(api.friends).items():
    # Proceed friend here
    # print(friend.name)
    # break

# Iterate through the first 200 statuses in the home timeline
# for status in tweepy.Cursor(api.home_timeline, tweet_mode="extended").items(1):
#     Process the status here
    # pprint(status._json)

# Update status
# api.update_status(status="This tweet is written on my python script using tweepy library.")

# User tweet
# for tweet in public_tweets:
    # print({"id": tweet.id, "status": tweet.text})

# Delete tweet
# api.destroy_status(id=1269240507533676544)

# Get user id
# user = api.get_user(screen_name="msaid_didu")
# id_didu = user.id_str
# pprint(user.id_str)

# Trace tweet replies
# for reply in tweepy.Cursor(api.search, q="to:{} filter:replies".format("@aniesbaswedan"), tweet_mode="extended").items(100):
#    print(reply.full_text)
#    print()

# Search tweet
# jokowi_tweet = tweepy.Cursor(api.search, q="Jokowi", count=1, include_entities=False, tweet_mode="extended").items(10)
#
# file = open("json.txt", "w", encoding="utf-8")
#
# for jokowi in jokowi_tweet:
#
#
#     if "retweeted_status" in jokowi._json:
#         retweet_text = "@RT" + api.get_user(jokowi.retweeted_status.user.id_str).screen_name
#         print(
#             {"User": jokowi.user.name,
#              "Created_at": jokowi.created_at.strftime("%Y-%M-%d"),
#              "Status": retweet_text + jokowi._json["retweeted_status"]["full_text"]
#              }
#         )
#
#     else:
#         print(
#             {"User": jokowi.user.name,
#              "Created_at": jokowi.created_at.strftime("%Y-%M-%d"),
#              "Status": jokowi.full_text
#              }
#         )
#
# file.close()

