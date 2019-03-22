```
# 简单查询
print(session.query(User).all())
print(session.query(User.name, User.fullname).all())
print(session.query(User, User.name).all())

# 带条件查询
print(session.query(User).filter_by(name='user1').all())
print(session.query(User).filter(User.name == "user").all())
print(session.query(User).filter(User.name.like("user%")).all())

# 多条件查询
print(session.query(User).filter(and_(User.name.like("user%"), User.fullname.like("first%"))).all())
print(session.query(User).filter(or_(User.name.like("user%"), User.password != None)).all())

# sql过滤
print(session.query(User).filter("id>:id").params(id=1).all())

# 关联查询
print(session.query(User, Address).filter(User.id == Address.user_id).all())
print(session.query(User).join(User.addresses).all())
print(session.query(User).outerjoin(User.addresses).all())

# 聚合查询
print(session.query(User.name, func.count('*').label("user_count")).group_by(User.name).all())
print(session.query(User.name, func.sum(User.id).label("user_id_sum")).group_by(User.name).all())

# 子查询
stmt = session.query(Address.user_id, func.count('*').label("address_count")).group_by(Address.user_id).subquery()
print(session.query(User, stmt.c.address_count).outerjoin((stmt, User.id == stmt.c.user_id)).order_by(User.id).all())

# exists
print(session.query(User).filter(exists().where(Address.user_id == User.id)))
print(session.query(User).filter(User.addresses.any()))

```


## 限制返回字段查询
```
person = session.query(Person.name, Person.created_at,
             Person.updated_at).filter_by(name="zhongwei").order_by(
             Person.created_at).first()
```




## 记录总数查询：
```
from sqlalchemy import func

# count User records, without
# using a subquery.
session.query(func.count(User.id))

# return count of user "id" grouped
# by "name"
session.query(func.count(User.id)).\
        group_by(User.name)

from sqlalchemy import distinct

# count distinct "name" values
session.query(func.count(distinct(User.name)))
```


SQLAlchemy查询过滤器
>- filter() 把过滤器添加到原查询上，返回一个新查询
>- filter_by() 把等值过滤器添加到原查询上，返回一个新查询
>- limit() 使用指定的值限制原查询返回的结果数量，返回一个新查询
>- offset() 偏移原查询返回的结果，返回一个新查询
>- order_by() 根据指定条件对原查询结果进行排序，返回一个新查询
>- group_by() 根据指定条件对原查询结果进行分组，返回一个新查询
    
---------------------

SQLAlchemy查询执行函数
>- all()	以列表形式返回查询的所有结果
>- first()	返回查询的第一个结果，如果没有结果，则返回None
>- first_or_484()	返回查询的第一个结果，如果没有结果，则终止请求，返回404错误响应
>- get()	返回指定主键对应的行，如果没有对应的行，则返回None
>- get_or_484	返回指定主键对应的行，如果没有找到指定的主键，则终止请求，返回404错误响应
>- count()	返回查询结果的数量
>- paginate()	返回一个Paginate对象，它包含指定范围内的结果
--------------------- 


