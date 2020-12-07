# -*- coding: utf-8 -*-
# @Time    : 2020/12/03 15:59:15
# @Author  : DannyDong
# @File    : UserModel.py
# @Describe: 用户Model层

from datetime import datetime

from factory import db


# 用户Model
class UserModel(db.Model):
    # 定义表名
    __tablename__ = 'user'
    # 主键必须要加 unique=True，否则会报错
    user_id = db.Column(db.String(50), primary_key=True, unique=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    create_time = db.Column(db.Date, default=datetime.now)

    # 序列化: 查询一条数据
    def query_one(self):
        res = {
            'userID': self.user_id,
            'userName': self.username,
            'password': self.password,
            'create_time': self.create_time
        }
        return res
