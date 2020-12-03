# -*- coding: utf-8 -*-
# @Time    : 2020/12/03 15:59:15
# @Author  : DannyDong
# @File    : UserModel.py
# @Describe: 用户Model层

from factory import db


# 用户Model
class UserModel(db.Model):
    # 定义表名
    __tablename__ = 'user'
    user_id = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def query_one(self):
        """
        序列化: 查询一条数据
        """
        res = {
            'userID': self.user_id,
            'userName': self.username,
            'password': self.password
        }
        return res
