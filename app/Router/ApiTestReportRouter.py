# -*- coding: utf-8 -*-
# @Time    : 2021/01/19 14:29:22
# @Author  : DannyDong
# @File    : ApiTestReportRouter.py
# @Describe: 接口测试报告相关路由

from flask import Blueprint, request, abort
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.Common.Result import Result
from app.Model.ApiTestReportModel import ApiTestReportModel
from app.Views.Reports.ApiTestReport import ApiTestReport


# 声明蓝图
ApiTestReportBlue = Blueprint('ApiTestReportBlue', __name__)


@ApiTestReportBlue.route('/apiReport/list', methods=['GET'])
def api_test_report():
    """
    Desc: 获取Api测试报告列表接口
    """
    response = ApiTestReport().get_api_test_report_list()
    return response
