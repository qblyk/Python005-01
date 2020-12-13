import pretty_errors
from sqlalchemy.orm import sessionmaker,Session
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

    def __repr__(self):
        return "UserAsset(id='{self.id}',userId={self.userId},totalAsset={self.totalAsset})".format(self=self)

class TransLogtable(Base):
    __tablename__ = 'TransLog'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    transtime = Column(DateTime(), default=datetime.now) 
    transUserId = Column(Integer())
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
# session = Session(engine)

transAmt_ = 100

# 根据姓名查询用户编号
transUser_ = session.query(UserInfotable.userId).filter(UserInfotable.userName == '张三')[0]
acceptorUser = session.query(UserInfotable.userId).filter(UserInfotable.userName == '王大山')[0]
# print(transUserId_)

# 根据用户编号查询交易账户当前额度
# fromtransUserAmt = session.query(UserAssettable.totalAsset).filter(UserAssettable.userId == transUserId_)
# print(fromtransUserAmt)
# totransUserAmt = session.query(UserAssettable.totalAsset).filter(UserAssettable.userId == acceptorUserId_)[0]

# 更新两个账户额度
session.query(UserAssettable).filter(UserAssettable.userId == transUser_).update({UserAssettable.totalAsset: UserAssettable.totalAsset - transAmt_})
session.query(UserAssettable).filter(UserAssettable.userId == acceptorUser).update({UserAssettable.totalAsset: UserAssettable.totalAsset + transAmt_})

# 新增操作记录
session.add(TransLogtable(transtime=datetime.now(),transUserId=transUser_.userId,acceptorUserId=acceptorUser.userId,transAmt=transAmt_,transType=1,crttime=datetime.now()))

# session.flush()
session.commit()  # 执行操作

# session.close;