import pretty_errors
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime


# 打开数据库连接
# mysql> create datebase db1;
# mysql> GRANT ALL PRIVILEGES ON db1.* TO 'root'@'%' IDENTIFIEED BY 'qcL_584652199';

Base = declarative_base()

class Book_table(Base):
    __tablename__ = 'bookorm'
    book_id = Column(Integer(), primary_key=True)
    book_name = Column(String(50), index=True)

# 定义一个更多的列属性的类
# 规范写法要记得写在最上面


class Author_table(Base):
    __tablename__ = 'authororm'
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,onupdate=datetime.now)


# 实例一个引擎
dburl = "mysql+pymysql://root:qcL_584652199@81.68.90.212:3306/db1?charset=utf8mb4"
engin = create_engine(dburl, echo=True, encoding="utf-8")

Base.metadata.create_all(engin)
