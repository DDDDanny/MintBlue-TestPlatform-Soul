# -*- coding: utf-8 -*-
# @Time    : 2020/12/14 10:16:45
# @Author  : DannyDong
# @File    : TestSuite.py
# @Describe: 测试用例集业务逻辑

import time
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

    # 时间转换
    @staticmethod
    def __transform_time(timeObj):
        return time.strftime("%Y-%m-%d %H:%M:%S", timeObj.timetuple())
    
    # 序列化测试集信息
    def __suite_info_serializer(self, suite_item):
        return {
            'suiteID': suite_item[0],
            'suiteName': suite_item[1],
            'remark': suite_item[2],
            'creator': suite_item[3],
            'proID': suite_item[4],
            'updateTime': self.__transform_time(suite_item[5])
        }

    # 测试用例集列表
    def get_suite_list(self, pro_id):
        sql = ''' select suite_id, suite_name, remark, username, pro_id, update_time from suite 
                left join user on creator=user_id 
                where is_delete = 0 and pro_id = "{}" 
                order by suite.create_time desc; '''.format(pro_id)
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
                suite_id=suite_id, 
                suite_name=suite_name,
                remark=remark,
                creator=user_id,
                pro_id=pro_id
            )
            db.session.add(suite_info)
            db.session.commit()
            db.session.close()
            res = Result(msg='新增用例集成功').success()
        return make_response(res)

    # 编辑测试用例集 (By Zoey)
    def edit_suite(self, suite_id, suite_name, remark, is_delete):
        suite_info = SuiteModel.query.filter_by(suite_id=suite_id).first()
        if suite_info is None:
            res = Result(msg='suiteID无效，没有查到对应的用例集').success()
        elif is_delete == 1:
            suite_info.is_delete = 1
            db.session.commit()
            db.session.close()
            res = Result(msg='测试用例集删除成功').success()
        elif suite_name == '':
            res = Result(msg='测试用例集名称不能为空')
        else:
            suite_info.suite_name = suite_name
            suite_info.remark = remark
            db.session.commit()
            db.session.close()
            res = Result(msg='修改测试用例集成功').success()
        return make_response(res)
