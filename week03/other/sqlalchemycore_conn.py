


import pretty_errors
import pymysql
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey

# 打开数据库连接
# mysql> create datebase db1;
# mysql> GRANT ALL PRIVILEGES ON db1.* TO 'root'@'%' IDENTIFIEED BY 'qcL_584652199';
# echo=True 开启调试

engine = create_engine("mysql+pymysql://root:qcL_584652199@81.68.90.212:3306/db1",echo=True)

# 创建元数据
metadata = MetaData(engine)

book_table = Table('book',metadata,
    Column('id',Integer,primary_key=True),
    Column('name',String(20)))
author_table = Table('author',metadata,
    Column('id', Integer, Primary_key=True),
    Column('book_id', None, ForeignKey('book.id')),
    Column('author_name',String(128), nullable=False)
    )

try:
    metadata.create_all()
except Exception as e:
    print(f"create error {e}")
