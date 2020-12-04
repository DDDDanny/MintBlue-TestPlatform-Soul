# -*- coding: utf-8 -*-
# @Time    : 2020/12/04 14:05:17
# @Author  : DannyDong
# @File    : UserRegister.py
# @Describe: 用户注册业务逻辑

import uuid

from factory import db
from app.Model.UserModel import UserModel


class UserRegister(object):
    def __init__(self):
        pass

    # 生成UUID
    def create_uuid(self):
        return str(uuid.uuid4())
    
    # 查询用户信息
    def query_user_info(self, username):
        data_obj = UserModel.query.filter_by(username=username).first()
        return data_obj

    # 用户注册逻辑
    def user_register(self, username, password):
        if self.query_user_info(username) is not None:
            return {}
        # 新增用户信息
        user_id = self.create_uuid()
        user_info = UserModel(user_id=user_id, username=username, password=password)
        db.session.add(user_info)
        db.session.commit()
        # 查询获取对象信息
        data_obj = UserModel.query.filter_by(user_id=user_id).first()
        data = data_obj.query_one()
        return data
