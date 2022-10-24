from sqlalchemy import create_engine,Table
from sqlalchemy.orm import declarative_base,Session
urldb = 'mysql+pymysql://root:123456@127.0.0.1:3306/testdb'
engine = create_engine(urldb)
Base = declarative_base()
metadata_obj = Base.metadata

# 利用Table中的autoload自动生成对应的表
stu_table = Table("student",metadata_obj,autoload_with=engine)

class Student(Base):
    __table__ = stu_table
    def __repr__(self) -> str:
        return f"Student(name={self.name!r},age={self.age!r})"

def insert_stu(name:str,age:int):
    with Session(engine) as session:
        stu = Student(name=name,age=age)
        session.add(stu)
        session.commit()

if __name__ == "__main__":
    insert_stu("Jack",12)