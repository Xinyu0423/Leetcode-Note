def split_list(nums,temp_nums,left,right):
    if left<right:
        middle=(left+right)//2
        split_list(nums,temp_nums,left,middle)
        split_list(nums,temp_nums,middle+1,right)
        merge_list(nums,temp_nums,left,middle,right)

def merge_list(nums,temp_nums,left,middle,right):
    l_pos=left
    r_pos=middle+1
    pos=left
    # 合并
    while l_pos<=middle and r_pos<=right:
        if nums[l_pos]<nums[r_pos]:  
            temp_nums[pos]=nums[l_pos]
            pos+=1
            l_pos+=1
        else:  
            temp_nums[pos]=nums[r_pos]
            pos+=1
            r_pos+=1
    # 合并左区剩余元素
    while l_pos<=middle:
        temp_nums[pos]=nums[l_pos]
        pos+=1
        l_pos+=1
    # 合并右半区剩余元素
    while r_pos<=right:
        temp_nums[pos]=nums[r_pos]
        pos+=1
        r_pos+=1

    # 把临时数组中合并后的元素放回原数组中
    while left<=right:
        nums[left]=temp_nums[left]
        left+=1

def merge_sort(nums):
    temp_nums=[0 for _ in range(len(nums))]
    split_list(nums,temp_nums,0,len(nums)-1)
    return nums

nums=[2,5,3,7,1,3,4,3,3]
print(merge_sort(nums))

