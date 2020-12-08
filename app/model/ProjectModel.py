# -*- coding: utf-8 -*-
# @Time    : 2020/12/02 17:54:59
# @Author  : DannyDong
# @File    : ProjectModel.py
# @Describe: 项目Model层

from datetime import datetime

from factory import db


# 项目Model
class ProjectModel(db.Model):
    # 定义表名
    __tablename__ = 'project'
    project_id = db.Column(db.String(50), primary_key=True)
    project_name = db.Column(db.String(20), unique=True)
    remark = db.Column(db.String(50))
    is_delete = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.Date, default=datetime.now)
    creator = db.Column(db.String(50), db.ForeignKey('user.user_id'), nullable=False)

    # 序列化: 查询一条数据
    def query_one(self):
        res = {
            'projectID': self.project_id,
            'projectName': self.project_name,
            'remark': self.remark,
            'createTime': self.create_time,
            'creator': self.creator
        }
        return res
