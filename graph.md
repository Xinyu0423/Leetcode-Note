# Graph

## Question
1. ~~994--思考994和695的区别~~
2. ~~695--bfs,dfs(非递归)~~

## 03/04/2022
1. 比较1091和994，994是多个中心同时开始bfs，1091是一个中心开始bfs。
2. 200题用while写一次。
3. 785
4. 547
5. 并查集

## Note
1. 二分图属于染色问题来做，染色问题不一定只有二分图

## 03/09/2022
1. 并查集(DSU):解决无向图的判环问题
   1. 547尝试用并查集做，684
2. 有向图判环
   1. 207
   
## 图的考点
1. 连通图
   1. 岛屿
2. 无向图判环
   1. 使用邻接表+度表
   2. 使用DSU
3. 有向图判环
   1. 使用邻接表+入度表

   

## 并查集 (DSU)
概念：如果两个节点有相同的根节点，那么两个节点一定相连
```python
# Disjoint set union(DSU)

# # 功能
# 1. 判断node1，node2是否相连，就是判断两者的root notde是否相连
# 2. 如果不相连，就把两者相连，就是把node1和node2的root相连

class DSU:
    def __init__(self,node_num):
        self.relation_list=[-1 for _ in range(node_num+1)]
    
    def find_root_node(self,node):
        while self.relation_list[node]!=-1:
            node=self.relation_list[node]
        return node
        

    def connect_node(self,node1,node2):
        root_node1=self.find_root_node(node1)
        root_node2=self.find_root_node(node2)
        if root_node1!=root_node2:
            self.relation_list[root_node1]=root_node2
        else:
            print("The two nodes has been connected")
```

## List Comprehension (列表推导式):
1. ```print([j.val for j in i.neighbors])```

## 入度表和邻接表
1. 邻接表存每个node的出node
2. 入度表存每个node的入个数