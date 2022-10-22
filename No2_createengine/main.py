from venv import create
from sqlalchemy import create_engine



# 演示当密码中包含@和/特殊字符时导致创建Engine对象失败
# dburl = "mysql+pymysql://testuser:123@456/!@127.0.0.1:3306/dbtest1"
# engine = create_engine(url=dburl,encoding='utf8')
# print(engine.connect())

import urllib.parse 
def encode_pwd(pwd:str) -> str:
    encode_password = urllib.parse.quote_plus(pwd)
    return encode_password

def get_dburl(pwd:str) -> str:
    password = encode_pwd(pwd)
    return f"mysql+pymysql://testuser:{password}@127.0.0.1:3306/dbtest1"

engine = create_engine(url=get_dburl('123@456/!'),encoding='utf8')
print(engine.connect())

'''
常见数据库连接的格式：
# default == psycopg2
engine = create_engine("postgresql://scott:tiger@localhost/mydatabase")
# psycopg2
engine = create_engine("postgresql+psycopg2://scott:tiger@localhost/mydatabase")
# pg8000
engine = create_engine("postgresql+pg8000://scott:tiger@localhost/mydatabase")


# default == mysqlclient
engine = create_engine("mysql://scott:tiger@localhost/foo")
# mysqlclient (a maintained fork of MySQL-Python)
engine = create_engine("mysql+mysqldb://scott:tiger@localhost/foo")
# PyMySQL
engine = create_engine("mysql+pymysql://scott:tiger@localhost/foo")


engine = create_engine("oracle://scott:tiger@127.0.0.1:1521/sidname")
engine = create_engine("oracle+cx_oracle://scott:tiger@tnsname")



# pyodbc == default
engine = create_engine("mssql+pyodbc://scott:tiger@mydsn")
# pymssql
engine = create_engine("mssql+pymssql://scott:tiger@hostname:port/dbname")

'''