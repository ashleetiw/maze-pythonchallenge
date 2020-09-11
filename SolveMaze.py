import numpy as np

def dfs(graph,s):
    stack=[]
    stack.append(s)
    explored=set()
    explored.add(s)
    parent={s:None}

    while (len(stack)>0):
        state=stack.pop()
        neighbors=graph[state]
        for n in neighbors:
            if n not in explored:
                stack.append(n)
                explored.add(n)
                parent[n]=state
        #print(state)
    return parent


def StartMaze(maze_matrix,start_point,end_point):
    maze_matrix[start_point[0],start_point[1]]=3     # set the current location (start point1) as number 2
    maze_matrix[end_point[0],end_point[1]]=2         # set the goal (end point) as number 3 in the maze
    return maze_matrix

def AddtoGraph():
    return 0

def CheckNeighbor(maze_matrix,current_location,count):
    arrayForDic=[]
    maze_matrix[current_location[0],current_location[1]]

    neighbor = maze_matrix[current_location[0]+1,current_location[1]]
    if neighbor != 1:                                              # if neighbor is not a wall
        if neighbor == 0:                                               # if neighbor is not explored
            count += 1
            arrayForDic.append(count)                                   # append to arrayfordic
        elif neighbor == 2:                                               # if neighbor is the goal
            return "goal found"
        else:                                                             # if neighbor is already explored
            arrayForDic.append(neighbor)                                    # append to arrayfordic

    neighbor = maze_matrix[current_location[0]-1,current_location[1]]       
    if neighbor != 1:                                              # if neighbor is not a wall
        if neighbor == 0:                                               # if neighbor is not explored
            count += 1
            arrayForDic.append(count)                                   # append to arrayfordic
        elif neighbor == 2:                                               # if neighbor is the goal
            return "goal found"
        else:                                                             # if neighbor is already explored
            arrayForDic.append(neighbor)                                    # append to arrayfordic
    
        
    maze_matrix[current_location[0],current_location[1]+1]
    maze_matrix[current_location[0],current_location[1]-1]

    return arrayForDic, count

def dfs2(start_point,):
    return 1





if __name__ == '__main__':
    '''
    graph={
        "A":["B","C"],
        "B":["A","C","D"],
        "C":["A","B","D","E"],
        "D":["B","C","E","F"],
        "E":["C","D"],
        "F":["D"],
    }

    parent = dfs(graph,"A")
    goal = 'F'
    while goal != None:
        print(goal)
        goal=parent[goal]

    
    a=np.zeros((20,20))                     
    b=StartMaze(a,[1,2],[19,19])     
    print(b)
    '''


    a=[3,4]

    print(a[-1])

    dic = {3:None,4:[6,7]}
    dic.update({4:[9,10]})
    print(dic)




