from sqlalchemy import Table,Column,ForeignKey,MetaData,Integer,String
from sqlalchemy.orm import declarative_base,relationship
Base = declarative_base()
metadata = MetaData()
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

class User(Base):
    __table__ = user_table,
    address = relationship("Address",back_populates="user")
    def __repr__(self):
        return f"User({self.name!r},{self.fullname!r}"

class Address(Base):
    __table__ = address_table,
    user = relationship("User",back_populates="address")
    def __repr__(self) -> str:
        return f"Address({self.email_address!r}"