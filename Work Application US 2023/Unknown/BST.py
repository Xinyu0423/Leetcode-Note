class BST:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value

    def insert(self,value):
        if value<self.value:
            if not self.left:
                self.left=BST(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right=BST(value)
            else:
                self.right.insert(value)
        return self

def insertArray(arr):
    currNode=BST(arr[0])
    for i in range(1,len(arr)):
        currNode.insert(arr[i])
    return currNode

tree_value=[]
def printTree(root):
    if not root:
        return
    printTree(root.left)
    printTree(root.right)
    tree_value.append(root.value)
    return tree_value
myNode=insertArray([3,10,5,2,7,6,11] )
printTree(myNode)
print(tree_value)

