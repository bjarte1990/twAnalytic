import locations
import sys

query=str(sys.argv[1])
tweetNum=int(sys.argv[2])

twData=locations.twitterLocation(query, tweetNum)


for tw in twData:
	print tw['tweet']