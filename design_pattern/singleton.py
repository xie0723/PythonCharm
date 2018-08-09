# -*- coding: utf-8 -*-
__Author__ = "xiewm"
__Date__ = '2018/3/29 11:33'

from functools import wraps



# 1 装饰器模式
def singleton(cls):
    inst = None
    
    @wraps(cls)
    def wrapper(*args, **kwargs):
        nonlocal inst
        if inst is None:
            inst = cls(*args, **kwargs)
        return inst
    
    return wrapper



# 2 基类
class Singleton:
    inst = None
    
    def __new__(cls, *args, **kwargs):
        if not cls.inst:
            cls.inst = super().__new__(cls, *args, **kwargs)
        
        return cls.inst



@singleton
class Base:
    pass



if __name__ == '__main__':
    b1 = Base()
    b2 = Base()
    
    print(b1 is b2)
