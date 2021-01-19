# -*- coding: utf-8 -*-
# @Time    : 2021/01/18 15:41:31
# @Author  : DannyDong
# @File    : TaskModel.py
# @Describe: 测试任务Model层

from datetime import datetime

from factory import db


# 测试任务Model
class TaskModel(db.Model):
    # 定义表名
    __tablename__ = 'task'
    task_id = db.Column(db.String(50), primary_key=True, unique=True)
    task_name = db.Column(db.String(6), nullable=False)
    create_time = db.Column(db.Date, default=datetime.now)
    task_start_time = db.Column(db.Date) 
    task_end_time = db.Column(db.Date)
    task_status = db.Column(db.Integer, nullable=False, default=0)
    creator = db.Column(db.String(50), db.ForeignKey('user.user_id'), nullable=False)
    pro_id = db.Column(db.String(50), db.ForeignKey('project.project_id'), nullable=False)
    env_id = db.Column(db.String(50), db.ForeignKey('env.env_id'), nullable=False)
    suite_id = db.Column(db.String(50), db.ForeignKey('suite.suite_id'), nullable=False)
    ver_id = db.Column(db.String(50), db.ForeignKey('version.ver_id'), nullable=False)
