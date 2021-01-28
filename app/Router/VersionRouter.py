# -*- coding: utf-8 -*-
# @Time    : 2020/12/09 10:39:10
# @Author  : DannyDong
# @File    : VersionRouter.py
# @Describe: 版本管理相关路由

from flask import Blueprint, request, abort

from flask_jwt_extended import get_jwt_identity, jwt_required

from app.Common.Result import Result
from app.Model.VersionModel import VersionModel
from app.Views.Project.VersionM import VersionM


# 声明蓝图
VersionBlue = Blueprint('VersionBlue', __name__)


@VersionBlue.route('/version/list', methods=['GET'])
def version_list():
    """
    Desc: 版本信息列表接口
    """
    pro_id = request.args.get('proID')
    response = VersionM().get_version_list(pro_id)
    return response


@VersionBlue.route('/version/add', methods=['POST'])
@jwt_required
def version_add():
    """
    Desc: 新增版本信息接口
    """
    form_data = eval(request.get_data(as_text=True))
    pro_id, version, remark = form_data['projectID'], form_data['version'], form_data['remark']
    user_id = get_jwt_identity() 
    response = VersionM().add_version(user_id, pro_id, version, remark)
    return response


@VersionBlue.route('/version/edit', methods=['POST'])
def version_edit():
    """
    Desc: 编辑项目信息接口(删除也用这个接口)
    """
    form_data = eval(request.get_data(as_text=True))
    is_delete, ver_id = form_data['isDel'], form_data['versionID']
    if is_delete == 0:
        version, remark = form_data['version'], form_data['remark']
    else:
        version, remark = None, None
    response = VersionM().edit_version(is_delete, ver_id, version, remark)
    return response
