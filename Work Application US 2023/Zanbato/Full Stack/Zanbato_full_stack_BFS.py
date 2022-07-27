import re

# The time complexity for this algorithm is O(m*n)
# where m is row length and n is column length
# I am using BFS to solve this problem

def find_same_area(queue,map,crown,vis,record):
    # while queue is not empty starts BFS
    while queue:
        x,y=queue.pop(0)
        # record[0] records how many squares
        # record[1] records how many crowns
        record[0]+=1
        if crown[x][y]==1:
            record[1]+=1
        vis[x][y]=True
        for i in [[1,0],[-1,0],[0,1],[0,-1]]:
            newX=x+i[0]
            newY=y+i[1]
            if 0<=newX<len(map) and 0<=newY<len(map[0])\
                and vis[newX][newY]==False and map[x][y]==map[newX][newY]:
                # check to make sure newX and newY are in the map
                # also they are in the same group and never been visited
                queue.append((newX,newY))
                vis[newX][newY]=True



def question1(map,crown):
    vis=[[False for _ in range(len(map[0]))] for _ in range(len(map))]
    res=0
    queue=[]
    for i in range(len(map)):
        for j in range(len(map[0])):
            if vis[i][j]==False:
                queue.append((i,j))
                record=[0,0]
                find_same_area(queue,map,crown,vis,record)
                res+=(record[0]*record[1])
    return res

map=[['S','S','S','L','L'],\
    ['S','W','W','W','L'],\
    ['L','W','K','W','L'],\
    ['F','W','W','F','F'],\
    ['F','F','F','F','L']]

crown=[[0,0,0,0,0],\
       [1,0,1,1,0],\
       [1,0,0,0,1],\
       [0,0,0,1,0],\
       [0,0,1,1,0]]
print("The total points for the board is", question1(map,crown))