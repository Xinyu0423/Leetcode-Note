# Tree

## 二叉树的四种遍历方式
1. 前序遍历
2. 中序遍历
3. 后序遍历
4. 层序遍历

## 树中用dfs通常用stack实现

## 树中用bfs通常用queue实现

## Question
1. Tree
   1. 107,103,101,110,104,951(TO_DO)
2. 110为什么不能用while
3. 104这个代码是什么意思
4. 713,424(滑动窗口)
5. 
```
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

## Procedure Doing Tree Questions（recursion）:
1. 判断树的根是否存在（Base Case）

   
### 前序遍历(Preorder Traversal)
前序遍历的顺序为 `根节点->左子树->右子树`
```
144. 二叉树的前序遍历
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

 

示例 1：


输入：root = [1,null,2,3]
输出：[1,2,3]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：


输入：root = [1,2]
输出：[1,2]
示例 5：


输入：root = [1,null,2]
输出：[1,2]
```
递归写法
```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        def traversal(root):
            if not root:
                return None
            res.append(root.val)
            traversal(root.left)
            traversal(root.right)
        
        traversal(root)
        return res
        
```
迭代写法
```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack=[root]
        res=[]
        while stack:
            root=stack.pop()
            if root:
                res.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return res 
```

### 中序遍历(Inorder Traversal)
中序遍历的顺序为`左子树->根节点->右子树`
```
94. 二叉树的中序遍历
给定一个二叉树的根节点 root ，返回它的 中序 遍历。

 

示例 1：


输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：


输入：root = [1,2]
输出：[2,1]
示例 5：


输入：root = [1,null,2]
输出：[1,2]

```

递归写法
```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 递归写法
        res=[]
        def traversal(root):
            if not root:
                return None
            traversal(root.left)
            res.append(root.val)
            traversal(root.right)
        traversal(root)
        return res  
```
迭代写法
```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 迭代写法
        stack=[]
        cur=root
        res=[]
        if root==None:
            return []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur=cur.left
            pop_node=stack.pop()
            res.append(pop_node.val)
            cur=pop_node.right
        return res
```

### 后序遍历
后序遍历的顺序为`左子树-右子树-跟节点`
```
145. 二叉树的后序遍历
给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。

 

示例 1：


输入：root = [1,null,2,3]
输出：[3,2,1]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
```
递归写法
```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 递归写法
        res=[]
        def traversal(root):
            if root==None:
                return
            traversal(root.left)
            traversal(root.right)
            res.append(root.val)
        traversal(root)
        return res
```
迭代写法
```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 迭代写法
        stack=[root]
        res=[]
        if root is None:
            return []
        while stack:
            pop_node=stack.pop()
            res.append(pop_node.val)
            if pop_node.left is not None:
                stack.append(pop_node.left)
            if pop_node.right is not None:
                stack.append(pop_node.right)
        return res[::-1]
```

### 层序遍历
层序遍历的顺序为`逐层遍历`
`TO DO`
