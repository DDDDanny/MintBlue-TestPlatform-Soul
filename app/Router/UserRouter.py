# -*- coding: utf-8 -*-
# @Time    : 2020/12/03 17:57:39
# @Author  : DannyDong
# @File    : UserRouter.py
# @Describe: 用户管理相关路由管理

import uuid

from flask_jwt_extended import set_access_cookies
from flask import Blueprint, request, abort, jsonify

from app.Common.Result import Result
from app.Views.User.UserLogin import UserLogin
from app.Views.User.UserRegister import UserRegister


# 声明蓝图
UserBlue = Blueprint('UserBlue', __name__)


@UserBlue.route('/user/register', methods=['POST'])
def user_register():
    """
    Desc: 用户注册
    """
    # 接收前端数据
    form_data = eval(request.get_data(as_text=True))
    # 解析数据
    username, password = form_data['username'], form_data['password']
    data = UserRegister().user_register(username, password)
    return Result(data).success() if data else Result(msg='用户名已存在，请更换用户名').success()


@UserBlue.route('/user/login', methods=['POST'])
def user_login():
    """
    Desc: 用户登录
    """
    # 接收前端数据
    form_data = eval(request.get_data(as_text=True))
    # 解析数据
    username, password = form_data['username'], form_data['password']
    response = UserLogin().user_login(username, password)
    if 'data' in response.json:
        set_access_cookies(response, response.json['data'])
    return response
