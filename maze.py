#!/usr/bin/env python
from collections import defaultdict 
import numpy as np
from numpy.random import random_integers as rnd
import matplotlib.pyplot as plt

class Node:
    def __init__(self,x,y,cost,parent=None):
        self.x=x
        self.y=y
        self.cost=cost
        self.parent=parent


def get_path(matrix,final_set,start,end):
    
    matrix[end.x][end.y]=60
    parent=end.parent
    while(parent!=-1):
        node=final_set[parent]
        matrix[node.x][node.y]=60
        parent=node.parent

    return matrix


def get_index(node):
    return (node.x-0) +(node.y-0)*1

def solve(matrix,start,end):

    temp_set, final_set = dict(), dict()
    # print(get_index(start))
    temp_set[get_index(start)]=start
# ##############################movement in neighbours 
    motion =    [[1, 0, 1],   # move right
                [0, 1, 1],   # move up
                [-1, 0, 1],   # move left 
                [0, -1, 1],
                [-1,1,1.41],
                [1,-1,1.41],
                [1,1,1.41],
                [-1,-1,1.41]]    # move down 
##############################end
    while(True):
        res=not bool(temp_set)
        if res==True:
            print('set is empty')
            break

        c_id=min(temp_set,key=lambda o: temp_set[o].cost)
        current=temp_set[c_id]
        print(current.x,current.y)
        # break
        # ###########plotting of each point here ########
        matrix[current.x,current.y]=60
        ###########         end      ###########
        # break loop condition 
        if current.x==end.x and current.y==end.y:
            end.parent = current.parent
            end.cost = current.cost
            print('reached goal')
            break

        
        #####################################################################
        # Remove the item from the temp set
        del temp_set[c_id]
        # Add it to the final set
        final_set[c_id] = current

        for move_x, move_y, move_cost in motion:
                node = Node(current.x + move_x,current.y + move_y,current.cost+move_cost, c_id)

                
                if node.x<0 or node.x>=10 or node.y<0 or node.y>=10:  #boundary condition 
                     continue


                # check if the point is not an obstacle
                if matrix[node.x][node.y]==0: 
                    print('obstacles are',node.x,node.y)
                    continue                

                new_id=get_index(node)
                # if already parent chosen skip this point and continue
                if new_id in final_set:
                    continue


                if new_id not in temp_set:  # if completely new node
                    temp_set[new_id]=node
                else:
                    # check if distancd [u]>distacne[v]+ cost[u,v]
                    if temp_set[new_id].cost > node.cost:
                                temp_set[new_id] = node
    matrix=get_path(matrix,final_set,start,end)
    # print(matrix)
    return matrix 

N=10
row=N
col=N

start_x,start_y=0,0
end_x,end_y=5,8
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
x, y = rnd(0,row), rnd(0,col)
matrix[x,y] = 0
# count=count+1
print('seed point of maze',x,y)

for j in range(depth):

        # print(x,y)
    # look for its neigbours 
        adjacent=[]
        if x > 0:          adjacent.append( (x-1,y) )
        if x < col-1:      adjacent.append( (x+1,y) )
        if y > 0:          adjacent.append( (x,y-1) )
        if y < row-1:      adjacent.append( (x,y+1) )
        

        # out of the neighbours choose randomly the one which is to free 
        if len(adjacent):
                xnext,ynext = adjacent[rnd(0,len(adjacent)-1)] 
                # if already visited ignore otherwise make it free  
                if matrix[xnext,ynext] == 255:
                    matrix[xnext,ynext] = 0
                    # matrix[ynext+(y-ynext)//2, xnext+(x-xnext)//2] = 0
                    # matrix[ynext+(y-ynext)//4, xnext+(x-xnext)//4] = 0
        x, y = xnext, ynext
        matrix[start_x,start_y]=60
        matrix[end_x,end_y]=200
print(matrix)


start=Node(start_x,start_y,0,-1)
end=Node(end_x,end_y,0,-1)

matrix=solve(matrix,start,end)
matrix[start_x,start_y]=200
matrix[end_x,end_y]=200
plt.imshow(matrix,interpolation='nearest')
plt.xticks([]),plt.yticks([])
plt.grid(True)
plt.show()


