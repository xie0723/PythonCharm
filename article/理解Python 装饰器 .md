2017年02月23日 14:29:44
---

**装饰器应该是我学习Python时，第一个遇到的难题，当时看了很多教程，最终理解并在工作中使用，是stackoverflow这篇文章**：[stackoverflow装饰器](http://stackoverflow.com/questions/739654/how-to-make-a-chain-of-function-decorators)

网上有很多大神的装饰器教程，写这篇文章是增强记忆，也是自己的理解。

 


----------


 **1.** Python 一切皆对象

> 这句话很好明白，但是在真正写代码的时候理解使用却很难，既然Python中一切皆对象，那函数肯定也是可以作为对象传递的。

举个栗子。
``` python
# 普通的函数
In[2]: def add(a, b):
  ...: 	return a + b
  ...: 
In[3]: add(1, 2)
Out[3]: 3

# 接收函数作为参数
In[3]: def foo(func,a,b):
  ...: 	return func(a,b)
  ...: 
In[4]: foo(add,1,2)
Out[4]: 3

# 有一个地方挺有趣的，传参时，为什么传递的是func，而不是直接传递func()，试试看。
In[5]: def bar(func(),a,b):
  File "<ipython-input-5-f09913042048>", line 1
    def bar(func(),a,b):
                ^
SyntaxError: invalid syntax
# 语法错误，无效语法。为什么呢？因为使用func()，是直接执行函数内部的表达式了，这也是func 与func()的区别。

```
*其实我们平常听到：回调函数，和以上的使用差不多：函数当做参数。*


----------


**2 .**理解了Python中一切皆对象后。我们看下装饰器。

> 装饰器：装饰器是一种设计模式，经常被用于有切面需求的场景，较为经典的有插入日志、性能测试、事务处理等。装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量函数中与函数功能本身无关的雷同代码并继续重用。概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。

**以上是概念解释，我自己比较通俗的理解：它其实就是在包装函数的前or后or前后增加一些额外功能代码。**


----------


> @语法糖：**使用@符号来装饰函数，其效果等同于先以该函数为参数，调用装饰器，然后把装饰器所返回的结果，赋给同一个作用域中与原函数同名的变量→func=deco(func)**

 - 举个栗子

```python
def foo():
	print('foo')
	
# 例如想在foo函数前加上一些功能，但是不能修改foo函数本身的代码。

In[3]: def bar(func):
  ...: 	print('start') 
  ...: 	func()
  ...: 	
In[4]: @bar
  ...: def foo():
  ...: 	print('foo')
  ...: 	
Out[5]: start
		foo
		
# 如果想在后面加呢？
In[5]: def bar(func):
  ...: 	func()
  ...: 	print('end')
  ...: 	
In[6]: @bar
  ...: def foo():
  ...: 	print('foo')
  ...: 	
Out[7]:foo
	   end
	   
# 在前后呢？
In[7]: def bar(func):
  ...: 	print('start')
  ...: 	func()
  ...: 	print('end')
  
In[8]: @bar
  ...: def foo():
  ...: 	print('foo')
  ...: 	
Out[9]:	start
		foo
		end
		
# 这样就满足了我们不改变原有函数的基础上，添加了额外的功能。
```

 - 简单理解装饰器是怎么回事后，我们实现一个功能：性能测试

```python
In[3]: import time

# ①
In[4]: def timeit(func):
  ...: 	start = time.time()
  ...: 	func()
  ...: 	end = time.time()
  ...: 	print 'cost:{}'.format(end - start)
  ...: 	
In[5]: @timeit
  ...: def bar(): #不需要调用bar()
  ...: 	sum(range(1000000))
  ...: 	
  
Out[6]:
	  cost:0.095999956131
	  
# 这和我们在网上看到的装饰器教程写法不太一样。一般是下面这种写法。

# ②
In[2]: 
  ...: def timeit(func):
  ...: 	def wrapper():
  ...: 		start = time.time()
  ...: 		func()
  ...: 		end = time.time()
  ...: 		print 'cost:{}'.format(end - start)
  ...: 	return wrapper
  ...: 
In[3]: @timeit
  ...: def bar():
  ...: 	sum(range(1000000))
  ...: 	
In[5]: bar() # 需要调用bar（）
Out[6]:
	   cost:0.0629999637604	  
```

*分析第二种写法*

>  - 该函数接收一个函数func 作为参数。
>  - 往下执行遇到wrapper函数。
>  - 在func()函数前后，执行time()函数，获取时间。
>  - 最后返回内嵌的函数wrapper
>  
>  和方法1区别是：方法2在包装函数func后，返回一个有额外功能的新函数，我们在调用bar()函数时,可以不严谨的理解为是调用了wrapper()函数（实际上呢，新函数名字还是bar），因为@的语法糖，timeit(bar)返回一个wrpper函数对象，这个wrapper对象，又传递给bar，等价于  bar = timeit(bar)，），这样新函数可以在任何地方被调用。
>  而方法1，是直接执行了timeit内的表达式，而无法返回一个函数对象。所以我们一般使用第二种方式，以便我们可以随时随地调用新函数。





**3 .**  装饰器的扩展

- 装饰有参数的函数

```python
In[6]: def deco(func):
  ...: 	def wrapper(a,b):
  ...: 		print 'start'
  ...: 		result = func(a, b)
  ...: 		print 'end'
  ...: 		return result
  ...: 	return wrapper
  ...: 
In[7]: @deco
  ...: def add(a,b):
  ...: 	return a + b
  ...: 
In[8]: add(1,2)
Out[8]: 
		start
		end
		3

```

- 装饰不定参数的函数
 

```python
		
In[11]: def deco(func):
   ...: 	def wrapper(*args, **kwargs):
   ...: 		result = func(*args, **kwargs)
   ...: 		return result
   ...: 	return wrapper

```


- 装饰器带参数

```python
# 在最外层包装了一层函数,用来接收参数。

In[13]: def deco(var):
   ...: 	print var
   ...: 	def _deco(func):
   ...: 		def wrapper():
   ...: 			func()
   ...: 		return wrapper
   ...: 	return _deco

```

- 装饰器装饰类

```python
# 典型例子就是单例模式。

In[14]: def singleton(cls):
   ...: 	instance = {}
   ...: 
   ...: 	def wrapper(*args, **kwargs):
   ...: 		if cls not in instance:
   ...: 			instance[cls] = cls(*args, **kwargs)
   ...: 		return instance[cls]
   ...: 
   ...: 	return wrapper
   ...: 
   ...: 
   ...: @singleton
   ...: class Foo(object):
   ...: 	pass
```

- 装饰器装饰 类方法

```python
In[7]: def deco(func):
  ...: 	def wrapper(self):
  ...: 		print 'wrapper'
  ...: 		func(self)
  ...: 	return wrapper
  ...: 
In[8]: class MyClass(object):
  ...: 	@deco
  ...: 	def foo(self):
  ...: 		print 'foo'
  ...: 		
In[9]: mycls = MyClass()
In[10]: mycls.foo()
Out[11]:
		wrapper
		foo
```


- 类装饰器装饰函数

```python

In[15]: class Foo(object):
   ...: 	def __init__(self, func):
   ...: 		self.func = func
   ...: 
   ...: 	def __call__(self, *args, **kwargs):
   ...: 		print 'start'
   ...: 		self.func(*args, **kwargs)
   ...: 		print 'end'
   ...: 
   ...: 
   ...: @Foo
   ...: def bar():
   ...: 	print 'bar'
```

- 类装饰器 带参数，装饰函数

```python
In[7]: class Bar(object):
  ...: 	def __init__(self, arg):
  ...: 		self.arg = arg
  ...: 	def __call__(self,func , *args, **kwargs):
  ...: 		print self.arg
  ...: 		print 'start'
  ...: 		func(*args ,**kwargs)
  ...: 		print 'end'
  ...: 		
In[8]: @Bar('xwm')
  ...: def foo():
  ...: 	print 'foo'
  ...: 
Out[9]:	
		xwm
		start
		foo
		end

```

- 嵌套装饰器

```python
In[2]: def deco1(func):
  ...: 	def wrapper():
  ...: 		print 'deco1'
  ...: 		func()
  ...: 		print 'deco1'
  ...: 	return wrapper
  ...: 
  
In[4]: def deco2(func):
  ...: 	def wrapper():
  ...: 		print 'deco2'
  ...: 		func()
  ...: 		print 'deco2'
  ...: 	return wrapper
  ...: 
  
In[5]: def deco3(func):
  ...: 	def wrapper():
  ...: 		print 'deco3'
  ...: 		func()
  ...: 		print 'deco3'
  ...: 	return wrapper
  ...: 
In[6]: 
In[6]: @deco1
  ...: @deco2
  ...: @deco3
  ...: def foo():
  ...: 	print 'foo'
  ...: 	
In[7]: foo()
Out[8]:
		deco1
		deco2
		deco3
		foo
		deco3
		deco2
		deco1
# 执行顺序从里到外，先调用最里层的装饰器，依次往外层调用装饰器 deco3→deco2→deco1
```


PS：一般为了保留被装饰函数的元信息，需要结合functools模块的wraps，wraps本身也是一个装饰器，它会保留元函数信息。

- 装饰器保存元信息

```python
In[8]: from functools import wraps
In[9]: def deco(func):
   ...: 	@wraps
   ...: 	def wrapper():
   ...: 		func()
   ...: 	return wrapper	
```


> 其实难理解的是函数内部嵌套函数，因为人类大脑习惯线性思考，可以考虑，把里边的def wrapp()：这句代码直接消失掉。再去看整体代码。

```python
def deco3(func):
	# def wrapper():   想象不存在这行代码，最后这个函数deco3返回的是一个含有被装饰的函数foo()功能的新函数，并且新函数的名字还是被装饰的函数foo().
		print 'deco3'
		func()
		print 'deco3'
	return wrapper

```

----------


**以上就是自己对于装饰器的小白理解，了解后，在工作中会经常使用到，至于效果，谁用谁知道，^_^**

