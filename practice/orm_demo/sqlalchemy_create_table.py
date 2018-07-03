from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String,Integer, DateTime, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

uri = '数据库类型+驱动://账号:密码@IP:端口/数据库名称'



# 创建连接
engine = create_engine(uri)

Base = declarative_base()



class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)


class Movie(BaseModel):
    __tablename__ = 'Movie'
    title = Column(String(255), nullable=False)
    genres = Column(String(255))
    # name = Column(String(255))
    
    
Base.metadata.bind = engine
Base.metadata.create_all()


# 创造数据库会话，用于sql 执行
Session = sessionmaker(bind=engine)
session = Session()


# 查询，返回是一个可迭代的Query结果对象
# result = session.query(Movie).filter_by(id='1')

# 返回Query对象中的第一条数据
# result.first()

# 去除第一条数据的id 值
# result.first().id

