# -*- coding: utf-8 -*-
# @Time    : 2020/12/01 22:45:30
# @Author  : DannyDong
# @File    : ProjectRouter.py
# @Describe: 项目管理相关路由管理

from flask import Blueprint, request, abort
from app.Common.Result import Result

ProjectBlue = Blueprint('ProjectBlue', __name__)


@ProjectBlue.route('/project/add', methods=['POST'])
def add_project():
    data = {
        'projectName': '测试项目',
        'remark': '这是一个备注信息'
    }
    return Result(data).fail()
