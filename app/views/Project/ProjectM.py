# -*- coding: utf-8 -*-
# @Time    : 2020/12/01 23:37:35
# @Author  : DannyDong
# @File    : ProjectM.py
# @Describe: 项目管理业务逻辑

import uuid

from flask import make_response

from factory import db
from app.Common.Result import Result
from app.Model.ProjectModel import ProjectModel


class ProjectM(object):
    def __init__(self):
        pass

    # 生成UUID
    def create_uuid(self):
        return str(uuid.uuid4())
    
    # 新增项目
    def add_project(self, user_id, pro_name, remark):
        if pro_name == '':
            res = Result(msg='项目名称不能为空').success()
        else:
            pro_id = self.create_uuid()
            pro_info = ProjectModel(
                project_id=pro_id, project_name=pro_name,
                remark=remark, creator=user_id
            )
            db.session.add(pro_info)
            db.session.commit()
            res = Result(msg='项目新增成功').success()
        return make_response(res)

