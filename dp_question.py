def dp_question(nums):
    if not nums:
        return 0
    dp=[1 for _ in range(len(nums))]
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[j]+1==nums[i]:
                dp[i]=dp[j]+1
    return max(dp)


print(dp_question([12,13,15,11,12,14]))
print(dp_question([1,2,3,5,2,3,4]))
print(dp_question([0,1,0,3,2,3]))