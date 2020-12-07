# -*- coding: utf-8 -*-
# @Time    : 2020/12/03 17:57:39
# @Author  : DannyDong
# @File    : UserRouter.py
# @Describe: 用户管理相关路由管理

import uuid

from flask import Blueprint, request
from flask_jwt_extended import set_access_cookies, jwt_required, get_jwt_identity
from flask_jwt_extended import unset_jwt_cookies

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
    response = UserRegister().user_register(username, password)
    return response


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
    if 'data' in response[0].json:
        set_access_cookies(response[0], response[1])
    return response[0]


@UserBlue.route('/user/logout', methods=['POST'])
# @get_jwt_identity
def logout():
    """
    Desc: 用户登出
    """
    response = UserLogin().user_logout()
    unset_jwt_cookies(response)
    # user_id = get_jwt_identity()
    return response
