from sqlalchemy import String,Column,Table,Integer,create_engine,Text,text,DateTime,Float,func,BigInteger,Date,Boolean

from sqlalchemy.orm import registry,mapper

localdb = 'mysql+pymysql://root:123456@127.0.0.1:3306/testdb'
crmdb = 'mysql+pymysql://crm_v1:crm123@10.40.6.253:13306/crm_v1'
engine = create_engine(localdb)
con = registry()


crm_advice = Table('crm_advice', con.metadata,
                   Column('id', Integer, primary_key=True, autoincrement=True, comment='id'),
                   Column('title', String(255), comment='标题'),
                   Column('types', String(255), nullable=False, comment='问题类型（1：建议 2：缺陷）'),
                   Column('content', Text(16000000), nullable=False, comment='建议内容'),
                   Column('condition', Integer, server_default=text('1'), comment='问题状态（1：未开始，2：已结束）'),
                   Column('status', Integer, server_default=text('1'), comment='状态（-1：删除，0：禁用，1：启用）'),
                   Column('create_time', DateTime(20), comment='创建时间'),
                   Column('update_time', DateTime(20), comment='更新时间'),
                   Column('delete_time', DateTime(20), comment='删除时间'),
                   Column('create_user', Integer, comment='创建者id'),
                   comment='问题建议表'
                   )


class CRM_ADVICE(object):
    def __init__(self, **kwargs):
        for i in kwargs:
            self.__dict__[i] = kwargs.get(i)


# table与model的映射
mapper(CRM_ADVICE, crm_advice)

crm_dict = Table('crm_dict', con.metadata,
                      Column('id', Integer, primary_key=True, autoincrement=True, comment='选项id'),
                      Column('pid',Integer,comment='pid'),
                      Column('name', String(255), comment='字典名称'),
                      Column('create_time', DateTime(20), comment='创建时间'),
                      Column('update_time', DateTime(20), comment='更新时间'),
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

crm_email = Table('crm_email', con.metadata,
                  Column('id', Integer, primary_key=True, autoincrement=True, comment='id'),
                  Column('title', String(10), comment='邮件标题'),
                  Column('emaillist', String(255), nullable=False, comment='邮箱列表'),
                  Column('content', Text(16000000), nullable=False, comment='邮件内容'),
                  Column('status', Integer, server_default=text('1'), comment='状态（-1：删除，0：禁用，1：启用）'),
                  Column('create_time', DateTime(20), comment='创建时间'),
                  Column('update_time', DateTime(20), comment='更新时间'),
                  Column('delete_time', DateTime(20), comment='删除时间'),
                  Column('create_user', Integer, comment='创建者id'),
                  comment='邮件表'
                  )


class CRM_EMAIL(object):
    def __init__(self, **kwargs):
        for i in kwargs:
            self.__dict__[i] = kwargs.get(i)


# table与model的映射
mapper(CRM_EMAIL, crm_email)

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

crm_fta = Table('rms_fault_tree', con.metadata,
                       Column('id', Integer, primary_key=True,comment='id'),
                       Column('pid', Integer, comment='父id'),
                       Column('description', String(255), nullable=False, comment='描述'),
                       comment='故障树基础信息表'
                       )


class CRM_FTA(object):
    def __init__(self, **kwargs):
        for i in kwargs:
            self.__dict__[i] = kwargs.get(i)


# table与model的映射
mapper(CRM_FTA, crm_fta)

crm_user_logs = Table('crm_user_logs', con.metadata,
                      Column('id', Integer, primary_key=True, autoincrement=True, comment='用户操作日志id'),
                      Column('uid', Integer, nullable=False, comment='用户id'),
                      Column('action', String(100), nullable=False, comment='用户行为'),
                      Column('action_ip', String(24), nullable=False, comment='操作来源ip'),
                      Column('action_table', String(24), nullable=False, comment='操作数据表'),
                      Column('action_id', Text(16000000), nullable=False, comment='操作id'),
                      Column('create_time', DateTime(20), server_default=func.now(), comment='操作时间'),
                      Column('spare1', String(32), comment='备用字段1'),
                      Column('spare2', String(32), comment='备用字段2'),
                      Column('spare3', String(32), comment='备用字段3'),
                      comment='用户操作日志表'
                      )


class CRM_USR_LOGS(object):
    def __init__(self, **kwargs):
        for i in kwargs:
            self.__dict__[i] = kwargs.get(i)


# table与model的映射
mapper(CRM_USR_LOGS, crm_user_logs)


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
    comment='处理流程表'
)
class CRM_PROCESS(object):
    def __init__(self, **kwargs):
        for i in kwargs:
            self.__dict__[i] = kwargs.get(i)
# table与model的映射
mapper(CRM_PROCESS, crm_process)

crm_repair_record = Table(
    "crm_repair_record",
    con.metadata,
    Column("id",BigInteger, primary_key=True, autoincrement=True, comment='主键id'),
    Column("creater",Integer,comment="创建人，用户id"),
    Column('reporter_name', String(50),  comment='报修人名称'),
    Column('reporter_tel', String(20),  comment='报修人电话'),
    Column('report_date', Date(),  comment="保修日期"),
    Column('area', String(20),  comment='保修区域'),
    Column('customer', String(20), comment='整车厂名称'),
    Column('cartype', String(20),  comment="车型名称"),
    Column('end_customer', String(50), comment='终端用户名称'),
    Column('vehicle_num', String(20), comment='车牌号'),
    Column('vin', String(20), comment='车架号'),
    Column('miles', Float(16),default=-1, comment='里程数'),
    Column('produce_date', Date(), comment='生产日期'),
    Column('vehicle_location', String(255), comment='车辆所在省市'),
    Column('error_description', Text, comment='故障现象描述'),
    Column('error_photo', String(255),comment='故障图片id'),
    Column('is_guaranted', String(10), comment="是否在质保期内"),
    Column('supply_method', String(20), comment="供货形式"),
    Column('pack_model', String(20), comment='Pack型号'),
    Column('module_model', String(20), comment='模组型号'),
    Column('cell_model', String(20), comment='电芯型号'),
    Column('project_status', String(10), comment="项目阶段：1表示量产前，2表示量产后"),
    Column('repair_method', String(20), comment="维修渠道"),
    Column('repair_way', String(20), comment='维修方式'),
    Column('service_site', String(50), comment='服务站名称'),
    Column('repair_advice', Text,comment='建议处理方案'),
    Column('repair_review', String(10), comment='建议维修方案审核结果'),
    Column('repair_review_advice', String(255), comment='建议维修方案审核意见'),
    Column('is_alarmed', String(10), comment='是否有大数据预警'),
    Column('alarm_item', String(50), comment='预警项目'),
    Column('error_part_analyse', String(255), comment='失效件初步定位'),
    Column('is_agreed',String(10), comment='是否同意建议方案'),
    Column('repair_advice_final', Text, comment="最终维修方案"),
    Column('error_category', String(50), comment="故障分类"),
    Column('error_part_location', String(150), comment='故障位置'),
    Column('error_part_category', String(100), comment='零部件类别'),
    Column('error_part_actual', String(100), comment='零部件定位'),
    Column('error_part_model', String(20), comment='故障件型号'),
    Column('error_part_factory', String(50), comment="故障件厂家"),
    Column('error_part_code', String(50), comment="故障件编码"),
    Column('repair_date',Date,comment="维修日期"),
    Column('repair_description', Text, comment='维修过程描述'),
    Column('error_disappear_photo', String(200), comment="故障消除照片，imageid"),
    Column('repair_man', String(20), comment='维修人,user id'),
    Column('is_back_needed', String(10), comment='故障件是否返回'),
    Column('back_loaction', String(255), comment='故障件返回地点'),
    Column('is_analyse_needed', String(10), comment='故障件是否分析'),
    Column('ignore_analyse_reason', String(255), comment='不分析的原因'),
    Column('factor', String(20),comment='失效因子，fta id'),
    Column('responsibilities', String(100), comment='责任方'),
    Column('analyse_man', Integer, comment='分析人,user id'),
    Column('transport_way', String(10), comment='返回方式'),
    Column('transport_ticket', String(20), comment='运单号、手机号'),
    Column('back_date',Date(), comment="故障件返回日期"),
    Column('analyse_status', String(10), comment='分析状态'),
    Column('analyse_description', Text, comment='分析过程描述'),
    Column('longtime_method', Text, comment='永久措施'),
    Column('pack_code_analyse', String(50), comment='PACK码'),
    Column('pack_produce_date', Date(), comment='PACK生产日期'),
    Column('pack_produce_line', String(50), comment='PACK产线'),
    Column('module_code_analyse', String(50), comment='模组码'),
    Column('module_produce_date', Date(), comment='模组生产日期'),
    Column('module_produce_line', String(50), comment='模组产线'),
    Column('cell_code_analyse', String(50), comment="电芯码"),
    Column('cell_produce_date', Date(), comment='电芯生产日期'),
    Column('cell_produce_line',String(50), comment='电芯产线'),
    Column('is_draft', String(5), comment="是否处于草稿状态0表示删除，1表示草稿，2表示生效"),
    comment='维修记录表'
)
class CRM_REPAIR_RECORD(object):
    def __init__(self, **kwargs):
        for i in kwargs:
            self.__dict__[i] = kwargs.get(i)
# table与model的映射
mapper(CRM_REPAIR_RECORD, crm_repair_record)


crm_settings = Table('crm_settings', con.metadata,
                        Column('id', Integer, primary_key=True, autoincrement=True, comment='id'),
                        Column('key', String(255), nullable=False, comment='KEY'),
                        Column('label', String(255), nullable=False, comment='标签'),
                        Column('value', Text, nullable=False, comment='value'),
                        Column('status', Integer, server_default=text('1'), comment='状态（-1：删除，0：禁用，1：启用）'),
                        Column('create_time', DateTime(20), comment='创建时间'),
                        comment='系统设置项'
                        )


class CRM_SETTINGS(object):
    def __init__(self, **kwargs):
        for i in kwargs:
            self.__dict__[i] = kwargs.get(i)
# table与model的映射
mapper(CRM_SETTINGS, crm_settings)

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
crm_appendixs = Table('crm_appendixs', con.metadata,
                      Column('id', Integer, primary_key=True, autoincrement=True, comment='id'),
                      Column('source', String(255), nullable=False, comment='文件路径'),
                      Column('name', String(255), nullable=False, comment='文件名称'),
                      Column('type', String(255), nullable=False, comment='附件类型'),
                      Column('status', Integer, server_default=text('1'), comment='状态（-1：删除，0：禁用，1：启用）'),
                      Column('create_time', DateTime(20), comment='创建时间'),
                      Column('update_time', DateTime(20), comment='更新时间'),
                      Column('delete_time', DateTime(20), comment='删除时间'),
                      Column('create_user', Integer, comment='创建者id'),
                      comment='附件资源表'
                      )


class CRM_APPENDIXS(object):
    def __init__(self, **kwargs):
        for i in kwargs:
            self.__dict__[i] = kwargs.get(i)


# table与model的映射
mapper(CRM_APPENDIXS, crm_appendixs)


crm_user = Table('crm_user', con.metadata,
                 Column('id', Integer, primary_key=True, autoincrement=True, comment='用户id'),
                 Column('account', String(20), unique=True, nullable=False, comment='用户账号'),
                 Column('name', String(20), nullable=False, comment='用户名'),
                 Column('email', String(50), unique=True, nullable=False, comment='邮箱'),
                 Column('pwd', String(32), nullable=False, comment='密码'),
                 Column('avatar', String(32), nullable=False, comment='图标'),
                 Column('status', Integer, server_default=text('1'), comment='状态（-1：删除，0：禁用，1：启用）'),
                 Column('last_login_time', DateTime(20), server_default=func.now(), comment='最后登录时间'),
                 Column('last_login_ip', String(15), comment='最后登录ip'),
                 Column('token', String(32), comment='登录令牌'),
                 Column('create_time', DateTime(20),  comment='创建时间'),
                 Column('update_time', DateTime(20),  comment='更新时间'),
                 Column('delete_time', DateTime(20),  comment='删除时间'),
                 Column('create_user', Integer, comment='创建者id'),
                 Column('super_admin', Boolean(20), server_default=text('False'), comment='系统超级管理员'),
                 comment='用户表'
                 )


class CRM_USER(object):
    def __init__(self, **kwargs):
        for i in kwargs:
            self.__dict__[i] = kwargs.get(i)


# table与model的映射
mapper(CRM_USER, crm_user)

crm_role = Table('crm_role', con.metadata,
                 Column('id', Integer, primary_key=True, autoincrement=True, comment='角色id'),
                 Column('pid', Integer, comment='父id'),
                 Column('name', String(255), nullable=False, comment='角色名'),
                 Column('disc', String(50), comment='角色描述'),
                 Column('status', Integer, server_default=text('1'), comment='状态（-1：删除，0：禁用，1：启用）'),
                 Column('create_time', DateTime(20), comment='创建时间'),
                 Column('update_time', DateTime(20), comment='更新时间'),
                 Column('delete_time', DateTime(20), comment='删除时间'),
                 Column('create_user', Integer, comment='创建者id'),
                 comment='角色表'
                 )


class CRM_ROLE(object):
    def __init__(self, **kwargs):
        for i in kwargs:
            self.__dict__[i] = kwargs.get(i)


# table与model的映射
mapper(CRM_ROLE, crm_role)

crm_node = Table('crm_node', con.metadata,
                 Column('id', Integer, primary_key=True, autoincrement=True, comment='节点id'),
                 Column('pid', Integer, comment='父id'),
                 Column('name', String(255), nullable=False, comment='节点名'),
                 Column('disc', String(50), comment='节点描述'),
                 Column('icon', String(255), comment='图标'),
                 Column('type', Integer, comment='节点类型，1：菜单，2：按钮'),
                 Column('router', String(255), comment='前端路由'),
                 Column('api', String(255), comment='后端路由'),
                 Column('sort_num', Float(32), comment='节点顺序'),
                 Column('status', Integer, server_default=text('1'), comment='状态（-1：删除，0：禁用，1：启用）'),
                 Column('create_time', DateTime(20),  comment='创建时间'),
                 Column('update_time', DateTime(20),  comment='更新时间'),
                 Column('delete_time', DateTime(20),  comment='删除时间'),
                 Column('create_user', Integer, comment='创建者id'),
                 comment='节点表'
                 )


class CRM_NODE(object):
    def __init__(self, **kwargs):
        for i in kwargs:
            self.__dict__[i] = kwargs.get(i)


# table与model的映射
mapper(CRM_NODE, crm_node)

crm_user_role = Table('crm_user_role', con.metadata,
                      Column('id', Integer, primary_key=True, autoincrement=True, comment='用户角色id'),
                      Column('user_id', Integer, comment='用户id'),
                      Column('role_id', Integer, comment='角色id'),
                      comment='用户角色表'
                      )


class CRM_USER_ROLE(object):
    def __init__(self, **kwargs):
        for i in kwargs:
            self.__dict__[i] = kwargs.get(i)


# table与model的映射
mapper(CRM_USER_ROLE, crm_user_role)

crm_role_node = Table('crm_role_node', con.metadata,
                      Column('id', Integer, primary_key=True, autoincrement=True, comment='角色节点id'),
                      Column('role_id', Integer, comment='角色id'),
                      Column('node_id', Integer, comment='节点id'),
                      comment='角色节点表'
                      )


class CRM_ROLE_NODE(object):
    def __init__(self, **kwargs):
        for i in kwargs:
            self.__dict__[i] = kwargs.get(i)


# table与model的映射
mapper(CRM_ROLE_NODE, crm_role_node)










con.metadata.create_all(bind=engine)