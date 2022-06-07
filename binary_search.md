# Binary Search(二分法)

## Note
1. 当right==middle时需要取左中位数
2. 当left==middle时需要取右中位数
3. 当无法获取数组的长度，并且需要找到target时，可以使用倍增法+二分查找(即当index小于target时，每次将index增长一倍)。ex：lintcode 447
4. 当要查询旋转后数组的最小值时，可以将nums[middle]和nums[right]比较，当nums[middle]>nums[right]时，更新left=middle+1(ex:Leetcode 153).当查询最大值时，比较nums[middle]<nums[right]。

## 模版
1. 左中位数
```
def binarySearch(nums,target):
    left=0
    right=len(nums)-1
    while left<right:
        middle=(left+right)//2
        # 取左中位数
        if nums[middle]<target:
            left=middle+1
        else:
            right=middle
    if nums[left]!=target:
        return -1
    else:
        return left
```
2. 右中位数
```
def binarySearch_version2(nums,target):
    left=0
    right=len(nums)-1
    while left<right:
        middle=(left+right+1)//2
        # 当left==midle时需要取右中位数
        if nums[middle]>target:
            right=middle-1
        else:
            left=middle
    if nums[left]!=target:
        return -1
    else:
        return left
```

## 降序二分法查找模版
1. 左中位数
```python
def binary_search(nums):
    left=0
    right=len(nums)-1
    while left<right:
        middle=(left+right)//2
        if nums[middle]>target:
            left=middle+1
        else:
            right=middle
    if nums[left]==target:
        return left
    else:
        return -1
```
2. 右中位数
```python
def binary_search(nums):
    left=0
    right=len(nums)-1
    while left<right:
        middle=(left+right+1)//2
        if nums[middle]<target:
            right=middle-1
        else:
            left=middle
    if nums[left]==target:
        return left
    else:
        return -1
```
   