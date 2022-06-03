# Bit Operation

## 位运算找唯一的数
1. 将所有数并(异或）起来，消除重复的数

## 找到2个异或的不同点 (找到异或结果中为1的那一位)
1. 因为已经有异或的结果，构造bit=1
2. 通过把异或的结果和bit与(and &)，当结果为0时，向左移一位("<<")，直到结果不为0(注意不为0不代表结果是1)

## 异或
1. 两个相同的数异或得0

## 通过两个数异或得到 该数的值
```
260. Single Number III
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]
```
```python
def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res_xor=0
        for i in nums:
            res_xor^=i
        bit=1
        while bit& res_xor==0:
            bit<<=1
        resA=0
        resB=0
        for i in nums:
            if i&bit==0:
                resA^=i
            else:
                resB^=i
        return [resA,resB]
```

## 将十进制的数转为2/7/16进制
1. 可以通过取余的方式，将数转为2/7/16进制
2. 最后将取余后的结果反向输出([::-1])，即可得到专为2/7/16进制的结果
例：将数转为7进制
```
504. Base 7
Given an integer num, return a string of its base 7 representation.

 

Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"
 

Constraints:

-107 <= num <= 107
```
```python
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return "0"
        res=""
        flag=False
        # 负数整除7，在除不尽的情况下永远等于-1,所以将它转为正数
        if num<0:
            flag=True
            num*=-1
        
        while num!=0:
            res=res+str((num%7))
            num//=7
        if flag:
            return "-"+res[::-1]
        else:
            return res[::-1]
```

## Note
1. 负数整除7，在除不尽的情况下永远等于-1
2. 3<sup>13</sup>=3<sup>(1011)_2</sup>=3<sup>2^3</sup>*3<sup>2^1</sup>*3<sup>2^0</sup>,即可以通过将幂转化为2进制，通过2进制相乘来防止数字溢出
3. 当num为负数时，可以通过num=(2^32)+num获得其负数的编码，此操作称为补码(2**32+num)

