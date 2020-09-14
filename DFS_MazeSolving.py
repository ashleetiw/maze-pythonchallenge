import numpy as np
import random


def StartMaze(maze_matrix,start_point,end_point):
    maze_matrix[start_point[0],start_point[1]]=int(3)     # set the current location (start point1) as number 2
    maze_matrix[end_point[0],end_point[1]]=int(2)         # set the goal (end point) as number 3 in the maze
    return maze_matrix


def CheckLeft(maze_matrix,current_location):
    if current_location[1] == 0:
        return False
    else:
        return True

def CheckRight(maze_matrix,current_location):
    n_col=np.shape(maze_matrix)[1]
    if current_location[1] == n_col - 1:
        return False
    else:
        return True

def CheckUp(maze_matrix,current_location):
    if current_location[0] == 0:
        return False
    else:
        return True

def CheckDown(maze_matrix,current_location):
    n_row=np.shape(maze_matrix)[0]
    if current_location[0] == n_row - 1:
        return False
    else:
        return True


def CheckNeighbor(maze_matrix,current_location,count,NumCorDic):
    arrayForDic=[]

    if CheckDown(maze_matrix,current_location) is True:                         # if on edge
        neighbor = maze_matrix[current_location[0]+1,current_location[1]]
        if neighbor != 1:                                                       # if neighbor is not a wall
            if neighbor == 0:                                                   # if neighbor is not explored
                count += 1
                arrayForDic.append(count)                                       # append to arrayfordic
                maze_matrix[current_location[0]+1,current_location[1]] = count  # set a new value to the free path
                NumCorDic[count]=[current_location[0]+1,current_location[1]]
            #elif neighbor == 2:                                                 # if neighbor is the goal
                #return True
            else:                                                               # if neighbor is already explored
                arrayForDic.append(neighbor)                                    # append to the array for the graph dictionary

    if CheckRight(maze_matrix,current_location) is True:
        neighbor = maze_matrix[current_location[0],current_location[1]+1]       
        if neighbor != 1:                                                       # if neighbor is not a wall
            if neighbor == 0:                                                   # if neighbor is not explored
                count += 1
                arrayForDic.append(count)                                       # append to arrayfordic
                maze_matrix[current_location[0],current_location[1]+1] = count  # set a new value to the free path
                NumCorDic[count]=[current_location[0],current_location[1]+1]
            #elif neighbor == 2:                                                 # if neighbor is the goal
                #return True
            else:                                                               # if neighbor is already explored
                arrayForDic.append(neighbor)                                    # append to arrayfordic

    if CheckLeft(maze_matrix,current_location) is True:
        neighbor = maze_matrix[current_location[0],current_location[1]-1]       
        if neighbor != 1:                                                       # if neighbor is not a wall
            if neighbor == 0:                                                   # if neighbor is not explored
                count += 1
                arrayForDic.append(count)                                       # append to arrayfordic
                maze_matrix[current_location[0],current_location[1]-1] = count  # set a new value to the free path
                NumCorDic[count]=[current_location[0],current_location[1]-1]
            #elif neighbor == 2:                                                 # if neighbor is the goal
                #return True
            else:                                                               # if neighbor is already explored
                arrayForDic.append(neighbor)                                    # append to arrayfordic

    if CheckUp(maze_matrix,current_location) is True:
        neighbor = maze_matrix[current_location[0]-1,current_location[1]]       
        if neighbor != 1:                                                       # if neighbor is not a wall
            if neighbor == 0:                                                   # if neighbor is not explored
                count += 1
                arrayForDic.append(count)                                       # append to arrayfordic
                maze_matrix[current_location[0]-1,current_location[1]] = count  # set a new value to the free path
                NumCorDic[count]=[current_location[0]-1,current_location[1]]
            #elif neighbor == 2:                                                 # if neighbor is the goal
                #return True
            else:                                                               # if neighbor is already explored
                arrayForDic.append(neighbor)                                    # append to arrayfordic

    return arrayForDic, maze_matrix, count, NumCorDic

if __name__ == '__main__':

    a=np.zeros((10,10))

    s=[0,4]
    e=[9,8]
    a[0][1]=1
    a[0][0]=1
    a[0][2]=1
    a[0][8]=1
    a[1][3]=1
    a[1][5]=1
    a[1][9]=1
    a[2][5]=1
    a[0][6]=1
    a1=StartMaze(a,s,e)

    count=int(3)
    current_cor = s
    graph={}
    NumCorDic={}
    NumCorDic[3]=current_cor
    NumCorDic[2]=e

    current_value = a1[current_cor[0],current_cor[1]]

    stack=[]
    path=[]
    stack.append(current_value)

    explored=set()
    went_set=set()

    explored.add(current_value)
    parent={current_value: None}

    while (len(stack)>0):
        state=stack.pop()
        went_set.add(state)                                              # set of points the robot went through
        if state == 2:                                                   # if found the goal, break
            path.append(2)
            break

        path.append(state)

        current_cor=NumCorDic[state]

        neighbors, a1, count, NumCorDic = CheckNeighbor(a1,current_cor,count,NumCorDic)
        random.shuffle(neighbors)

        count_in_explored = 0
        for n in neighbors:
            if n not in explored:
                stack.append(n)
                explored.add(n)
                parent[n]=state
            if n in went_set:
                count_in_explored += 1
        if count_in_explored == len(neighbors):                         # go back if no way out
            stack.append(parent[state])

    
    print(a1)
    print(path)
    path_cor=[]
    for n in path:
        path_cor.append(NumCorDic[n])                                   # save the corrdinate of each move
    print(path_cor)
