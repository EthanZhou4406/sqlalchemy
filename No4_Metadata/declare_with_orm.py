from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import registry

# 创建注册表
mapper_registry = registry()
metadata = mapper_registry.metadata()
# 创建基础类
Base = mapper_registry.generate_base()

# 创建基础类的另一种方法
from sqlalchemy import Integer,String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    name = Column(String(30))
    fullname = Column(String(50))

    address = relationship("Address", back_populates="user")
    def __repr__(self) -> str:
        return f"User(id={self.id!r},name={self.name!r},fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer,primary_key = True)
    email_address = Column(String,nullable = False)
    user_id = Column(Integer,ForeignKey("user_account.id"))

    user = relationship("User",back_populates="address")
    def __repr__(self) -> str:
        return f"Address(id={self.id!r},email_address={self.email_address!r})"