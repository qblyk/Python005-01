import pretty_errors
from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime,desc,and_,or_,not_

Base = declarative_base()

class UserInfotable(Base):
    __tablename__ = 'UserInfo'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    userId = Column(Integer(), unique=True)
    userName = Column(String(128))
    crttime = Column(DateTime(), default=datetime.now)
    upttime = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return "UserInfo(id='{self.id}',userId={self.userId},userName={self.userName})".format(self=self)


class UserAssettable(Base):
    __tablename__ = 'UserAsset'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    userId = Column(Integer(), unique=True)
    totalAsset = Column(Integer())
    crttime = Column(DateTime(), default=datetime.now)
    upttime = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

class TransLogtable(Base):
    __tablename__ = 'TransLog'
    id = Column(Integer(), primary_key=True)
    transtime = Column(DateTime(), default=datetime.now) 
    usetransUserIdrId = Column(Integer())
    acceptorUserId = Column(Integer())
    transAmt = Column(Integer())
    transType = Column(Integer())
    crttime = Column(DateTime(), default=datetime.now)
    upttime = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

# 实例化一个引擎
dburl = "mysql+pymysql://root:qcL_584652199@81.68.90.212:3306/db1?charset=utf8mb4"
engine = create_engine(dburl, echo=False, encoding="utf-8")

# 创建session
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# 增加数据
# userInfo_demo = UserInfotable(userId='4',userName="李东风",crttime=datetime.now())
# userInfo_demo1 = UserInfo()  #,userName="卿宇晨",crttime=

# 查询
# result = session.query(UserInfotable).all()
result1 = session.query(UserInfotable).first()

# first()
# one()     结果确保只有一行
# scalar()  第一个结果第一个元素（结果确保只有一行）

print(">> 全表查询数据:")
for result in session.query(UserInfotable):  #全表列查询
    print(">> ",result)

# 指定列
print(">> 指定列数据:")
for result in session.query(UserInfotable.userName):
    print(">> ",result)

# 排序(反向desc)
print(">> 排序数据:")
for result in session.query(UserInfotable.userId,UserInfotable.userName).order_by(desc(UserInfotable.userId)):
    print(">> ",result)

# limit数据
print(">> limit数据:")
query = session.query(UserInfotable.userId,UserInfotable.userName).order_by(desc(UserInfotable.userId)).limit(3)
print(">> ",[result.userName for result in query])

# 条件查询filter
print(">> filter数据:")
print(">> ",session.query(UserInfotable.userId,UserInfotable.userName).filter(UserInfotable.userId > 2).all())

# 多条件查询filter
print(">> filter多条件数据:")
print(">> ",session.query(UserInfotable.userId,UserInfotable.userName).filter(UserInfotable.userId > 2, UserInfotable.userName == "李东风").all())

# 连接词 and or not 
print(">> 连接词 and or not 数据:")
print(">> ",session.query(UserInfotable.userId,UserInfotable.userName).filter(
    or_(
        UserInfotable.userName == "李大山",
        UserInfotable.userName == "王大山"
        )
    ).all())

# 更新
query = session.query(UserInfotable)
query = query.filter(UserInfotable.userId == 1)
query.update({UserInfotable.userName: '蔡小山'})


for result in session.query(UserInfotable):  #全表列查询
    print(">> ",result)


# 删除
# session.add(userInfo_demo)
query = session.query(UserInfotable).order_by(desc(UserInfotable.id)).limit(1)

# query.one()
session.delete(query.one())

# 新增数据
userIdP =  max(session.query(UserInfotable.id))[0]+3
userInfo_demo = UserInfotable(userId=userIdP,userName="李东风",crttime=datetime.now())
session.add(userInfo_demo)

# session.flush()
session.commit()  # 执行操作