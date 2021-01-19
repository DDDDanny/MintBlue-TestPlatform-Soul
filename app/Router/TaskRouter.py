# -*- coding: utf-8 -*-
# @Time    : 2021/01/19 09:47:23
# @Author  : DannyDong
# @File    : TaskRouter.py
# @Describe: 测试任务相关路由

from flask import Blueprint, request, abort
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.Common.Result import Result
from app.Model.TaskModel import TaskModel
from app.Views.ApiTest.TestTask import TestTask


# 声明蓝图
TaskBlue = Blueprint('TaskBlue', __name__)


@TaskBlue.route('/task/list', methods=['GET'])
def task_list():
    """
    Desc: 测试任务获取列表接口
    """
    response = TestTask().get_task_list()
    return response
