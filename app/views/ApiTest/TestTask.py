# -*- coding: utf-8 -*-
# @Time    : 2021/01/18 16:19:29
# @Author  : DannyDong
# @File    : TestTask.py
# @Describe: 测试任务相关业务逻辑

import time
import uuid
 
from flask import make_response

from factory import db
from app.Common.Result import Result
from app.Model.TaskModel import TaskModel
from app.Utils.TransformTime import transform_time
 
 
class TestTask(object):
    def __init__(self):
        self.status_dict = {0: '未开始', 1: '进行中', 2: '已完成'}
    
    # 生成UUID
    @staticmethod
    def __create_uuid():
        return str(uuid.uuid4())

    # 序列化测试任务信息
    def __task_info_serializer(self, task_item):
        return {
            'taskID': task_item[0],
            'taskName': task_item[1],
            'createTime': transform_time(task_item[2]),
            'startTime': transform_time(task_item[3]),
            'endTime': transform_time(task_item[4]),
            'taskStatus': self.status_dict[task_item[5]],
            'creator': task_item[6],
            'version': task_item[7],
            'caseSuite': task_item[8]
        }

    # 测试任务列表
    def get_task_list(self):
        sql = ''' select task_id, task_name, task.create_time, task_start_time,
                task_end_time, task_status, username, version, suite_name from
                task left join user on creator = user_id left join version on 
                task.ver_id = version.ver_id left join suite on 
                task.suite_id = suite.suite_id '''
        data_obj = db.session.execute(sql)
        data = [self.__task_info_serializer(item) for item in data_obj]
        res = Result(data).success()
        return make_response(res)
