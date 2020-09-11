#!/usr/bin/env python
import random
import math
import matplotlib.pyplot as plt
import numpy as np


start=[50,50]
nodes=[]
nodes.append(start)

fig, ax = plt.subplots()
ax.set_xlim(0,100)
ax.set_ylim(0,100)

for i in range(500):
    #STEP 1: generate random node 
    point=[random.randint(0,100),random.randint(0,100)]

     # STEP2 :finding the nearest vertix 
    d_list=[]
    for node in nodes:
        distance=abs(node[0]-point[0])+abs(node[1]-point[1])  # L1 distance for fast computation 
        d_list.append(distance)

    # find min distance and its index 
    min_val=min(d_list)
    min_index=d_list.index(min_val)


    # STEP 3:make the min index point as the parent for the newly created random point 
    parent_node=nodes[min_index]
    # print('parent_node',parent_node)
    nodes.append([point[0],point[1]])
    x=[parent_node[0],point[0]]
    y=[parent_node[1],point[1]]
    plt.plot([point[0]], [point[1]], marker='o', markersize=3, color="red")
    plt.plot(x,y, '-g')
    # plt.hold(True)

    # print('after interation',i)
plt.show()