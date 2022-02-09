from logging import root
import queue


class Node:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None
    
    def add_element(self,node_value):
        node=Node(node_value)
        if self.root is None:
            self.root=node
            return
        queue=[self.root]
        while True:
            pop_node=queue.pop(0)
            if pop_node.left is None:
                pop_node.left=node
                return
            else:
                queue.append(pop_node.left)
            if pop_node.right is None:
                pop_node.right=node
                return
            else:
                queue.append(pop_node.right)
    
    def bfs(self):
        if self.root is None:
            return
        queue=[self.root]
        while queue:
            pop_node=queue.pop(0)
            print(pop_node.val)
            if pop_node.left is not None:
                queue.append(pop_node.left)
            if pop_node.right is not None:
                queue.append(pop_node.right)

    def dfs_preoder(self,root):
        if root is None:
            return
        print(root.val)
        self.dfs_preoder(root.left)
        self.dfs_preoder(root.right)

    def dfs_inorder(self,root):
        if root is None:
            return
        self.dfs_inorder(root.left)
        print(root.val)
        self.dfs_inorder(root.right)
        
    def dfs_postorder(self,root):
        if root is None:
            return
        self.dfs_postorder(root.left)
        self.dfs_postorder(root.right)
        print(root.val)
        


tree=Tree()
tree.add_element(1)
tree.add_element(2)
tree.add_element(3)
tree.add_element(4)
tree.add_element(5)
tree.add_element(6)
tree.add_element(7)
print("-------------------BFS-------------------")
tree.bfs()
print("-------------------DFS Preorder-------------------")
tree.dfs_preoder(tree.root)
print("-------------------DFS Inorder-------------------")
tree.dfs_inorder(tree.root)
print("-------------------DFS Postorder-------------------")
tree.dfs_postorder(tree.root)