2017年09月16日 16:44:23
---
##### **背景**
-  一个函数运行需要根据不同项目的配置，动态导入对应的配置文件运行。

##### **解决**
- 文件结构

> a
	│    a.py
	│\__init__.py
b
	│ b.py
	│\__init__.py
	│
	├─c
	│   c.py
	│  \__init__.py

- c.py 中内容
```python
args = {'a':1}

class C:
    
    def c(self):
        pass
```


	
- 目的
从a模块中导入c.py 中的对象

- 解决方案

``` python

import importlib

# 从b  module 导入c module中的c.py中的对象全部对象
params = importlib.import_module('b.c.c') #绝对导入
params1 = importlib.import_module('.c.c',package='b') #相对导入



# 对象中取出需要的对象
params.args #取出变量
params.C  #取出class C
params.C.c  #取出class C 中的c 函数
```





**以上就是动态函数import_module的使用方法**