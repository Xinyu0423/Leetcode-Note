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
Similar question with 739
```
503. 下一个更大元素 II
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

示例 1:

输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数； 
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
注意: 输入数组的长度不会超过 10000。
```
Solution:
```
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[-1 for i in range(len(nums))]
        stack=[]
        for i in range(len(nums)*2):
            idx=i%len(nums)
            while stack and nums[stack[-1]]<nums[idx]:
                res[stack.pop(-1)]=nums[idx]
                
            stack.append(idx)
        return res
```