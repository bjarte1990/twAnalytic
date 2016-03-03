import urllib
import json
import time

serviceurl='http://maps.googleapis.com/maps/api/geocode/json?'

def getLatLong(addresses):
	locationData=[]
	i=0
	for a in addresses:
		try:
			i=i+1
			if i==9:
				i=0
				time.sleep(10)
			url=serviceurl+urllib.urlencode({'sensor':'false', 'address': a})
			#print 'Retrieving ',url
			html=urllib.urlopen(url).read()

			#print 'Retrieved ',len(html),' characters'

			info=json.loads(html)

			if 'status' not in info or info['status'] != 'OK':
				print '==== Failure To Retrieve ===='
				print html
			else:
				data= info['results'][0]
				
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
	
#def loadData():
#	with open('geoData.json') as dataFile:
#		data=json.load(dataFile)
#	return data

	