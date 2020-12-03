# -*- coding: utf-8 -*-
# @Time    : 2020/12/02 17:54:59
# @Author  : DannyDong
# @File    : ProjectModel.py
# @Describe: 项目Model层

from factory import db


# 项目Model
class ProjectModel(db.Model):
    # 定义表名
    __tablename__ = 'project'
    project_id = db.Column(db.String(50), primary_key=True)
    project_name = db.Column(db.String(20), unique=True)
    remark = db.Column(db.String(50))
    create_time = db.Column(db.Date)
    creator = db.Column(db.String(50))

    def query_one(self):
        """
        序列化
        查询一条数据
        """
        res = {
            'projectID': self.project_id,
            'projectName': self.project_name,
            'remark': self.remark,
            'createTime': self.create_time,
            'creator': self.creator
        }
        return res
