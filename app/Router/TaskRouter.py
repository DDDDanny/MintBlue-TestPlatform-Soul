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
@jwt_required
def task_list():
    """
    Desc: 测试任务获取列表接口
    """
    pro_id = request.args.get('proID')
    response = TestTask().get_task_list(pro_id)
    return response


@TaskBlue.route('/task/add', methods=['POST'])
@jwt_required
def add_task():
    """
    Desc: 新增测试任务接口
    """
    form_data = eval(request.get_data(as_text=True))
    task_name, suite_id, ver_id = form_data['taskName'], form_data['suiteID'], form_data['verID']
    env_id, pro_id, start_time = form_data['envID'], form_data['proID'], form_data['startTime']
    user_id = get_jwt_identity()
    response = TestTask().add_task_info(task_name, suite_id, ver_id, env_id, start_time, pro_id, user_id)
    return response


@TaskBlue.route('/task/del', methods=['POST'])
@jwt_required
def del_task():
    """
    Desc: 删除测试任务接口
    """
    form_data = eval(request.get_data(as_text=True))
    task_id = form_data['taskID']
    response = TestTask().del_task_info(task_id)
    return response
