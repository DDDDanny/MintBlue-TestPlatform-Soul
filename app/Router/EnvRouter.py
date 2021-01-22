# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 10:57:01
# @Author  : DannyDong
# @File    : EnvRouter.py
# @Describe: 环境管理相关路由

from flask import Blueprint, request, abort

from flask_jwt_extended import get_jwt_identity, jwt_required

from app.Common.Result import Result
from app.Model.EnvModel import EnvModel
from app.Views.Project.EnvM import EnvM


# 声明蓝图
EnvBlue = Blueprint('EnvBlue', __name__)


@EnvBlue.route('/env/list', methods=['GET'])
@jwt_required
def env_list():
    """
    Desc: 环境参数信息列表接口
    """
    pro_id = request.args.get('proID')
    response = EnvM().get_env_list(pro_id)
    return response


@EnvBlue.route('/env/add', methods=['POST'])
@jwt_required
def env_add():
    """
    Desc: 新增环境信息接口
    """
    form_data = eval(request.get_data(as_text=True))
    pro_id, env_name, base_url = form_data['projectID'], form_data['envName'], form_data['baseURL']
    user_id = get_jwt_identity()
    response = EnvM().add_env(user_id, pro_id, env_name, base_url)
    return response


@EnvBlue.route('/env/edit', methods=['POST'])
@jwt_required
def env_edit():
    """
    Desc: 编辑环境信息接口(删除也用这个接口)
    """
    form_data = eval(request.get_data(as_text=True))
    is_delete = form_data['isDel']
    if is_delete == 0:
        env_id, env_name, base_url = form_data['envID'], form_data['envName'], form_data['baseURL']
    else:
        env_id, env_name, base_url = form_data['envID'], None, None
    response = EnvM().edit_env(is_delete, env_id, env_name, base_url)
    return response
