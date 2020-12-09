# -*- coding: utf-8 -*-
# @Time    : 2020/12/09 10:39:10
# @Author  : DannyDong
# @File    : VersionRouter.py
# @Describe: 版本管理相关路由

from flask import Blueprint, request, abort

from flask_jwt_extended import get_jwt_identity, jwt_required

from app.Common.Result import Result
from app.Model.VersionModel import VersionModel


# 声明蓝图
VersionBlue = Blueprint('VersionBlue', __name__)


@VersionBlue.route('/version/list', methods=['GET'])
def version_list():
    """
    Desc: 版本信息列表接口
    """
    return Result().success()


@VersionBlue.route('/version/add', methods=['POST'])
def version_add():
    """
    Desc: 新增版本信息接口
    """
    return Result().success()


@VersionBlue.route('/version/edit', methods=['POST'])
def version_edit():
    """
    Desc: 编辑项目信息接口(删除也用这个接口)
    """
    return Result().success()