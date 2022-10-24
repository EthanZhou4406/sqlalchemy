'''
Author: Ethan.Zhou ethanzhou4406@outlook.com
Date: 2022-10-23 21:01:14
LastEditors: Ethan.Zhou ethanzhou4406@outlook.com
LastEditTime: 2022-10-23 22:01:18
FilePath: No4_Metadata\main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String,ForeignKey

dburl = 'mysql+pymysql://root:123456@127.0.0.1:3306/testdb'
engine = create_engine(url = dburl)
metadata = MetaData()

# 演示利用Table类声明数据表

user_table = Table(
    "user",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("name",String(30)),
    Column("fullname",String)
)

address_table = Table(
    "address",
    metadata,
    Column("id",Integer, primary_key = True),
    Column("user_id", ForeignKey("user.id"), nullable = False),
    Column("email_address", String(200), nullable=False)
)

# 利用metadata来创建数据表
def create_table(metadata,engine):
    metadata.create_all(engine)

# 利用metadata来删除数据表
def drop_table(metadata,engine):
    metadata.drop_all(engine)