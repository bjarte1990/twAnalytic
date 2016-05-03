# -*- coding: utf-8 -*-
"""
Created on Tue May 03 11:10:17 2016

@author: cpigler
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

class MapDrawer:
    
    mymap = None;
    projection = 'hammer';
    
    def __init__(self, projection = 'hammer', lon_0 = 0, resolution = 'c'):
        self.mymap = Basemap(projection, lon_0, resolution);
        self.mymap.bluemarble()
    
    def show_map(self):
        self.mymap.show();
        
    def draw_markers(self, lats, longs, title = '', clever_mode = 0):
        
        # draw parallels and meridians.
        lats = np.array(lats)
        longs = np.array(longs)
        if clever_mode:
            print "Clever mode is under construction" 
        xpt,ypt = self.mymap(longs,lats)
        print xpt;
        self.mymap.plot(xpt, ypt, 'ro')
        if title:
            plt.title('Tweets about ' + title) 
            plt.show()        
        
        #mymap = Basemap(projection = 'hammer', lon_0 = 0, resolution = 'c');
        #xpt,ypt = mymap(longs,lats)
        #mymap.plot(xpt, ypt, 'ro')