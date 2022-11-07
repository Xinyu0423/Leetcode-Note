def question2(a,b):
    from collections import Counter
    res=[]
    for i in range(len(a)):
        if len(a[i])==len(b[i]):
            counter_ai=Counter(a[i])
            counter_bi=Counter(b[i])
            count=0
            for i in counter_ai:
                if i in counter_bi:
                    counter_bi[i]-=1
                    if counter_bi[i]==0:
                        del counter_bi[i]
                else:
                    count+=1
            res.append(count)            
        else:
            res.append(-1)
    return res



print(question2(['tea','tea','act'],['ate','toe','acts']))
print(question2(['a','jk','abb','mn','abc'],['bb','kj','bbc','op','def']))