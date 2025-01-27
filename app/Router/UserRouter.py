# -*- coding: utf-8 -*-
# @Time    : 2020/12/03 17:57:39
# @Author  : DannyDong
# @File    : UserRouter.py
# @Describe: 用户管理相关路由管理

import uuid

from flask import Blueprint, request
from flask_jwt_extended import set_access_cookies, unset_jwt_cookies

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
    return response


@UserBlue.route('/user/logout', methods=['POST'])
def logout():
    """
    Desc: 用户登出
    """
    response = UserLogin().user_logout()
    return response
