# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 10:57:01
# @Author  : DannyDong
# @File    : EnvRouter.py
# @Describe: 环境管理相关路由

from flask import Blueprint, request, abort

from flask_jwt_extended import get_jwt_identity, jwt_required

from app.Common.Result import Result
from app.Model.EnvModel import EnvModel


# 声明蓝图
EnvBlue = Blueprint('EnvBlue', __name__)


@EnvBlue.route('/env/list', methods=['GET'])
def env_list():
    """
    Desc: 环境参数信息列表接口
    """
    return Result().success()


@EnvBlue.route('/env/add', methods=['POST'])
def env_add():
    """
    Desc: 新增环境信息接口
    """
    return Result().success()


@EnvBlue.route('/env/edit', methods=['POST'])
def env_edit():
    """
    Desc: 编辑环境信息接口(删除也用这个接口)
    """
    return Result().success()