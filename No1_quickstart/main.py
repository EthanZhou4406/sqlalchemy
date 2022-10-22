# 步骤1：声明模型
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
# 基础类
Base = declarative_base()

class User(Base):
    # 表的名称
    __tablename__ = "user_account"
    # 表的列名及相关设定
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String(60))
    addresses = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
    user = relationship("User", back_populates="addresses")
    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

# 步骤2：创建数据库连接引擎
from sqlalchemy import create_engine
# 利用create_engine函数创建一个数据库连接引擎。
# 注意第一个参数的含义dialect表示所使用的数据库类型，
# driver表示所使用的数据库驱动名称，
# username表示连接数据库时所用的用户名，
# password表示该用户名对应的密码，
# host表示数据库所在的主机名，
# port表示端口号，
# database表示连接的数据库名称。
engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/testdb", encoding='utf8')

# 步骤3：创建数据库表
Base.metadata.create_all(engine)

# 步骤4：利用持久化会话创建记录
from sqlalchemy.orm import Session
# 创建持久的会话对象
with Session(engine) as session:
    # 创建示例对象
    spongebob = User(
        name="spongebob",
        fullname="Spongebob Squarepants",
        addresses=[Address(email_address="spongebob@sqlalchemy.org")],
    )
    sandy = User(
        name="sandy",
        fullname="Sandy Cheeks",
        addresses=[
            Address(email_address="sandy@sqlalchemy.org"),
            Address(email_address="sandy@squirrelpower.org"),
        ],
    )
    patrick = User(name="patrick", fullname="Patrick Star")
    # 添加所有记录
    session.add_all([spongebob, sandy, patrick])
    # 提交数据库
    session.commit()
# 步骤5：单表查询
from sqlalchemy import select
# 创建持久会话对象
session = Session(engine)

stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))

for user in session.scalars(stmt):
    print(user)

# 步骤6：多表查询
stmt = (
    select(Address)
    .join(Address.user)
    .where(User.name == "sandy")
    .where(Address.email_address == "sandy@sqlalchemy.org")
)
sandy_address = session.scalars(stmt).one()

# 步骤7：更新记录
stmt = select(User).where(User.name == "patrick")
patrick = session.scalars(stmt).one()


patrick.addresses.append(Address(email_address="patrickstar@sqlalchemy.org"))


sandy_address.email_address = "sandy_cheeks@sqlalchemy.org"

session.commit()

# 步骤8：删除记录
# 获取要删除的对象
sandy = session.get(User, 2)
# 删除指定的对象
sandy.addresses.remove(sandy_address)
# 执行删除
session.flush()
# 指定要删除的对象
session.delete(patrick)
# 执行删除
session.commit()
