
from sqlalchemy import String,Column,Table,Integer,create_engine,Text,text,DateTime,Float,Date,BigInteger,not_,null,func,and_,outerjoin


from sqlalchemy.orm import registry,mapper,Session

localdb = 'mysql+pymysql://root:123456@127.0.0.1:3306/testdb'
crmdb = 'mysql+pymysql://crm_v1:crm123@10.40.6.253:13306/crm_v1'
engine = create_engine(crmdb)
con = registry()
crm_images = Table('crm_images', con.metadata,
                   Column('id', Integer, primary_key=True, autoincrement=True, comment='id'),
                   Column('source', String(255), nullable=False, comment='	图片路径'),
                   Column('thumb_image', String(255), nullable=False, comment='缩略图路径'),
                   Column('status', Integer, server_default=text('1'), comment='状态（-1：删除，0：禁用，1：启用）'),
                   Column('create_time', DateTime(20), comment='创建时间'),
                   Column('update_time', DateTime(20), comment='更新时间'),
                   Column('delete_time', DateTime(20), comment='删除时间'),
                   Column('create_user', Integer, comment='创建者id'),
                   comment='图片资源表'
                   )


class CRM_IMAGES(object):
    def __init__(self, **kwargs):
        for i in kwargs:
            self.__dict__[i] = kwargs.get(i)


# table与model的映射
mapper(CRM_IMAGES, crm_images)
db = Session(bind=engine)
image = db.query(CRM_IMAGES.source).filter(CRM_IMAGES.id == 1).one()
print(image[0])

# db = Session(bind=engine)
# # .filter(CRM_PROCESS.next_process_owner == 4)

# # subq = db.query(func.max(CRM_PROCESS.id).label("maxid"),CRM_PROCESS.repair_record).group_by(CRM_PROCESS.repair_record).subquery()
# records = db.execute(text('''
#         SELECT * from `crm_process` ,
#         (SELECT max(id) as maxid,repair_record FROM `crm_process` GROUP BY repair_record ) as tem
#         WHERE crm_process.id = tem.maxid and  not isnull(crm_process.next_process_owner)'''))
# repair_records = []
# for record in records:
#     repair_records.append(record['repair_record'])
# print(repair_records) 




# con.metadata.create_all(bind=engine)