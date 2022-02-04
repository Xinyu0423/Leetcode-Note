# Stack and Queue

## Stack
在list末尾添加元素，弹出list里最后一个元素

## Queue
在list末尾添加元素，弹出list里第一个元素

## 题目编号
1. 739


## Sample
```
739. 每日温度
请根据每日 气温 列表 temperatures ，请计算在每一天需要等几天才会有更高的温度。如果气温在这之后都不会升高，请在该位置用 0 来代替。

示例 1:

输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
示例 2:

输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]
示例 3:

输入: temperatures = [30,60,90]
输出: [1,1,0]

```
Solution:
```
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack=[]
        res=[0 for i in range(len(temperatures))]
        for idx, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<t:
                res[stack.pop(-1)]=idx-stack[-1]
            stack.append(idx)
        return res

```