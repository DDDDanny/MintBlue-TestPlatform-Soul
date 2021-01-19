# -*- coding: utf-8 -*-
# @Time    : 2021/01/18 14:10:50
# @Author  : DannyDong
# @File    : ApiTestReport.py
# @Describe: 接口测试报告相关业务逻辑

import time
import uuid

from flask import make_response

from factory import db
from app.Common.Result import Result
from app.Model.ApiTestReportModel import ApiTestReportModel


class ApiTestReport(object):
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

    # 序列化测试任务信息
    def __api_test_report_serializer(self, report_item):
        return {
            'reportID': report_item[0],
            'reprotName': report_item[1],
            'success': report_item[2],
            'fail': report_item[3],
            'createTime': self.__transform_time(report_item[4]),
            'proID': report_item[5],
            'taskID': report_item[6],
            'version': report_item[7]
        }
    
    # 接口测试报告列表
    def get_api_test_report_list(self):
        sql = ''' select report_id, report_name, success, fail, api_report.create_time,
                api_report.pro_id, api_report.task_id, version from api_report 
                left join task on api_report.task_id = task.task_id
                left join version on task.ver_id = version.ver_id '''
        data_obj = db.session.execute(sql)
        data = [self.__api_test_report_serializer(item) for item in data_obj]
        res = Result(data).success()
        return make_response(res)
