# -*- coding: utf-8 -*-
# @Time    : 2020/12/01 22:45:30
# @Author  : DannyDong
# @File    : ProjectRouter.py
# @Describe: 项目管理相关路由管理

from flask import Blueprint, request, abort
from app.Common.Result import Result

ProjectBlue = Blueprint('ProjectBlue', __name__)


@ProjectBlue.route('/project/list', methods=['GET'])
def project_list():
    """
    Desc: 项目列表接口
    """
    return Result().success()


@ProjectBlue.route('/project/add', methods=['POST'])
def project_add():
    """
    Desc: 新增项目接口
    """
    data = {
        'projectName': '测试项目',
        'remark': '这是一个备注信息'
    }
    return Result(data).fail()


@ProjectBlue.route('/project/edit', methods=['POST'])
def project_edit():
    """
    Desc: 编辑项目接口、删除项目（逻辑删除）也用这个接口
    """
    return Result().success()