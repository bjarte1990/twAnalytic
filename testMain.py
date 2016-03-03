import locations
import sys
import twitterHandler

#query=str(sys.argv[1])
#tweetNum=int(sys.argv[2])

#twData=locations.twitterLocation(query, tweetNum)

#for tw in twData:
#	print tw['tweet']
#	print '\t'+tw['location']

tweetsByUser=twitterHandler.getTweetsByUser('OW_Zoly',2)

print tweetsByUser