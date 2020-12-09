# -*- coding: utf-8 -*-
# @Time    : 2020/12/09 15:02:18
# @Author  : DannyDong
# @File    : VersionM.py
# @Describe: 版本管理业务逻辑

import uuid

from flask import make_response

from factory import db
from app.Common.Result import Result
from app.Model.VersionModel import VersionModel
from app.Model.ProjectModel import ProjectModel


class VersionM(object):
    def __init__(self):
        pass

    # 生成UUID
    @staticmethod
    def __create_uuid():
        return str(uuid.uuid4())

    # 新增版本号
    def add_version(self, pro_id, version, remark):
        pro_info = ProjectModel.query.filter_by(project_id=pro_id).first()
        if pro_info is None:
            res = Result(msg='Project ID 无效，没有查找到对应的项目').success()
        elif version == '':
            res = Result(msg='版本号不能为空').success()
        else:
            ver_id = self.__create_uuid()
            version_info = VersionModel(
                ver_id=ver_id, version=version,
                remark=remark, pro_id=pro_id
            )
            db.session.add(version_info)
            db.session.commit()
            res = Result(msg='新增版本号成功').success()
        return make_response(res)
