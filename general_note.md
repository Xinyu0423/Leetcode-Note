# General Note

## 反转字符串

```
a="abcdef"
print("a=",a)
res_a=a[::-1]
print("res_a=",res_a)
```
('a=', 'abcdef')  
('res_a=', 'fedcba')

## Join
 join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串  
 ```
 mylist=['a','b','c']
 mystr=''.join(mylist)
 print("mystr=",mystr)
 ```
 ('mystr=', 'abc')

 ## 去除string的标点
```
exclude = set(string.punctuation)
s = ''.join(ch for ch in s if ch not in exclude)
```
 