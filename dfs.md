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

### Backtracking Sample
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

### BFS/DFS Sample
### 题目编号 200
```
200. 岛屿数量
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
```
Solution:
```
# BFS
        row=len(grid)
        col=len(grid[0])
        count=0
        if row==0 or col==0:
            return 0
        queue=[]
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    queue.append((i,j))
                    grid[i][j]="0"
                    while queue:
                        cur_i,cur_j=queue.pop(0)
                        for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                            temp_i=x+cur_i
                            temp_j=y+cur_j
                            if 0<=temp_i<row and 0<=temp_j<col and grid[temp_i][temp_j]=="1":
                                queue.append((temp_i,temp_j))
                                grid[temp_i][temp_j]="0"
                    count+=1
        return count
```

```
# DFS
        def dfs(grid,i,j):
            if 0<=i<row and 0<=j<col and grid[i][j]=='1':
                grid[i][j]='0'
                dfs(grid,i+1,j)
                dfs(grid,i-1,j)
                dfs(grid,i,j+1)
                dfs(grid,i,j-1)

        if not grid:
            return 0
        row=len(grid)
        col=len(grid[0])
        count=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    dfs(grid,i,j)
                    count+=1
        return count
```
