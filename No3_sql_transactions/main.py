'''
Author: Ethan.Zhou ethanzhou4406@outlook.com
Date: 2022-10-22 20:30:05
LastEditors: Ethan.Zhou ethanzhou4406@outlook.com
LastEditTime: 2022-10-22 21:18:04
FilePath: No3_sql_transactions\main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from sqlalchemy import create_engine,text
dburl = 'mysql+pymysql://root:123456@127.0.0.1:3306/testdb'
engine = create_engine(dburl,echo=True).connect()

# 演示原生sql交互数据库
text_sql = "select 'hello world'"
def say_hello(engine,text_sql):
    with engine.connect() as conn:
        result = conn.execute(text(text_sql))
        print(result.all())

create_sql = "CREATE TABLE student(id int,name varchar(20),age smallint)"
def create_table(engine,text_sql):
    with engine.connect() as conn:
        conn.execute(text(text_sql))

insert_sql = "INSERT INTO student (id,name,age) VALUES (:id, :name,:age)"
records = [{"id": 1, "name": "jack","age":18}, {"id": 2, "name": "tom","age":19}]
def insert_record(engine,text_sql,records):
    with engine.connect() as conn:
        conn.execute(text(text_sql),records)

fetch_sql = "SELECT name, age FROM student"
def fetch_record(engine,text_sql):
    with engine.connect() as conn:
        students = conn.execute(text(text_sql))
        print(text(text_sql))
        for stu in students:
            print(f"name:{stu.name}  age:{stu.age}")
            print(f"name:{stu[0]}  age:{stu[1]}")
        
        for name,age in students:
            print(f"{name} {age}")
    


if __name__ == "__main__":
    fetch_record(engine,fetch_sql)
    