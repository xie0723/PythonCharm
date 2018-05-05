2016年08月24日 16:51:59
---
> 在学习RF自定义关键字的时候，网上看到有些不够详细，最重要的是没有debug过程，这篇记录下自己在写关键字时候的除错过程。

**1：**
> 在C:\Python27\Lib\site-packages\ 文件夹下， 新建python package文件夹 ，例如我的是ATestLibrary
> 建好后的完整路径：C:\Python27\Lib\site-packages\ATestLibrary\

*（Tips：我的python 是安装在C盘，在创建时，要根据自己的安装路径选择）*

**2：**
> 在C:\Python27\Lib\site-packages\ATestLibrary\  文件夹下查看是否有\__init__.py 文件，若没有新建\__init__.py(空内容文件）。
> 建好后的完整路径：C:\Python27\Lib\site-packages\ATestLibrary\\__init__.py

**3：**

> 在C:\Python27\Lib\site-packages\ATestLibrary\ 文件夹下，新建自己的moudle，例如我的是test_RF_import.py

代码demo：

test_RF_import.py
```python
class myKeyWords(object):
	def __init__(self):
		pass

	def my_key_word(self):
		print ('this is my key word')
```


**4：**
>  C:\Python27\Lib\site-packages\ATestLibrary\\__init__.py  修改该文件内容为

\__init__.py 
```python
# -*- coding: utf-8 -*-
from test_RF_import import myKeyWords

class ATestLibrary(myKeyWords):
	ROBOT_LIBRARY_SCOPE = 'GLOBAL'
```

```python

# 特别注意：
在__init__.py文件中，创建class 时，类名必须和自己的库文件夹名称相同。
例如我的类名称是ATestLibrary，而创建的库文件夹名也是ATestLibrary→C:\Python27\Lib\sitepackages\ATestLibrary 
```


**5：**

> 在robotframework 中，点击Library 导入自定义库
> 导入自定义库文件ATestLibrary，正确时为灰色字体（导入库文件，就不需要说明了）
> 运行结果:

```python
Starting test: BetaInterfaceTest xiewm.Testcase.Test My Key Word.test_my_key_word
20160824 16:22:23.640 :  INFO : this is my key word
Ending test:   BetaInterfaceTest xiewm.Testcase.Test My Key Word.test_my_key_word
```


----------
完整的文件结构应该是这样：
ATestLibrary
				-------    \__init__.py
				-------    test_RF_import.py
		
----------


以下自己遇到的一些问题的debug
**1：**尽量在文件的开头加上：# -*- coding: utf-8 -*-,因为python默认编码是ascii，所以如果代码中有()，或中文等等符号，会报错，提示编码不正确

**2：**如果写的代码里边有中文，尽量在文件开头加上以下3行代码

```python
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
```
**3：**如果在初始化函数中，定义了形参。则必须在导入库的时候，也要提供对应的参数。
不然会提示少给了变量的报错。

```python
def __init__(self,a,b):
	pass
```
![这里写图片描述](http://img.blog.csdn.net/20160824164951186)


**4:**
修改代码后，及时把对应的.pyc文件删除并且重启下robotframework 后，再导入。

**5：**如果还是有其他的报错，请点击Tools→View RIDE log ，查看并debug。


----------
**就总结这么多，如果还有遇到什么问题，会继续补充。**