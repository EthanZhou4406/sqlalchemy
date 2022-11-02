from sqlalchemy import String,Column,Table,Integer,create_engine

from sqlalchemy.orm import registry,mapper

engine = create_engine('mysql+pymysql://crm_v1:crm123@10.40.6.253:13306/crm_v1')
con = registry()

crm_project = Table(
    "crm_project",
    con.metadata,
    Column('id',Integer,primary_key=True,autoincrement=True,comment='主键id'),
    Column('base',String(20),comment='生产基地'),
    Column('customer',String(20),comment='客户名称'),
    Column('project',String(40),comment='项目名称'),
    Column('baktype',String(20),comment='留用形式'),
    Column('isvalid',String(10),comment='产线状态，1在产，0停产'),
    Column('btype',String(20),comment='电池型号'),
    Column('htype',String(20),comment='交付类型'),
    Column('material',String(20),comment='料号'),
    Column('ptype',String(50),comment='产品型号'),
    Column('smanager',Integer,comment='售后经理,用户表id'),
    Column('cqe',Integer,comment='CQE,用户表id'),
    Column('bakstandard',String(10),comment='备货标准'),
    Column('bak1',String(50),comment='备用字段1'),
    Column('bak2',String(50),comment='备用字段2'),
    Column('bak3',String(50),comment='备用字段3'),
    comment="整车厂和项目表"
)
class CRM_PROJECT(object):
    def __init__(self, **kwargs):
        for i in kwargs:
            self.__dict__[i] = kwargs.get(i)

mapper(CRM_PROJECT, crm_project)

con.metadata.create_all(bind=engine)