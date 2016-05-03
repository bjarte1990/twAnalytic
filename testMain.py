import locations
import twitterHandler
import mapdrawer

query="leicester"
tweetNum=100

tw_locs = locations.get_locations_by_content(query, tweetNum)

tweet_coords = locations.get_lat_long(tw_locs)

lats = [];
longs = [];
for c in tweet_coords:
    lats.append(c['lat'])
    longs.append(c['long'])
    
map_drawer = mapdrawer.MapDrawer()
map_drawer.draw_markers(lats, longs, query)
