# import requests
# import mysql.connector
# import pandas as pd

# print('Hello')

# Define a simple tree node class.
 #     Write a function to convert an array into a binary search tree, using the node class you've defined.
# Example: [4, 2, 10,3] could give a tree like this:
#        4
#    /     \
#  2         10
#   \
#     3

class BST:
    def __init__(self,vaule):
        self.left=None
        self.right=None
        self.vaule=vaule
    
    def insert(self,vaule):
        if vaule<self.vaule:
            if self.left==None:
                self.left=BST(vaule)
            else:
                self.left.insert(vaule)
        else:
            if self.right==None:
                self.right=BST(vaule)
            else:
                self.right.insert(vaule)

def generateTree(arr):
    if not arr:
        print("Nothing in the arr")
        return None
    root=BST(arr[0])
    for i in range(1,len(arr)):
        root.insert(arr[i])
    return root

tree_value=[]
def printTree(root):
    if not root:
        return
    
    printTree(root.left)
    tree_value.append(root.vaule)
    printTree(root.right)
    return tree_value
        
# tree1=generateTree([4, 2, 10,3])
# # print(tree1.vaule)
# # print(tree1.left.vaule)
# # print(tree1.right.vaule)
# # print(tree1.left.right.vaule)
# printTree(tree1)
# print(tree_value)


# tree2=generateTree([2,10,11,3])
# printTree(tree2)
# print(tree_value)

# tree3=generateTree([])
# printTree(tree3)
# print(tree_value)

tree4=generateTree([2,2,2,100,10,1])
printTree(tree4)
print(tree_value)


# Basic question:
# Google allows you to run calculations from the search field, for example 3+4 or (3-7.5)^2. How would you go about testing this?
# https://www.google.com/search?q=3%2B4&source=hp&ei=uoFEY5aXG7CdkPIPx46rkAo&iflsig=AJiK0e8AAAAAY0SPykaKJI_C51saIR2eLiErCUSa3eWE&ved=0ahUKEwiW3Pyjwdb6AhWwDkQIHUfHCqIQ4dUDCAk&uact=5&oq=3%2B4&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgsIABCABBCxAxCDAToLCC4QgAQQsQMQgwE6CwguEIAEELEDENQCOgUILhCABDoICAAQsQMQgwFQAFjoBmD5DGgAcAB4AIABXYgBjwKSAQEzmAEAoAEB&sclient=gws-wiz

#  general automation question