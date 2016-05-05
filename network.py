# -*- coding: utf-8 -*-
"""
Created on Thu May 05 10:40:48 2016

@author: cpigler
"""

import networkx as nx
from networkx.algorithms import bipartite
import re
import numpy as np

nodes = []
names = []
edges = []        
    
def load_data():
    fhand = open('marvel_network.txt')
    try:
        regex = '([0-9]+) \"(.*)\"'
        for line in fhand:
            if line.strip() == '*Edgeslist':
                break
            else:
                node = re.findall(regex, line)
                if node:
                    nodes.append(node[0][0])
                    names.append(node[0][1])
        for line in fhand:
            conn = line.split()
            for i in range(1,len(conn)):
                edges.append((names[int(conn[0]) - 1], conn[i]))
            
    finally:
        fhand.close()


load_data()

G = nx.Graph(edges)

degrees = nx.degree(G)
clusters = nx.clustering(G)
degrees_sorted = sorted(degrees.items(), key=lambda x:x[1])

bi_matrix = bipartite.biadjacency_matrix(G,nodes)

bi_matrix = np.matrix(bi_matrix)

print type(bi_matrix)

#character_projection = np.dot(bi_matrix.T, bi_matrix)
#M = np.zeros(shape=(len(character_names), len(comic_names)))
