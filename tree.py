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
            if pop_node.left==None:
                pop_node.left=node
                return
            else:
                queue.append(pop_node.left)
            if pop_node.right==None:
                pop_node.right=node
                return
            else:
                queue.append(pop_node.right)
    
    def bfs(self):
        if self.root==None:
            return
        queue=[self.root]
        while True:
            pop_node=queue.pop(0)
            print(pop_node.val)
            if pop_node.left!=None:
                queue.append(pop_node.left)
            else:
                return
            if pop_node.right!=None:
                queue.append(pop_node.right)
            else:
                return
    
