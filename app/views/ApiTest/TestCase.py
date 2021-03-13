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
from app.Model.TestCaseModel import TestCaseModel
from app.Utils.TransformTime import transform_time


class TestCase(object):
    def __init__(self):
        pass

    # 生成UUID
    @staticmethod
    def __create_uuid():
        return str(uuid.uuid4())

    # 序列化测试集信息
    def __case_info_serializer(self, case_item):
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
        sql = ''' select case_id, case_name, level, method, req_url, remark, 
                testcase.create_time, username from testcase 
                left join user on creator=user_id where pro_id = "{}" 
                order by testcase.create_time desc; '''.format(pro_id)
        data_obj = db.session.execute(sql)
        data = [self.__case_info_serializer(item) for item in data_obj]
        res = Result(data).success()
        return make_response(res)
