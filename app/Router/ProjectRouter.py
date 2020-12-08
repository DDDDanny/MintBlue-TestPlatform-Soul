# -*- coding: utf-8 -*-
# @Time    : 2020/12/01 22:45:30
# @Author  : DannyDong
# @File    : ProjectRouter.py
# @Describe: 项目管理相关路由管理

from flask import Blueprint, request, abort

from flask_jwt_extended import get_jwt_identity, jwt_required

from app.Common.Result import Result
from app.Model.ProjectModel import ProjectModel
from app.Views.Project.ProjectM import ProjectM


# 声明蓝图
ProjectBlue = Blueprint('ProjectBlue', __name__)


@ProjectBlue.route('/project/list', methods=['GET'])
@jwt_required
def project_list():
    """
    Desc: 项目列表接口
    """
    response = ProjectM().get_project_list()
    return response


@ProjectBlue.route('/project/add', methods=['POST'])
@jwt_required
def project_add():
    """
    Desc: 新增项目接口
    """
    form_data = eval(request.get_data(as_text=True))
    pro_name, remark = form_data['projectName'], form_data['remark']
    user_id = get_jwt_identity()
    response = ProjectM().add_project(user_id, pro_name, remark)
    return response


@ProjectBlue.route('/project/edit', methods=['POST'])
def project_edit():
    """
    Desc: 编辑项目接口、删除项目（逻辑删除）也用这个接口
    """
    return Result().success()
