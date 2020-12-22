# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 11:30:43
# @Author  : DannyDong
# @File    : EnvM.py
# @Describe: 环境管理业务逻辑

import time
import uuid

from flask import make_response

from factory import db
from app.Common.Result import Result
from app.Model.EnvModel import EnvModel
from app.Model.ProjectModel import ProjectModel


class EnvM(object):
    def __init__(self):
        pass

    # 生成UUID
    @staticmethod
    def __create_uuid():
        return str(uuid.uuid4())
    
    # 时间转换
    @staticmethod
    def __transform_time(timeObj):
        return time.strftime("%Y-%m-%d %H:%M:%S", timeObj.timetuple())
    
    # 序列化环境信息
    def __env_info_serializer(self, env_item):
        return {
            'envId': env_item[0],
            'envName': env_item[1],
            'baseURL': env_item[2],
            'createTime': self.__transform_time(env_item[3]),
            'creator': env_item[4]
        }
    
    # 新增环境信息
    def add_env(self, user_id, pro_id, env_name, base_url):
        pro_info = ProjectModel.query.filter_by(project_id=pro_id).first()
        if pro_info is None:
            res = Result(msg='Project ID 无效，没有查找到对应的项目').success()
        elif env_name == '' or base_url == '':
            res = Result(msg='环境名称或基础地址不能为空').success()
        else:
            env_id = self.__create_uuid()
            env_info = EnvModel(
                env_id=env_id, env_name=env_name,
                base_url=base_url, pro_id=pro_id,
                creator=user_id
            )
            db.session.add(env_info)
            db.session.commit()
            res = Result(msg='新增环境信息成功').success()
        return make_response(res)
    
    # 环境信息列表
    def get_env_list(self):
        sql = ''' select env_id, env_name, base_url, env.create_time, username from env 
                left join user on user_id=creator 
                where is_delete=0 
                order by env.create_time desc; '''
        data_obj = db.session.execute(sql)
        data = [self.__env_info_serializer(item) for item in data_obj]
        res = Result(data).success()
        return make_response(res)
    
    # 编辑环境信息
    def edit_env(self, is_del, env_id, env_name, base_url):
        env_info = EnvModel.query.filter_by(env_id=env_id).first()
        if env_info is None:
            res = Result(msg='Env ID 无效，没有找到对应的版本').success()
        elif is_del == 1:
            env_info.is_delete = 1
            db.session.commit()
            res = Result(msg='环境信息删除成功').success()
        elif env_name == '' or base_url == '':
            res = Result(msg='环境名称或基础地址不能为空').success()
        else:
            env_info.env_name = env_name
            env_info.base_url = base_url
            db.session.commit()
            res = Result(msg='环境信息修改成功').success()
        return make_response(res)
