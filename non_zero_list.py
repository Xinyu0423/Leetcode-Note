## 给定一个数组，查找数组中和 “不为0” 的所有子数组的个数

## 思路：
## 找和不为0的个数，可以先找出所有子数组的个数，然后用子数组的个数-和为0的数组的个数
## 和为0的数组的个数，可以通过数组中my_dict[s]出现的次数得到

def solution(nums):
    my_dict={0:1}
    s=0
    res=0
    index=0
    for i in nums:
        s+=i
        index+=1
        res+=index
        # print("res=",res)
        if s in my_dict:
            # print("here")
            res-=my_dict[s]
        if s not in my_dict:
            my_dict[s]=1
        else:
            my_dict[s]+=1
        
    return res

print(solution([-1,0,1]))
