# -*- coding: utf-8 -*-
# @Time    : 2020/12/14 10:16:45
# @Author  : DannyDong
# @File    : TestSuite.py
# @Describe: 测试用例集业务逻辑

import uuid

from flask import make_response

from factory import db
from app.Common.Result import Result
from app.Model.SuiteModel import SuiteModel


class TestSuite(object):
    def __init__(self):
        pass

    # 生成UUID
    @staticmethod
    def __create_uuid():
        return str(uuid.uuid4())
    
    # 序列化测试集信息
    @staticmethod
    def __suite_info_serializer(suite_item):
        return {
            'suiteID': suite_item[0],
            'suiteName': suite_item[1],
            'remark': suite_item[2],
            'creator': suite_item[3],
            'proID': suite_item[4],
            'updateTime': suite_item[5]
        }

    # 测试用例集列表
    def get_suite_list(self, pro_id):
        sql = 'select suite_id, suite_name, remark, username, pro_id, update_time from suite ' \
              'left join user on creator=user_id where pro_id = "{}"'.format(pro_id)
        data_obj = db.session.execute(sql)
        data = [self.__suite_info_serializer(item) for item in data_obj]
        res = Result(data).success()
        return make_response(res)

    # 测试用例集新增
    def add_suite(self, user_id, suite_name, remark, pro_id):
        if suite_name == '':
            res = Result(msg='项目名称不能为空').success()
        else:
            suite_id = self.__create_uuid()
            suite_info = SuiteModel(
                suite_id=suite_id, suite_name=suite_name,
                remark=remark, creator=user_id,
                pro_id=pro_id
            )
            db.session.add(suite_info)
            db.session.commit()
            db.session.close()
            res = Result(msg='新增用例集成功').success()
        return make_response(res)