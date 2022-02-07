# 滑动窗口(Sliding Window)

## 题目编号
1. 28

# 滑动窗口的类型
1. 定长的窗口
2. 收缩的
3. 不定长的滑窗

## TBD:
1. 3,76(Ignore for now),209,904,1004
2. 930,992,1248

## 定长滑动窗口Sample
1. 
```
28. 实现 strStr()
实现 strStr() 函数。

给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

 

说明：

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

 

示例 1：

输入：haystack = "hello", needle = "ll"
输出：2
示例 2：

输入：haystack = "aaaaa", needle = "bba"
输出：-1
示例 3：

输入：haystack = "", needle = ""
输出：0
 
```
Solution:
```
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        start=0
        if needle=="":
            return 0
        for end in range(len(needle),len(haystack)+1):
            # print(haystack[start:end])
            if haystack[start:end]==needle:
                return start
            else:
                start+=1
        return -1
```
2. 和28题基本相同，567题在if比较时需要比较排列（使用Counter），28题是直接进行比较。
```
567. 字符串的排列
给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。

换句话说，s1 的排列之一是 s2 的 子串 。

 

示例 1：

输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").
示例 2：

输入：s1= "ab" s2 = "eidboaoo"
输出：false
```
   
```
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        start=0
        counter_s1=Counter(s1)
        for end in range(len(s1),len(s2)+1):
            # print("end=",end)
            # print(s2[start:end])
            if Counter(s2[start:end])== counter_s1:
                return True
            else:
                start+=1
        return False
```