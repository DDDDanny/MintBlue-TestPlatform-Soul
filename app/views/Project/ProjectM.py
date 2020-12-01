# -*- coding: utf-8 -*-
# @Time    : 2020/12/01 22:45:30
# @Author  : DannyDong
# @File    : ProjectM.py
# @Describe: 项目管理业务逻辑

from flask import Blueprint, request, abort
from app.Common.Result import Result

ProjectM = Blueprint('calc', __name__)


@ProjectM.route('/project/add', methods=['POST'])
def calc_money():
    data = {
        'projectName': '测试项目',
        'remark': '这是一个备注信息'
    }
    return Result(data).fail()
