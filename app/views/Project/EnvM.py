# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 11:30:43
# @Author  : DannyDong
# @File    : EnvM.py
# @Describe: 环境管理业务逻辑

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
    
    # 新增环境信息
    def add_env(self, pro_id, env_name, base_url):
        pro_info = ProjectModel.query.filter_by(project_id=pro_id).first()
        if pro_info is None:
            res = Result(msg='Project ID 无效，没有查找到对应的项目').success()
        elif env_name == '' or base_url == '':
            res = Result(msg='环境名称或基础地址不能为空').success()
        else:
            env_id = self.__create_uuid()
            env_info = EnvModel(
                env_id=env_id, env_name=env_name,
                base_url=base_url, pro_id=pro_id
            )
            db.session.add(env_info)
            db.session.commit()
            res = Result(msg='新增环境信息成功').success()
        return make_response(res)
