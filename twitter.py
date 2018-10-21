'''
retrieves tweets from home
ofcourse! We will specify the limit
'''

import tweepy
from tweepy import OAuthHandler

# Here be main
def main():
# auth variables for keys
consumerKey = input('Enter your consumer key: ')
consumerSecret = input('Enter your consumer secret: ')
accessToken = input('Enter your access token: ')
accessSecret = input('Enter your access secret: ')

# OPEN the handle variable which acts like a cursor
handle=open('tweets.txt','w')

# Loading Auth variables 
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessSecret)
api = tweepy.API(auth)

# Cursor goes through each tweet and processes the status, limit is set to 100
for status in tweepy.Cursor(api.home_timeline).items(100):
    # Process a single status
    print (status.text)
    handle.write(status.text.encode('utf-8'))
    handle.write('\n \n')
handle.close()

# Here be main starting its game
if __name__ == "__main__": main()
