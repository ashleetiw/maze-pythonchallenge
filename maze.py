#!/usr/bin/env python
from collections import defaultdict 
import numpy as np
from numpy.random import random_integers as rnd
import matplotlib.pyplot as plt

N=10
row=N
col=N

start_x,start_y=0,4
end_x,end_y=9,8
print('enter level 1-9')
level=int(input())
level=level/10.0



randomness=int(level*N)
depth=int(level*N*N)
print('depth',depth)
# matrix= np.zeros((row+1,col+1), dtype=bool)
matrix=np.ones((row+1,col+1),dtype=int)*255

# count=0
# for i in range(randomness):
#     # generate random coordinate
#     if count==0:
# x, y = rnd(0,row), rnd(0,col)
matrix[y,x] = 0
# count=count+1
print('seed point of maze',x,y)

for j in range(depth):

        # print(x,y)
    # look for its neigbours 
        adjacent=[]
        if x > 0:          adjacent.append( (y,x-1) )
        if x < col-1:      adjacent.append( (y,x+1) )
        if y > 0:          adjacent.append( (y-1,x) )
        if y < row-1:      adjacent.append( (y+1,x) )
        

        # out of the neighbours choose randomly the one which is to free 
        if len(adjacent):
                ynext,xnext = adjacent[rnd(0,len(adjacent)-1)] 
                # if already visited ignore otherwise make it free  
                if matrix[ynext,xnext] == 255:
                    matrix[ynext,xnext] = 0
                    # matrix[ynext+(y-ynext)//2, xnext+(x-xnext)//2] = 0
                    # matrix[ynext+(y-ynext)//4, xnext+(x-xnext)//4] = 0
        x, y = xnext, ynext
        matrix[start_x,start_y]=60
        matrix[end_x,end_y]=200
        # print(matrix)
    

plt.imshow(matrix,interpolation='nearest')
plt.xticks([]),plt.yticks([])
plt.show()


