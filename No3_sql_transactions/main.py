from sqlalchemy import create_engine,text
dburl = 'mysql+pymysql://root:123456@127.0.0.1:3306/testdb'
engine = create_engine(dburl,echo=True)

# 演示原生sql交互数据库
# with engine.connect() as conn:
#     result = conn.execute(text("select 'hello world'"))

#     # conn.execute(text("CREATE TABLE student(id int,name varchar(20),age smallint)"))
#     conn.execute(
#         text("INSERT INTO student (id,name,age) VALUES (:id, :name,:age)"),
#         [{"id": 1, "name": "jack","age":18}, {"id": 2, "name": "tom","age":19}]
#         )
    


with engine.begin() as conn:
    result = conn.execute(text("select 'hello world'"))

    # conn.execute(text("CREATE TABLE student(id int,name varchar(20),age smallint)"))
    conn.execute(
        text("INSERT INTO student (id,name,age) VALUES (:id, :name,:age)"),
        [{"id": 1, "name": "jack","age":18}, {"id": 2, "name": "tom","age":19}]
        )
    