import re

# The time complexity for this algorithm is O(m*n)
# where m is row length and n is column length
# I am using DFS to solve this problem

def find_same_area(x,y,map,crown,vis,record):
    # record[0] records how many squares
    # record[1] records how many crowns
    record[0]+=1
    if crown[x][y]==1:
        record[1]+=1
    vis[x][y]=True
    for i in [[0,1],[1,0],[0,-1],[-1,0]]:
        newX=x+i[0]
        newY=y+i[1]
        if 0<=newX<len(map) and 0<=newY<len(map[0]):
            if vis[newX][newY]==False and map[x][y]==map[newX][newY]:
                # check to make sure newX and newY are in the map
                # also they are in the same group and never been visited
                # dfs
                find_same_area(newX,newY,map,crown,vis,record)

def question1(map,crown):
    vis=[[False for _ in range(len(map[0]))] for _ in range(len(map))]
    res=0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if vis[i][j]==False:
                record=[0,0]
                find_same_area(i,j,map,crown,vis,record)
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