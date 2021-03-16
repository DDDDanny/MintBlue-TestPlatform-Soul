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
from app.Model.VersionModel import VersionModel
from app.Model.TaskModel import TaskModel
from app.Model.ApiTestReportModel import ApiTestReportModel as ARM
from app.Utils.TransformTime import transform_time


class ApiTestReport(object):
    def __init__(self):
        pass
    
    # 生成UUID
    @staticmethod
    def __create_uuid():
        return str(uuid.uuid4())

    # 序列化测试任务信息
    def __api_test_report_serializer(self, report_item):
        return {
            'reportID': report_item[0],
            'reportName': report_item[1],
            'successNum': report_item[2],
            'failNum': report_item[3],
            'createTime': transform_time(report_item[4]),
            'proID': report_item[5],
            'taskID': report_item[6],
            'version': report_item[7]
        }
    
    # 接口测试报告列表
    def get_api_test_report_list(self, pro_id):
        # 获取数据对象
        report_obj = db.session.query(
            ARM.report_id, ARM.report_name, ARM.success, ARM.fail, ARM.create_time,
            ARM.pro_id, ARM.task_id, VersionModel.version
        ).join(
            TaskModel, TaskModel.task_id == ARM.task_id
        ).join(
            VersionModel, VersionModel.ver_id == TaskModel.ver_id
        )
        # 数据对象进行筛选和排序
        data_obj = report_obj.filter(ARM.pro_id == pro_id).order_by(ARM.create_time.desc())
        data = [self.__api_test_report_serializer(item) for item in data_obj]
        res = Result(data).success()
        return make_response(res)
