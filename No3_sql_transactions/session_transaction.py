'''
Author: Ethan.Zhou ethanzhou4406@outlook.com
Date: 2022-10-23 06:11:33
LastEditors: Ethan.Zhou ethanzhou4406@outlook.com
LastEditTime: 2022-10-23 06:45:06
FilePath: No3_sql_transactions\session_transaction.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from sqlalchemy import create_engine,text
from sqlalchemy.orm import Session

# 第一步：创建数据库引擎
dburl = 'mysql+pymysql://root:123456@127.0.0.1:3306/testdb'
engine = create_engine(url=dburl)

# # 第二步：创建orm中会话对象
# session = Session(engine)

# 第三步：创建原生sql

sql_text = "SELECT name, age FROM student"

# # 第四步：执行原生sql
# students = session.execute(text(sql_text))

# # 第五步：查看执行结果
# for name,age in students:
#     print(name, age)

# # 第六步：关闭会话对象
# session.close()

# 整合后的代码
with Session(engine) as session:
	students = session.execute(text(sql_text))
	for name, age in students:
		print(name,age)