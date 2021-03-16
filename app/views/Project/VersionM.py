# -*- coding: utf-8 -*-
# @Time    : 2020/12/09 15:02:18
# @Author  : DannyDong
# @File    : VersionM.py
# @Describe: 版本管理业务逻辑

import time
import uuid

from flask import make_response

from factory import db
from app.Common.Result import Result
from app.Model.UserModel import UserModel
from app.Model.VersionModel import VersionModel as VM
from app.Model.ProjectModel import ProjectModel
from app.Utils.TransformTime import transform_time


class VersionM(object):
    def __init__(self):
        pass

    # 生成UUID
    @staticmethod
    def __create_uuid():
        return str(uuid.uuid4())

    # 序列化版本号信息
    def __ver_info_serializer(self, ver_item):
        return {
            'verID': ver_item[0],
            'version': ver_item[1],
            'remark': ver_item[2],
            'createTime': transform_time(ver_item[3]),
            'creator': ver_item[4]
        }

    # 新增版本号
    def add_version(self, user_id, pro_id, version, remark):
        pro_info = ProjectModel.query.filter_by(project_id=pro_id).first()
        if pro_info is None:
            res = Result(msg='Project ID 无效，没有查找到对应的项目').fail()
        elif version == '':
            res = Result(msg='版本号不能为空').fail()
        else:
            ver_id = self.__create_uuid()
            version_info = VM(
                ver_id=ver_id, 
                version=version, 
                remark=remark, 
                pro_id=pro_id, 
                creator=user_id
            )
            db.session.add(version_info)
            db.session.commit()
            res = Result(msg='新增版本号成功').success()
        return make_response(res)

    # 版本号列表
    def get_version_list(self, pro_id):
        # 获取数据对象
        version_obj = db.session.query(
            VM.ver_id, VM.version, VM.remark, VM.create_time, UserModel.username
        ).join(UserModel, UserModel.user_id == VM.creator)
        # 数据对象进行筛选和排序
        data_obj = version_obj.filter(VM.is_delete == 0).filter(VM.pro_id == pro_id).order_by(VM.create_time.desc())
        data = [self.__ver_info_serializer(item) for item in data_obj]
        res = Result(data).success()
        return make_response(res)

    # 编辑版本号
    def edit_version(self, is_del, ver_id, version, remark):
        ver_info = VM.query.filter_by(ver_id=ver_id).first()
        if ver_info is None:
            res = Result(msg='Version ID 无效，没有找到对应的版本').fail()
        elif is_del == 1:
            ver_info.is_delete = 1
            db.session.commit()
            res = Result(msg='版本号删除成功').success()
        elif version == '':
            res = Result(msg='版本号不能为空').fail()
        else:
            ver_info.version = version
            ver_info.remark = remark
            db.session.commit()
            res = Result(msg='版本号修改成功').success()
        return make_response(res)
