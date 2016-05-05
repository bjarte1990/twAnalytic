import urllib
import json
import time
import twurl
import re
import twitterHandler

GOOGLEMAPS_URL='http://maps.googleapis.com/maps/api/geocode/json?'

def twitterLocation(content, tweetNum=10):
	
	tweetJson=twitterHandler.getTweetsByContent(content, tweetNum)
	statuses=tweetJson['statuses']

	locationList=[]
	for tweet in statuses:
		user=tweet['user']
		try:
			#print tweet['text']
			#print user['location'],'\n'
			location=user['location']
			if location:
				twitterData=dict()
				twitterData['tweet']=tweet['text']
				twitterData['location']=location
				locationList.append(twitterData)
		except UnicodeEncodeError:
			#print '.....Encoding error.....\n'
			continue
			

	return locationList
 
def get_locations_by_content(content, tweetNum=10):
    
    tweetJson=twitterHandler.getTweetsByContent(content, tweetNum)
    statuses=tweetJson['statuses']

    locationList=[]
    for tweet in statuses:
        try:
            location=tweet['user']['location'];
            if location:
                locationList.append(location)
        except UnicodeEncodeError:
            continue
    
    return locationList

def get_lat_long(addresses):
    #Retrievs geocodes of given addresses using google maps API
    locationData=[]
    i=0
    for a in addresses:
        try:
            i=i+1
            if i==9:
                i=0
                time.sleep(10)
            url=GOOGLEMAPS_URL+urllib.urlencode({'sensor':'false', 'address': a})
    		#print 'Retrieving ',url
            html=urllib.urlopen(url).read()
    
            #print 'Retrieved ',len(html),' characters'
            info=json.loads(html)
    
            if 'status' not in info or info['status'] != 'OK':
                
                print '==== Failure To Retrieve ===='
                print html
            else:
                data = info['results'][0]
    				
                address=data['formatted_address']
    					
                print 'Address: ',address
    				
                location=data['geometry']['location']
    
                print 'Lat: ',location['lat']," Long: ",location['lng']
                newData=dict()
                newData['name']=address
                newData['lat']=location['lat']
                newData['long']=location['lng']
                locationData.append(newData)
        except UnicodeEncodeError:
            print 'Encoding error...'
    			
    return locationData	


	
