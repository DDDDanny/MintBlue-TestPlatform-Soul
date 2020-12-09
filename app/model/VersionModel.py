# -*- coding: utf-8 -*-
# @Time    : 2020/12/09 10:20:55
# @Author  : DannyDong
# @File    : VersionModel.py
# @Describe: 版本信息Model层

from datetime import datetime

from factory import db


# 版本信息Model
class VersionModel(db.Model):
    # 定义表名
    __tablename__ = 'version'
    ver_id = db.Column(db.String(50), primary_key=True, unique=True)
    version = db.Column(db.String(15), nullable=False)
    remark = db.Column(db.String(50))
    is_delete = db.Column(db.Integer, nullable=False, default=0)
    create_time = db.Column(db.Date, default=datetime.now)
    pro_id = db.Column(db.String(50), db.ForeignKey('project.project_id'), nullable=False)
