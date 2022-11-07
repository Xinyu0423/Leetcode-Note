# SQL Note

## Group by
1. 通常来说，count,sum, max, min（聚合函数）需要和group by搭配使用
2. 在使用group by时，select中只能包含group by的涉及的字段，或者把不涉及的字段放入聚合函数
3. group by经常用作去重


## Where和having的区别
1. where在是用group by时，必须写在group by后面（代码后面）
2. having是group by执行后，对group by执行后的table的where
3. 在实际应用中，尽量不要使用having，尽量在where中过滤掉，having会增加查询时间

## SQL写法规范
Select name
      ,age
      ,salary
from
      t1

## Case when
1. 类似if, elif, else,最后可以使用and（else)，如果有匹配，则变为匹配值，否则变为null

## 子查询(subquery)
1. 在使用子查询时需要对子查询的表哥起别名

Show all users, ordering by their name, with a location, showing the location name, and the parent location name for their location. If there is no parentLocation, show "None" in parentLocationName column.