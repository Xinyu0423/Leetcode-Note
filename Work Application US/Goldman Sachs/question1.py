from distutils.util import change_root


def meanderingArray(unsorted):
    res=[None for _ in range(len(unsorted))]
    unsorted.sort()
    left=0
    right=len(unsorted)-1
    flag=True
    for i in range(len(unsorted)):
        if flag:
            res[i]=unsorted[right]
            right-=1
        else:
            res[i]=unsorted[left]
            left+=1
        if flag==True:
            flag=False
        else:
            flag=True
    return res

print(meanderingArray([-1,1,2,3,-5]))
