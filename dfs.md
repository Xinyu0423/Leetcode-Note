# BFS/DFS/Backtracking刷题笔记

## 题目编号
1. 994
2. 200
3. 695
4. 1091
5. 46
6. 47
7. 39
8. 40
9. 216

## BackTracking本质是一种暴力求解的算法，因此需要消耗大量空间

## 通常找到所有路径/排列，都可以使用BrackTracking的思想

## BackTracking模版
1. 设置现场
2. DFS
3. 回复现场

### Sample
#### 题目编号 216
```
216. 组合总和 III
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
```
Solution:
```
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(start_index,k,n,path,res):
            if k==0 and n==0:
                res.append(copy.deepcopy(path))
                
            # if (k!=0 and n==0) or (k==0 and n!=0):
            #     return
            for i in range(start_index,10):
                if i<=n: 
                    path.append(i)
                    #设置现场
                    dfs(i+1,k-1,n-i,path,res) #DFS
                    path.pop() #恢复现场
        start_index=1
        path=[]
        res=[]
        dfs(start_index,k,n,path,res)
        return res
```
