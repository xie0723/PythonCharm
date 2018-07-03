#  sqlalchemy  反射


from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

uri = '数据库类型+驱动://账号:密码@IP:端口/数据库名称'

engine = create_engine(uri, echo=False)

metadata = MetaData(engine)

# ①：反射单个表
# apply_info = Table('apply_info', metadata, autoload=True)
# apply_info.columns.keys()  # 列出所有的列名
# *********************************************************************
# ②：反射整个数据库
# 使用reflect()方法，它不会返回任何值
# metadata.reflect(bind=engine)

# metadata.tables.keys()  # 获取所有的表名
# # 虽然反射了整个数据库，还是需要再添加一次具体的表反射.
# apply_info = metadata.tables['apply_info']
# *********************************************************************

# ③：基于ORM的反射

Base = automap_base()
# Base = declarative_base()
# apply_info = Base.metadata.tables['apply_info']

Base.prepare(engine, reflect=True)
Base.classes.keys()  # 获取所有的对象名
# 获取表对象
apply_info = Base.classes.apply_info
# *********************************************************************


Session = sessionmaker(bind=engine)

session = Session()

# 插入数据
# session.add(apply_info(email_address="foo@bar.com", name="foo"))
# session.commit()

# keys = apply_info.__table__.columns.keys()
#
# rows = session.query(apply_info)
#
# data = [getattr(rows, key) for key in keys]

# mysql 查询的结果，可以通过dot.号访问。而oracle 不可以。
