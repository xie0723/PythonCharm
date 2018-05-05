- 背景

  装饰器模式是我经常使用的一种Python设计模式，也非常的好用，一般是用函数实现，但是这种实现有一个缺点。
  > 如果逻辑非常的复杂，写在一个函数中，会让函数非常长且冗余，需要把小功能的抽象，然后再进行组合 而类装饰器，就适用于这种场景。


```
# coding=utf-8
# 深入理解类装饰器


# 一：类装饰器(都不带参数)
class ClsDeco:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print(f'Running {self.func.__name__}')
        self.func()
        print('End')

@ClsDeco  # 等价于 bar = ClsDeco(bar)
def bar():
    print('do something')

# call bar()
# OUT:
#     Running bar
#     do something
#     End









# 二：类装饰器带参数
class ClsDeco1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, func, *args, **kwargs):
        print(f'Running {func.__name__}')
        print(f'Using x + y = {self.x + self.y}')
        return func


@ClsDeco1(1,2) # 等价于 bar1 = ClsDeco1(1,2)(bar1)
def bar1():
    print('do something')
    

# call bar1()
# OUT:
#     Running bar1
#     Using x + y = 3
#     do something









# 三：类装饰器不带参数，被包装对象带参数
class ClsDeco2:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'Running {self.func.__name__}')
        self.func(*args, **kwargs)
        print('End')

@ClsDeco2  # 等价于bar2 = ClsDeco2(bar2)
def bar2(a,b):
    print('do something')
    print(f'return a + b = {a + b}')


# bar2(1,2)
# OUT:
#     Running bar2
#     do something
#     return a + b = 3
#     End









# 四：类装饰器带参数且被装饰对象也带参数
class ClsDeco3:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, func, *args, **kwargs):
        print(f'Using x + y = {self.x + self.y}')

        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            print('Ending')

        return wrapper



@ClsDeco3(1, 2) # 等价于 bar3 = ClsDeco3(1, 2)(bar3)
def bar3(a, b):
    print('do something')
    print(f'return a + b = {a + b}')


# call bar3(1,2)
# OUT:
#     Using x + y = 3
#     do something
#     return a + b = 3
#     Ending





if __name__ == '__main__':
    bar3(1,2)

```

---
2018年03月30日 17:59:49
