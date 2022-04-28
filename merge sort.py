def merge_sort(nums):
    if len(nums)==1:
        return nums
    middle=len(nums)//2
    left_boundary=merge_sort(nums[:middle])
    right_boundary=merge_sort(nums[middle:])
    res=[]
    left_index=0
    right_index=0
    [3,5,7]
    [1,6,9,10]
    while left_index!=len(left_boundary) and right_index!=len(right_boundary):
        if left_boundary[left_index]<right_boundary[right_index]:
            res.append(left_boundary[left_index])
            left_index+=1
        else:
            res.append(right_boundary[right_index])
            right_index+=1
    res+=left_boundary[left_index:]
    res+=right_boundary[right_index:]
    return res

        