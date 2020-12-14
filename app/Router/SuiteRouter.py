# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 10:50:32
# @Author  : DannyDong
# @File    : SuiteRouter.py
# @Describe: 测试集相关路由

from flask import Blueprint, request, abort

from flask_jwt_extended import get_jwt_identity, jwt_required

from app.Common.Result import Result
from app.Model.VersionModel import VersionModel
from app.Views.ApiTest.TestSuite import TestSuite


# 声明蓝图
SuiteBlue = Blueprint('SuiteBlue', __name__)


@SuiteBlue.route('/suite/list', methods=['GET'])
def suite_list():
    """
    Desc: 测试集获取列表接口
    """
    return Result().success()


@SuiteBlue.route('/suite/add', methods=['POST'])
@jwt_required
def suite_add():
    """
    Desc: 新增测试集接口
    """
    form_data = eval(request.get_data(as_text=True))
    suite_name, remark, pro_id = form_data['suiteName'], form_data['remark'], form_data['proID']
    user_id = get_jwt_identity()
    response = TestSuite().add_suite(user_id, suite_name, remark, pro_id)
    return response


@SuiteBlue.route('/suite/edit', methods=['POST'])
def suite_edit():
    """
    Desc: 编辑测试集接口(删除也用这个接口)
    """
    return Result().success()
