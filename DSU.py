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

dsu=DSU(4)
dsu.connect_node(1,2)
dsu.connect_node(2,3)
dsu.connect_node(2,3)
print(dsu.relation_list)