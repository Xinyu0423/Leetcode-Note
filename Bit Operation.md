# Bit Operation

## 位运算找唯一的数
1. 将所有数并(异或）起来，消除重复的数

## 找到2个异或的不同点 (找到异或结果中为1的那一位)
1. 因为已经有异或的结果，构造bit=1
2. 通过把异或的结果和bit与(and &)，当结果为0时，向左移一位("<<")，直到结果不为0(注意不为0不代表结果是1)

## 异或
1. 两个相同的数异或得0

## 通过两个数异或得到 该数的值
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

