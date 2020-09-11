#!/usr/bin/env python
from collections import defaultdict 
import numpy as np
from numpy.random import random_integers as rnd
import matplotlib.pyplot as plt

N=30
row=N
col=N

print('enter level 1-9')
level=int(input())
level=level/10.0

randomness=int(level*N)
depth=int(level*N)
# matrix= np.zeros((row+1,col+1), dtype=bool)
matrix=np.ones((row+1,col+1),dtype=int)
for i in range(randomness):
    # generate random coordinate
    x, y = rnd(0,row), rnd(0,col)
    matrix[y,x] = 0
    

    for j in range(depth):
    # look for its neigbours 
        adjacent=[]
        if x > 0:          adjacent.append( (y,x-1) )
        if x < col-1:      adjacent.append( (y,x+1) )
        if y > 0:          adjacent.append( (y-1,x) )
        if y < row-1: adjacent.append( (y+1,x) )
        

        # out of the neighbours choose randomly the one which is to free 
        if len(adjacent):
                ynext,xnext = adjacent[rnd(0,len(adjacent)-1)] 
                # if already visited ignore otherwise make it free  
                if matrix[ynext,xnext] == 1:
                    matrix[ynext,xnext] = 0
                    matrix[ynext+(y-ynext)//2, xnext+(x-xnext)//2] = 0
                    matrix[ynext+(y-ynext)//4, xnext+(x-xnext)//4] = 0
                    x, y = xnext, ynext
    # print(matrix)

plt.imshow(matrix,cmap=plt.cm.binary,interpolation='nearest')
plt.xticks([]),plt.yticks([])
plt.show()


