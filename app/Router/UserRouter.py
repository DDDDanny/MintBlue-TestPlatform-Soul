# -*- coding: utf-8 -*-
# @Time    : 2020/12/03 17:57:39
# @Author  : DannyDong
# @File    : UserRouter.py
# @Describe: 用户管理相关路由管理

import uuid

from flask import Blueprint, request, abort

from factory import db
from app.Common.Result import Result
from app.Model.UserModel import UserModel


# 声明蓝图
UserBlue = Blueprint('UserBlue', __name__)


@UserBlue.route('/user/register', methods=['POST'])
def user_register():
    """
    Desc: 用户注册
    """
    # 生成UUID
    user_id = str(uuid.uuid4())
    # 新增用户信息
    user_info = UserModel(user_id=user_id, username='admin', password='admin')
    db.session.add(user_info)
    db.session.commit()
    # 查询获取对象信息
    data_Obj = UserModel.query.filter_by(user_id=user_id).first()
    data = data_Obj.query_one()
    return Result(data).success()


@UserBlue.route('/user/login', methods=['POST'])
def user_login():
    """
    Desc: 用户登录
    """
    return Result().success()
