# -*- coding: utf-8 -*-
# @Time    : 2021/02/27 15:32:51
# @Author  : DannyDong
# @File    : TestCaseRouter.py
# @Describe: 测试用例相关路由

from flask import Blueprint, request, abort

from flask_jwt_extended import get_jwt_identity, jwt_required

from app.Common.Result import Result
from app.Model.TestCaseModel import TestCaseModel
from app.Views.ApiTest.TestCase import TestCase


# 声明蓝图
TestCaseBlue = Blueprint('TestCaseBlue', __name__)


@TestCaseBlue.route('/testcase/list', methods=['GET'])
def testcase_list():
    """
    Desc: 获取测试用例列表接口
    """
    pro_id = request.args.get('proID')
    response = TestCase().get_case_list(pro_id)
    return response


@TestCaseBlue.route('/testcase/add', methods=['POST'])
def testcase_add():
    """
    Desc: 新增测试用例接口
    """
    pass


@TestCaseBlue.route('/testcase/edit', methods=['POST'])
def testcase_edit():
    """
    Desc: 编辑测试用例接口
    """
    pass


@TestCaseBlue.route('/testcase/del', methods=['POST'])
def testcase_del():
    """
    Desc: 删除测试用例接口
    """
    pass
