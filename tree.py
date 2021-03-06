from inspect import stack
from logging import root
import queue
import re


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
    
    def dfs_preorder_stack(self):
        if self.root is None:
            return
        stack=[self.root]
        while stack:
            pop_node=stack.pop()
            print(pop_node.val)
            if pop_node.right is not None:
                stack.append(pop_node.right)
            if pop_node.left is not None:
                stack.append(pop_node.left)


    def dfs_inorder(self,root):
        if root is None:
            return
        self.dfs_inorder(root.left)
        print(root.val)
        self.dfs_inorder(root.right)
    
    def dfs_inorder_stack(self):
        if self.root is None:
            return
        stack=[]
        cur=self.root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur=cur.left
            pop_node=stack.pop()
            print(pop_node.val)
            cur=pop_node.right
        

    def dfs_postorder(self,root):
        if root is None:
            return
        self.dfs_postorder(root.left)
        self.dfs_postorder(root.right)
        print(root.val)
    
    def dfs_postorder_stack(self):
        # Need to reverse it
        res=[]
        if self.root is None:
            return
        stack=[self.root]
        while stack:
            pop_node=stack.pop()
            res.append(pop_node.val)
            if pop_node.left is not None:
                stack.append(pop_node.left)
            if pop_node.right is not None:
                stack.append(pop_node.right)
        return res[::-1]
        
        


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
print("-------------------DFS Preorder Stack-------------------")
tree.dfs_preorder_stack()
print("-------------------DFS Inoder Stack-------------------")
tree.dfs_inorder_stack()
print("-------------------DFS Postoder Stack-------------------")
print(tree.dfs_postorder_stack())