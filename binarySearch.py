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

print(binarySearch([2,3,5,7,9],11))
print(binarySearch([2,3,5,7,9],3))
print(binarySearch([2,3,5,7,9],7))
print(binarySearch([2,3,5,7,9],2))
print(binarySearch([2,3,5,7,9],9))

print(binarySearch_version2([2,3,5,7,9],11))
print(binarySearch_version2([2,3,5,7,9],3))
print(binarySearch_version2([2,3,5,7,9],7))
print(binarySearch_version2([2,3,5,7,9],2))
print(binarySearch_version2([2,3,5,7,9],9))
