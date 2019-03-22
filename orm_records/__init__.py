from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker

URL = "mysql://cmdb_dev:cZt3homvrlAy2cgT@rm-uf6761kt70m851725.mysql.rds.aliyuncs.com/cmdb_dev"

engine = create_engine(URL, encoding="UTF-8", echo=True)

table_meta = MetaData(bind=engine, reflect=True)

pipelines = table_meta.tables.get('pipelines')
# print(pipelines)

Session = sessionmaker(bind=engine)
session = Session()

# ret = session.query(pipelines).filter_by(id=49).one()

# print(ret.id)

# from sqlalchemy import create_engine, String ,MetaData
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# 在创建表对象和查询时，有几个核心
# ① create_engine  创建数据库连接
# ② declarative_base  定义表对象的基类
# ③ sessionmaker 用于数据库的CRUD
# ④ String 字段类用于创建数据库定义字段类型
# ⑤ MetaData 用于反射


