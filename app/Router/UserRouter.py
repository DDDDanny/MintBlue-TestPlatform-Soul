# -*- coding: utf-8 -*-
# @Time    : 2020/12/03 17:57:39
# @Author  : DannyDong
# @File    : UserRouter.py
# @Describe: 用户管理相关路由管理

from flask import Blueprint, request, abort

from app.Common.Result import Result
from app.Model.UserModel import UserModel


# 声明蓝图
UserBlue = Blueprint('UserBlue', __name__)


@UserBlue.route('/user/register', methods=['GET'])
def user_register():
    """
    Desc: 用户注册
    """
    return Result().success()


@UserBlue.route('/user/login', methods=['POST'])
def user_login():
    """
    Desc: 用户登录
    """
    return Result().success()