from sqlalchemy import String,Column,Table,Integer,create_engine,Text,text,DateTime,Float

from sqlalchemy.orm import registry,mapper

localdb = 'mysql+pymysql://root:123456@127.0.0.1:3306/testdb'
crmdb = 'mysql+pymysql://crm_v1:crm123@10.40.6.253:13306/crm_v1'
engine = create_engine(localdb)
con = registry()

crm_dict = Table('crm_dict', con.metadata,
                      Column('id', Integer, primary_key=True, autoincrement=True, comment='选项id'),
                      Column('pid', Integer, comment='父级id'),
                      Column('desc', String(255), comment='字典值'),
                      Column('create_time', DateTime(20), comment='创建时间'),
                      Column('update_time', DateTime(20), comment='更新时间'),
                      Column('delete_time', DateTime(20), comment='删除时间'),
                      Column('create_user', Integer, comment='创建者id'),
                      Column('remark', String(255), comment='备注'),
                      comment='字典选项表'
                      )


class CRM_DICT(object):
    def __init__(self, **kwargs):
        for i in kwargs:
            self.__dict__[i] = kwargs.get(i)


# table与model的映射
mapper(CRM_DICT, crm_dict)

con.metadata.create_all(bind=engine)