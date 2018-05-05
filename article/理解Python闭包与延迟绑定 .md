2016年12月29日 11:45:45
---
> Python闭包可能会在面试或者是工作中经常碰到，而提到Python的延迟绑定，肯定就离不开闭包的理解，今天总结下 关于闭包的概念以及一个延迟绑定的面试题。

**Python闭包**

1.什么是闭包，闭包必须满足以下3个条件：

 - 必须是一个嵌套的函数。
 - 闭包必须返回嵌套函数。
 - 嵌套函数必须引用一个外部的非全局的局部自由变量。

举个栗子
```
# 嵌套函数但不是闭包
def nested():
	def nst():
		print('i am nested func %s' % nested.__name__)
	nst()

# 闭包函数
def closure():
	var = 'hello world' # 非全局局部变量

	def cloe():
		print(var) # 引用var

	return cloe # 返回内部函数


cl = closure()
cl()

```


----------


2.闭包优点

 - 避免使用全局变量
 - 可以提供部分数据的隐藏
 - 可以提供更优雅的面向对象实现

优点1,2 就不说了，很容易理解，关于第三个，例如当在一个类中实现的方法很少时，或者仅有一个方法时，就可以选择使用闭包。

举个栗子

```
# 用类实现一个加法的类是这样
class _Add(object):
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def add(self):
		return self.a + self.b

# 用闭包实现
def _Add(a):
	def add(b):
		return a + b

	return add	

ad = _Add(1) # 是不是很像类的实例化
print(ad(1)) # out:2
print(ad(2)) # out:3
print(ad(3)) # out:4
```

闭包的概念差不多就是这样了。

----------

**Python 延迟绑定**

*结合一个题目来说明：*

```
def multipliers():
    return [lambda x : i*x for i in range(4)]

print [m(2) for m in multipliers()] 

output:
# [6, 6, 6, 6]

```
其实这个题目，可能目的是想输出：[0, 2, 4, 6]，如何改进才能输出这个结果呢？

```
def multipliers():
	# 添加了一个默认参数i=i
    return [lambda x, i=i: i*x for i in range(4)]

print [m(2) for m in multipliers()] 

output:
# [0, 2, 4, 6]
```

multipliers就是一个闭包函数了

```
1.def multipliers():
2.    return [lambda x : i*x for i in range(4)]
3.	# multipliers内嵌套一个匿名函数
4.	# 该匿名函数引用外部非全局变量 i
5.	# 返回该嵌套函数
6.print [m(2) for m in multipliers()]
```
*下面来解释为什么输出结果是[6,6,6,6]。*

> 运行代码，代码从第6行开始运行，解释器碰到了一个列表解析，循环取multipliers()函数中的值，而multipliers()函数返回的是一个列表对象，这个列表中有4个元素，每个元素都是一个匿名函数（实际上说是4个匿名函数也不完全准确，其实是4个匿名函数计算后的值，因为后面for i 的循环不光循环了4次，同时提还提供了i的变量引用，等待4次循环结束后，i指向一个值i=3,这个时候，匿名函数才开始引用i=3，计算结果。所以就会出现[6,6,6,6]，因为匿名函数中的i并不是立即引用后面循环中的i值的，而是在运行嵌套函数的时候，才会查找i的值，这个特性也就是延迟绑定）

```
# 为了便于理解，你可以想象下multipliers内部是这样的(这个是伪代码，并不是准确的)：

def multipliers():
	return [lambda x: 3 * x, lambda x: 3 * x, lambda x: 3 * x, lambda x: 3 * x]
```
*因为Python解释器，遇到lambda（类似于def）,只是定义了一个匿名函数对象，并保存在内存中，只有等到调用这个匿名函数的时候，才会运行内部的表达式，而for i in range(4) 是另外一个表达式，需等待这个表达式运行结束后，才会开始运行lambda 函数，此时的i 指向3，x指向2*


----------
那我们来看下，添加了一个i=i，到底发生了什么？
```
def multipliers():
	# 添加了一个默认参数i=i
    return [lambda x, i=i: i*x for i in range(4)]
```

> 添加了一个i=i后，就给匿名函数，添加了一个默认参数，而python函数中的默认参数，是在python 解释器遇到def(i=i)或lambda 关键字时，就必须初始化默认参数，此时for i in range(4)，每循环一次，匿名函数的默认参数i，就需要找一次i的引用，i=0时，第一个匿名函数的默认参数值就是0，i=1时，第二个匿名函数的默认参数值就是1，以此类推。

```
# 为了便于理解，你可以想象下multipliers内部是这样的(这个是伪代码只是为了理解)：

def multipliers():
	return [lambda x,i=0: i*x, lambda x,i=1: i*x, lambda x,i=2: i*x, lambda x,i=3:i*x i=3]
# x的引用是2 所以output的结果就是：[0,2,4,6]
```

当然你的i=i，也可以改成a=i。

```
def multipliers():
	return [lambda x，a=i: a * x for i in range(4)]
```

Python的延迟绑定其实就是只有当运行嵌套函数的时候，才会引用外部变量i，不运行的时候，并不是会去找i的值，这个就是第一个函数，为什么输出的结果是[6,6,6,6]的原因。


----------
**以上就是自己对于Python闭包和延迟绑定的理解。**

