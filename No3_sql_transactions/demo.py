'''
Author: Ethan.Zhou ethanzhou4406@outlook.com
Date: 2022-10-22 22:02:30
LastEditors: Ethan.Zhou ethanzhou4406@outlook.com
LastEditTime: 2022-10-22 22:23:24
FilePath: No3_sql_transactions\demo.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from sqlalchemy import create_engine,text

dburl = 'mysql+pymysql://root:123456@127.0.0.1:3306/testdb'
# 获取数据库引擎
engine = create_engine(url=dburl)

# 增加数据
with engine.connect() as conn:
	result = conn.execute(text("INSERT INTO student(id, name, age) VALUES(:id, :name, :age)"),
		[{"id":1, "name":"jack", "age":28},{"id":2, "name":"tom", "age":18},{"id":3, "name":"rose", "age":19}])

# 无条件查询
with engine.connect() as conn:
	students = conn.execute(text("SELECT name,age FROM student"))
	# 这是两种方式
	for stu in students:
		print(stu[0],stu[1])  #下标的方式，stu[0]表示name，stu[1]表示age
		print(stu.name,stu.age) #属性的方式
	# 这是另外一种方式
	for name, age in students:
		print(name,age)

print("*" * 20)
# 有条件查询
with engine.connect() as conn:
	students = conn.execute(text("SELECT name, age FROM student where age < :age"),{"age":20})
	for name, age in students:
		print(name,age)

print("*" * 20)
#  更改记录
with engine.connect() as conn:
	conn.execute(text("UPDATE student SET name=:name WHERE id=:id"),{"name":"Rose","id":3})

# 删除记录
with engine.connect() as conn:
	conn.execute(text("DELETE FROM student WHERE id=:id"),{"id":2})