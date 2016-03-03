import urllib
import json
import twurl
import re

TWEET_URL = 'https://api.twitter.com/1.1/search/tweets.json'
USER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

def getData(url):

	print 'Retrieving ',url
	
	connection=urllib.urlopen(url)
	data=connection.read().decode("utf-8","replace")
	headers=connection.info().dict
	tweetJson=json.loads(data)
	
	print 'Remaining requests: ',headers['x-rate-limit-remaining']
	
	return tweetJson


def getTweetsByContent(content, tweetNum=10):
	
	url = twurl.augment(TWEET_URL,{'q': content, 'count': tweetNum})

	return getData(url)
	
def getTweetsByUser(userName, tweetNum=10):
	
	url = twurl.augment(USER_URL,{'screen_name': userName, 'count': tweetNum})
	
	return getData(url)