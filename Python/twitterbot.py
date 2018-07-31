import tweepy
import random
import time

CONSUMER_KEY    = 'cgyiyeniPu005NJKj9aGF40zk'
CONSUMER_SECRET = 'epnkpbjBUJbEKGsu6djKHFLncwV6NxTAHrFSDuRbb0VImF8p68'

ACCESS_TOKEN    = '1017154585503227905-dtLIY0TtkY3ge0pf2evYDYR5FDUkza'
ACCESS_SECRET   = 'SVw23Hx8OFnqyQ3RMKlM3TmEhOoq1eSXkRtB9f66MY8cB'


tweets = ["gurl u thiccer than a bowl of oatmeal", "u my rawrbae <3", "snacc"]


# Authentication

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api  = tweepy.API(auth)

# Update Status
count = 0
while True:
    count += 1
    index = random.randint(0, len(tweets) - 1)
    api.update_status(tweets[index] + str(count))
    time.sleep(5)
