# PythonTrick 

### By xiewm

---
1. **obj.name 通过点号dot访问属性时，实质上是Python 解释器内部自动调用\__getattribute__或\__getattr__魔法方法，两者的区别在于前者在任何情况下都会调用,后者是在使用getattribute 触发AttributeError异常时会去调用getattr，如果没有触发就会一直调用getattribute**

2. **obj[name] 通过key或者索引访问属性时，实质上Python 解释器内部自动调用\__getitem__**


3. **obj[name]=value**

4. **obj.name =value**