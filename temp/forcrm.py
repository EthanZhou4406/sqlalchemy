
from sqlalchemy import String,Column,Table,Integer,create_engine,Text,text,DateTime,Float,Date,BigInteger,not_,null,func,and_,outerjoin


from sqlalchemy.orm import registry,mapper,Session

localdb = 'mysql+pymysql://root:123456@127.0.0.1:3306/testdb'
crmdb = 'mysql+pymysql://crm_v1:crm123@10.40.6.253:13306/crm_v1'
engine = create_engine(crmdb)
con = registry()
crm_process = Table(
    "crm_process",
    con.metadata,
    Column('id', BigInteger, primary_key=True, autoincrement=True, comment='主键id'),
    Column('modify_time', DateTime(20), nullable=False, comment='修改时间'),
    Column('current_process', String(20), nullable=False, comment='当前流程名称'),
    Column('process_action',String(20),comment='操作按钮名称，同意，拒绝，转移'),
    Column('process_result', String(255), nullable=False, comment='流程处理结果'),
    Column('process_owner',Integer,comment='执行人id'),
    Column('repair_record', BigInteger, nullable=False, comment='维修记录id'),
    Column('next_process',String(20),comment='下一流程名称'),
    Column('next_process_owner',Integer,comment='下一流程执行人id'),
    comment='处理流程表'
)
class CRM_PROCESS(object):
    def __init__(self, **kwargs):
        for i in kwargs:
            self.__dict__[i] = kwargs.get(i)
# table与model的映射
mapper(CRM_PROCESS, crm_process)

db = Session(bind=engine)
# .filter(CRM_PROCESS.next_process_owner == 4)

# subq = db.query(func.max(CRM_PROCESS.id).label("maxid"),CRM_PROCESS.repair_record).group_by(CRM_PROCESS.repair_record).subquery()
records = db.execute(text('''
        SELECT * from `crm_process` ,
        (SELECT max(id) as maxid,repair_record FROM `crm_process` GROUP BY repair_record ) as tem
        WHERE crm_process.id = tem.maxid and  not isnull(crm_process.next_process_owner)'''))
repair_records = []
for record in records:
    repair_records.append(record['repair_record'])
print(repair_records) 




# con.metadata.create_all(bind=engine)