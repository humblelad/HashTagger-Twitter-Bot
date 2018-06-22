#By @robocyber
#Contributions welcome!

#Enter your credentials
import tweepy
from time import sleep
consumer_key = "XXXX"
consumer_secret = "XXXX"
access_token = "XXXX"
access_token_secret = "XXXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# Where q='#search1OR#search2' is url encoded, change them to whatever hashtag or keyword you want to search.
# Where items(10), will run the loop till 10 and net retweets will be 10.

for post in tweepy.Cursor(api.search, q='#search1%2BOR%2B#search2').items(10):
    try:
        print('\nRetweeting @' + post.user.screen_name + '-')

        post.retweet()
        print('Retweet published successfully.')

        # Where sleep(10), sleep is measured in seconds.
        # Change 10 to amount of seconds you want to have in-between retweets.
        sleep(10)

    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break
