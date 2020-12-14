# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 17:43:43
# @Author  : DannyDong
# @File    : SuiteModel.py
# @Describe: 测试集Model层

from datetime import datetime

from factory import db


# 测试集Model层
class SuiteModel(db.Model):
    # 定义表名
    __tablename__ = 'suite'
    suite_id = db.Column(db.String(50), primary_key=True, unique=True)
    suite_name = db.Column(db.String(30), nullable=False)
    remark = db.Column(db.String(50))
    is_delete = db.Column(db.Integer, nullable=False, default=0)
    create_time = db.Column(db.Date, default=datetime.now)
    update_time = db.Column(db.Date, default=datetime.now, onupdate=datetime.now)
    pro_id = db.Column(db.String(50), db.ForeignKey('project.project_id'), nullable=False)
    creator = db.Column(db.String(50), db.ForeignKey('user.user_id'), nullable=False)
