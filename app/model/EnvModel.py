# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 10:29:44
# @Author  : DannyDong
# @File    : EnvModel.py
# @Describe: 环境参数Model层

from datetime import datetime

from factory import db


# 环境参数Model
class EnvModel(db.Model):
    # 定义表名
    __tablename__ = 'env'
    env_id = db.Column(db.String(50), primary_key=True, unique=True)
    env_name = db.Column(db.String(15), nullable=False)
    base_url = db.Column(db.String(50), nullable=False)
    create_time = db.Column(db.Date, default=datetime.now)
    pro_id = db.Column(db.String(50), db.ForeignKey('project.project_id'), nullable=False)
