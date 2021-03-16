# -*- coding: utf-8 -*-
# @Time    : 2020/12/01 23:37:35
# @Author  : DannyDong
# @File    : ProjectM.py
# @Describe: 项目管理业务逻辑

import time
import uuid

from flask import make_response

from factory import db
from app.Common.Result import Result
from app.Model.ProjectModel import ProjectModel
from app.Model.UserModel import UserModel
from app.Utils.TransformTime import transform_time


class ProjectM(object):
    def __init__(self):
        pass

    # 生成UUID
    @staticmethod
    def __create_uuid():
        return str(uuid.uuid4())

    # 序列化项目信息
    @staticmethod
    def __pro_info_serializer(pro_item):
        return {
            'projectID': pro_item[0],
            'projectName': pro_item[1],
            'remark': pro_item[2],
            'createTime': transform_time(pro_item[3]),
            'creator': pro_item[4]
        }

    # 新增项目
    def add_project(self, user_id, pro_name, remark):
        if pro_name == '':
            res = Result(msg='项目名称不能为空').success()
        else:
            pro_id = self.__create_uuid()
            pro_info = ProjectModel(
                project_id=pro_id, 
                project_name=pro_name,
                remark=remark, 
                creator=user_id
            )
            db.session.add(pro_info)
            db.session.commit()
            res = Result(msg='项目新增成功').success()
        return make_response(res)

    # 获取项目列表
    def get_project_list(self):
        # 获取数据对象
        project_obj = db.session.query(
            ProjectModel.project_id, ProjectModel.project_name, ProjectModel.remark, 
            ProjectModel.create_time, UserModel.username
        ).join(UserModel, ProjectModel.creator == UserModel.user_id)
        # 数据对象进行筛选和排序
        data_obj = project_obj.filter(ProjectModel.is_delete == 0).order_by(ProjectModel.create_time.desc())
        data = [self.__pro_info_serializer(item) for item in data_obj]
        res = Result(data).success()
        return make_response(res)

    # 编辑项目
    def edit_project(self, is_del, pro_id, pro_name, remark):
        pro_info = ProjectModel.query.filter_by(project_id=pro_id).first()
        if pro_info is None:
            res = Result(msg='Project ID 无效，没有查找到对应的项目').fail()
        # 判断是否删除
        elif is_del == 1:
            pro_info.is_delete = 1
            db.session.commit()
            res = Result(msg='项目删除成功').success()
        elif pro_name == '':
            res = Result(msg='项目名称不能为空').fail()
        else:
            pro_info.project_name = pro_name
            pro_info.remark = remark
            db.session.commit()
            res = Result(msg='项目信息修改成功').success()
        return make_response(res)
