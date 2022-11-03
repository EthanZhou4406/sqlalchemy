from sqlalchemy import String,Column,Table,Integer,create_engine,Text,text,DateTime,Float

from sqlalchemy.orm import registry,mapper

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/testdb')
con = registry()

crm_fault_tree = Table('rms_fault_tree', con.metadata,
                       Column('id', Integer, primary_key=True, autoincrement=True, comment='id'),
                       Column('pid', Integer, comment='父id'),
                       Column('tag', String(10), comment='复制tag'),
                       Column('description', String(255), nullable=False, comment='描述'),
                       Column('mechanism', Text(16000000), nullable=False, comment='机理'),
                       Column('img_id', String(255), comment='照片ID'),
                       Column('appendix_id', String(255), comment='附件ID'),
                       Column('sort_num', Float(32), comment='节点顺序'),
                       Column('status', Integer, server_default=text('1'), comment='状态（-1：删除，0：禁用，1：启用）'),
                       Column('source', Integer, server_default=text('0'), comment='来源（0：新增 1：继承）'),
                       Column('create_time', DateTime(20), comment='创建时间'),
                       Column('update_time', DateTime(20), comment='更新时间'),
                       Column('delete_time', DateTime(20), comment='删除时间'),
                       Column('create_user', Integer, comment='创建者id'),
                       comment='故障树基础信息表'
                       )


class CRM_FAULT_TREE(object):
    def __init__(self, **kwargs):
        for i in kwargs:
            self.__dict__[i] = kwargs.get(i)


# table与model的映射
mapper(CRM_FAULT_TREE, crm_fault_tree)

con.metadata.create_all(bind=engine)