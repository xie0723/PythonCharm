2016年06月16日 16:29:55
---
怎样找出一个序列中出现次数最多的元素呢？

1：超极简单的方法
```python
from collections import Counter

words = [
	'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
	'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
	'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
	'my', 'eyes', "you're", 'under'
]

print(Counter(words))
#OUT
# Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2, "you're": 1, "don't": 1, 'under': 1, 'not': 1})


print (Counter(words).most_common(4))
#OUT
# [('eyes', 8), ('the', 5), ('look', 4), ('into', 3)]
```

2：稍微复杂的

```  python
words = [
	'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
	'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
	'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
	'my', 'eyes', "you're", 'under'
]

dict_num = {}
for item in words:
	if item not in dict_num.keys():
		dict_num[item] = words.count(item)

print (dict_num)

# 未做排序
# {"you're": 1, 'eyes': 8, 'look': 4, "don't": 1, 'into': 3, 'under': 1, 'not': 1, 'the': 5, 'my': 3, 'around': 2}

# 排序
import operator
sorted(dict_num.items(),key=operator.itemgetter(1))

#OUT
#[('not', 1),("don't", 1),("you're", 1),('under', 1),('around', 2),('into', 3),('my', 3),('look', 4),('the', 5),('eyes', 8)]
```

3：字典推导
```python
words = [
	'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
	'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
	'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
	'my', 'eyes', "you're", 'under'
]


dict_num = dict_num = {i:words.count(i) for i in set(words)}

```

