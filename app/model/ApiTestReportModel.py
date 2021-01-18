# -*- coding: utf-8 -*-
# @Time    : 2021/01/18 14:12:03
# @Author  : DannyDong
# @File    : ApiTestReportModel.py
# @Describe: 接口测试报告Model层

from datetime import datetime

from factory import db


# 接口测试报告Model
class ApiTestReportModel(db.Model):
    # 定义表名
    __tablename__ = 'api_report'
    report_id = db.Column(db.String(50), primary_key=True, unique=True)
    report_name = db.Column(db.String(100), nullable=False)
    success = db.Column(db.Integer, nullable=False, default=0)
    fail = db.Column(db.Integer, nullable=False, default=0)
    create_time = db.Column(db.Date, default=datetime.now)
    pro_id = db.Column(db.String(50), db.ForeignKey('project.project_id'), nullable=False)
    task_id = db.Column(db.String(50), db.ForeignKey('task.task_id'), nullable=False)
