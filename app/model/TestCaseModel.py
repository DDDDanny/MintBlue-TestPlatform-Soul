# -*- coding: utf-8 -*-
# @Time    : 2021/02/27 14:55:03
# @Author  : DannyDong
# @File    : TestCaseModel.py
# @Describe: 测试用例Model

from factory import db


class TestCaseModel(db.Model):
    # 定义表名
    __tablename__ = 'testcase'
    case_id = db.Column(db.String(50), primary_key=True, unique=True)
    case_name = db.Column(db.String(20), nullable=False)
    level = db.Column(db.Integer, nullable=False, default=0)
    method = db.Column(db.Integer, nullable=False, default=0)
    url = db.Column(db.String(200), nullable=False, default=None)
    header = db.Column(db.String(100), nullable=False, default=None)
    body = db.Column(db.Text(500), nullable=True)
    case_assert = db.Column(db.Text(500), nullable=False, default=None)
    forward = db.Column(db.Text(500), nullable=True)
    mock = db.Column(db.Text(500), nullable=True)
    remark = db.Column(db.String(200), nullable=True)
    create_time = db.Column(db.Date, default=datetime.now)
    creator = db.Column(db.String(50), db.ForeignKey('user.user_id'), nullable=False)
    pro_id = db.Column(db.String(50), db.ForeignKey('project.project_id'), nullable=False)
