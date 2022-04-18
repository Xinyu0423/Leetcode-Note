from cmath import pi
import random


def quick_sort(nums,head,tail):
    if head>=tail:
        return nums
    random_index = random.randint(head,tail)
    nums[random_index], nums[head] = nums[head], nums[random_index]
    pivot = nums[head]
    
    # pivot=nums[random.randint(head,tail)]
    low=head
    high=tail
    while low!=high:
        while low<high and nums[high]>=pivot:
            high-=1
        nums[low]=nums[high]
        while low<high and nums[low]<pivot:
            low+=1
        nums[high]=nums[low]
    nums[high]=pivot
    quick_sort(nums,head,low-1)
    quick_sort(nums,low+1,tail)
    return nums

nums=[3,1,2,5,4,2]
nums=[1,2,1]
head=0
tail=len(nums)-1
print(quick_sort(nums,head,tail))
print(random.randint(1,1))
    
    

        
        
