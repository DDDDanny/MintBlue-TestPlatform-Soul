# -*- coding: utf-8 -*-
# @Time    : 2020/12/04 14:05:44
# @Author  : DannyDong
# @File    : UserLogin.py
# @Describe: 用户登录业务逻辑

from flask import jsonify, make_response
from flask_jwt_extended import create_access_token

from factory import db
from app.Utils.MD5 import md5_encrypt
from app.Common.Result import Result
from app.Model.UserModel import UserModel


class UserLogin(object):
    def __init__(self):
        pass

    # 查询用户信息
    @staticmethod
    def __query_user_info(username):
        data_obj = UserModel.query.filter_by(username=username).first()
        return data_obj

    # 用户登录逻辑
    def user_login(self, username, password):
        data_obj = self.__query_user_info(username)
        new_pwd = md5_encrypt(password)  # 密码加密
        access_token = None  # 初始化access token
        if username == '' or password == '':
            res = Result(msg='用户名或密码不能为空').fail()
        elif data_obj is None or data_obj.query_one()['password'] != new_pwd:
            res = Result(msg='用户名或者密码错误').fail()
        else:
            data = data_obj.query_one()
            access_token = create_access_token(identity=data['userID'])
            data['access_token'] = access_token
            res = Result(data, '登录成功').success()
        return make_response(res)

    # 用户退出逻辑
    def user_logout(self):
        res = Result(msg='退出成功').success()
        return make_response(res)
