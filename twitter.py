'''
retrieves tweets from home
ofcourse! We will specify the limit
'''

import tweepy
from tweepy import OAuthHandler

# Here be main
def main():
# variables for keys
consumerKey = input('Enter your consumer key: ')
consumerSecret = input('Enter your consumer secret: ')
accessToken = input('Enter your access token: ')
accessSecret = input('Enter your access secret: ')

# OPEN ZE HANDLE
handle=open('tweets.txt','w')

# Auth variables
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessSecret)
api = tweepy.API(auth)

# <Insert cool stuff here>
for status in tweepy.Cursor(api.home_timeline).items(100):
    # Process a single status
    print (status.text)
    handle.write(status.text.encode('utf-8'))
    handle.write('\n \n')
handle.close()

# Here be main starting its game
if __name__ == "__main__": main()
