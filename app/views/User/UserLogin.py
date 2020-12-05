# -*- coding: utf-8 -*-
# @Time    : 2020/12/04 14:05:44
# @Author  : DannyDong
# @File    : UserLogin.py
# @Describe: 用户登录业务逻辑

from flask import jsonify, make_response
from flask_jwt_extended import create_access_token, get_jwt_identity

from factory import db
from app.Common.Result import Result
from app.Model.UserModel import UserModel


class UserLogin(object):
    def __init__(self):
        pass

    @staticmethod
    def __query_user_info(username):
        data_obj = UserModel.query.filter_by(username=username).first()
        return data_obj

    def user_login(self, username, password):
        data_obj = self.__query_user_info(username)
        if username == '' or password == '':
            res = Result(msg='用户名或密码不能为空').success()
        elif data_obj is None or data_obj.query_one()['password'] != password:
            res = Result(msg='用户名或者密码错误').success()
        else:
            user_id = data_obj.query_one()['userID']
            access_token = create_access_token(identity=user_id)
            res = Result(access_token).success()
        return make_response(res)
