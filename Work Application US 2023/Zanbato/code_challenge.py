class King_Domino:
    def __init__(self, board, crown):
        # Intilize variables
        self.board=board
        self.crown=crown
        self.visited=[[False for _ in range(len(board[0]))] for _ in range(len(board))]
        self.queue=[]
        self.point=0
        self.row_length=len(board)
        self.col_length=len(board[0])

    # Caculate total points for the game
    def caculate_point(self):
        for i in range(self.row_length):
            for j in range(self.col_length):
                if self.visited[i][j]==False and self.crown[i][j]!=0:
                    self.queue.append((i,j))
                    square,crown=self.bfs(0,0)
                    self.point+=square*crown
        return self.point

    # check if the index if in the board, has not been visited and it is in the same sub-area
    def checker(self,x,y,pop_node_i,pop_node_j):
        if 0<=x<self.row_length and 0<=y<self.col_length\
            and self.visited[x][y]==False\
            and self.board[pop_node_i][pop_node_j]==self.board[x][y]:
            return True 
        else:
            return False

    # bfs        
    def bfs(self,square,crown):
        while self.queue:
            pop_node_i,pop_node_j=self.queue.pop(0)
            square+=1
            crown+=self.crown[pop_node_i][pop_node_j]
            self.visited[pop_node_i][pop_node_j]=True
            for x, y in [[1,0],[-1,0],[0,1],[0,-1]]:
                temp_x=pop_node_i+x
                temp_y=pop_node_j+y
                if self.checker(temp_x,temp_y,pop_node_i,pop_node_j):
                    self.queue.append((temp_x,temp_y))
                    self.visited[temp_x][temp_y]=True
        return square,crown
        




map1=[['S','S','S','L','L'],\
    ['S','W','W','W','L'],\
    ['L','W','K','W','L'],\
    ['F','W','W','F','F'],\
    ['F','F','F','F','L']]

crown1=[[0,0,0,0,0],\
       [1,0,1,1,0],\
       [1,0,0,0,1],\
       [0,0,0,1,0],\
       [0,0,1,1,0]]
game1=King_Domino(map1,crown1)
print("The total points for the board is", game1.caculate_point())


map2=[['S','S','S','L','L'],\
    ['S','W','W','W','L'],\
    ['L','W','K','W','L'],\
    ['F','W','W','F','F'],\
    ['F','F','F','F','L']]

crown2=[[0,0,0,0,0],\
       [1,0,1,1,0],\
       [3,0,0,0,1],\
       [0,0,0,1,0],\
       [0,0,1,1,0]]
game2=King_Domino(map2,crown2)
print("The total points for the board is", game2.caculate_point())

map3=[['S','S','S','L','L'],\
    ['S','W','W','W','L'],\
    ['L','W','K','W','L'],\
    ['F','W','W','F','F'],\
    ['F','F','F','F','L']]

crown3=[[0,0,0,0,0],\
       [1,0,1,1,0],\
       [3,2,0,3,1],\
       [0,0,0,1,0],\
       [0,0,1,1,0]]
game3=King_Domino(map3,crown3)
print("The total points for the board is", game3.caculate_point())


map4=[['S','S','S','L','L'],\
    ['S','W','W','W','L'],\
    ['L','W','K','W','L'],\
    ['F','W','W','F','F'],\
    ['F','F','F','F','L']]

crown4=[[0,0,0,0,0],\
       [0,0,0,0,0],\
       [0,0,0,0,0],\
       [0,0,0,0,0],\
       [0,0,0,0,0]]
game4=King_Domino(map4,crown4)
print("The total points for the board is", game4.caculate_point())