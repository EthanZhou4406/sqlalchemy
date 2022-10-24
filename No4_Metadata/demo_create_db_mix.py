from importlib.metadata import metadata
from sqlalchemy import Table,Column,Integer,String,ForeignKey,create_engine
from sqlalchemy.orm import declarative_base,relationship

dburl = 'mysql+pymysql://root:123456@127.0.0.1:3306/testdb'
engine = create_engine(dburl)

Base = declarative_base()
metadata_obj = Base.metadata

user_table = Table(
    "user",
    metadata_obj,
    Column("id",Integer,primary_key=True,autoincrement=True),
    Column("name",String(30))
)

address_table = Table(
    "address",
    metadata_obj,
    Column("id",Integer,primary_key=True,autoincrement=True),
    Column("email_address",String(200)),
    Column("user_id",ForeignKey("user.id"),nullable=False)
)

class User(Base):
    __table__ = user_table
    address = relationship("Address",back_populates="user")
    def __repr__(self):
        return f'User(name={self.name!r})'

class Address(Base):
    __table__ = address_table
    user = relationship("User",back_populates="address")
    def __repr__(self):
        return f'Address(email_address={self.email_address!r},user={self.user!r})'

def create_table(metadata,engine):
    metadata.create_all(engine)

if __name__ == "__main__":
    create_table(metadata_obj,engine)
