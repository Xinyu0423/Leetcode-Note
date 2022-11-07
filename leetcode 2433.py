def findArray(pref):
    from functools import reduce
    res=[pref[0]]
    for i in range(1,len(pref)):
        temp=reduce(lambda x, y: x ^ y, res)
        bin_length=temp-1
        for j in range(2**bin_length):
            if j^temp==pref[i]:
                res.append(j)
                break
    return res

print(findArray([580749,257475,683852,498321,554252,183734,902737,233091]))