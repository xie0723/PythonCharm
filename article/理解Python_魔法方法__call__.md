## 概述：
> Python有很多内置魔法方法，一般表现为双下划线开头和结尾。例如 \__name__、\__doc__、\__new__、\__init__、\__call__等，这些魔法方法会让对象持有特殊行为，今天就介绍，自己平时使用比较多的\__call__，我称它为：实例魔法方法。

##使用方式
> 什么叫实例魔法方法呢？，就是它可以把类实例当做函数调用。


## 举个栗子

```
class Bar:
    def __call__(self, *args, **kwargs):
        print('i am instance method')
        
b = Bar()  # 实例化
b()  # 实例对象b 可以作为函数调用 等同于b.__call__ 使用


# OUT: i am instance method



# 带参数的类装饰器
class Bar:

    def __init__(self, p1):
        self.p1 = p1

    def __call__(self, func):
        def wrapper():
            print("Starting", func.__name__)
            print("p1=", self.p1)
            func()
            print("Ending", func.__name__)
        return wrapper


@Bar("foo bar")
def hello():
    print("Hello")

# 上面的语法糖写法 等价于 hello = Bar('foo bar')(hello)

if __name__ == "__main__":
    hello()

#OUT
	Starting hello
	p1= foo bar
	Hello
	Ending hello


```


## 执行
>  实例变为可调用对象，与普通函数一致，执行的逻辑是__call__ 函数内部逻辑。

## 优点

- 代码逻辑很复杂时，不适合写成一个函数内，会封装成类，调用该类对象时，我们直接使用实例作为函数引用，更方便简洁.
- 通过__call__ 实现类装饰器.






---
2018年03月14日 16:42:07
