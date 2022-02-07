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

## Questions
1. 问题超时(1176)
2. 为什么不直接用len(s[start:end])查看窗口长度，而使用end-start+1

## 获取窗口的长度
```
窗口长度=end-start+1
```

## 定长滑动窗口Sample
1. 标准定长滑动窗口类问题
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
3. 和前两题基本相同，卡出长度为3的字符串，然后使用Counter的长度是否为3查看是否存在重复元素。
```
1876. 长度为三且各字符不同的子字符串
如果一个字符串不含有任何重复字符，我们称这个字符串为 好 字符串。

给你一个字符串 s ，请你返回 s 中长度为 3 的 好子字符串 的数量。

注意，如果相同的好子字符串出现多次，每一次都应该被记入答案之中。

子字符串 是一个字符串中连续的字符序列。

 

示例 1：

输入：s = "xyzzaz"
输出：1
解释：总共有 4 个长度为 3 的子字符串："xyz"，"yzz"，"zza" 和 "zaz" 。
唯一的长度为 3 的好子字符串是 "xyz" 。
示例 2：

输入：s = "aababcabc"
输出：4
解释：总共有 7 个长度为 3 的子字符串："aab"，"aba"，"bab"，"abc"，"bca"，"cab" 和 "abc" 。
好子字符串包括 "abc"，"bca"，"cab" 和 "abc" 。
```
```
class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        start=0
        count=0
        for end in range(3,len(s)+1):
            #print(s[start:end])
            if len(Counter(s[start:end]))==3:
                count+=1
            start+=1
        return count
```

## 不定长滑动窗口Sample
1. 注意"[]"是左开右闭的（不能取到最后一个），所以for循环需要+1
```
1. 无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0
```
```
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start=0
        count=0
        for end in range(len(s)+1):
            # print(s[start:end])
            # print("length set=",len(set(s[start:end])))
            # print("length=",len(s[start:end]))
            if len(set(s[start:end]))==len(s[start:end]):
                count=max(count,len(s[start:end]))
            else:
                start+=1
        return count
```
2. 找到符合条件的窗口后，需要使用while不断缩小窗口
```
209. 长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

 

示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：

输入：target = 4, nums = [1,4,4]
输出：1
示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
```
```
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        start=0
        res=float("inf")
        for end in range(len(nums)+1):
           
            while sum(nums[start:end])>=target:
                res=min(res,len(nums[start:end]))
                start+=1
        if res==float("inf"):
            return 0
        return res
```

