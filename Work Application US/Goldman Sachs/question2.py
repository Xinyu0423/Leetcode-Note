def countPairs(numbers,k):
    def swap(a,b):
        if a<b:
            return tuple([a,b])
        else:
            return tuple([b,a])
    my_dict={}
    for i in numbers:
        if i not in my_dict:
            my_dict[i]=1
        else:
            my_dict[i]+=1
    pair_dict={}
    for n, count in my_dict.items():
        if k==0 and count>1:
            pair_dict[tuple(n,n)]=True
        else:
            if n+k in my_dict:
                pair_dict[swap(n,n+k)]=True
            if n-k in my_dict:
                pair_dict[swap(n,n-k)]=True
    return len(pair_dict)

print(countPairs([1,1,1,2],1))
    