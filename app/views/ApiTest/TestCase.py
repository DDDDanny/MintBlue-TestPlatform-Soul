# -*- coding: utf-8 -*-
# @Time    : 2021/03/13 16:09:51
# @Author  : DannyDong
# @File    : TestCase.py
# @Describe: 测试用例业务逻辑

import time
import uuid

from flask import make_response

from factory import db
from app.Common.Result import Result
from app.Model.TestCaseModel import TestCaseModel as TCM
from app.Model.UserModel import UserModel
from app.Utils.TransformTime import transform_time


class TestCase(object):
    def __init__(self):
        pass

    # 生成UUID
    @staticmethod
    def __create_uuid():
        return str(uuid.uuid4())

    # 序列化测试集信息
    @staticmethod
    def __case_info_serializer(case_item):
        return {
            'caseID': case_item[0],
            'caseName': case_item[1],
            'caseLevel': case_item[2],
            'requestMethod': case_item[3],
            'requestUrl': case_item[4],
            'remark': case_item[5],
            'updateTime': transform_time(case_item[6]),
            'creator': case_item[7]
        }

    # 测试用例列表
    def get_case_list(self, pro_id):
        # 获取数据对象
        case_obj = db.session.query(
            TCM.case_id, TCM.case_name, TCM.level, TCM.method, TCM.req_url, TCM.remark,
            TCM.create_time, UserModel.username
        ).join(UserModel, UserModel.user_id == TCM.creator)
        # 数据对象进行筛选和排序
        data_obj = case_obj.filter(TCM.pro_id == pro_id).order_by(TCM.create_time.desc())
        data = [self.__case_info_serializer(item) for item in data_obj]
        res = Result(data).success()
        return make_response(res)
