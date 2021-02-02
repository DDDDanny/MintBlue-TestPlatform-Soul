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
from app.Utils.TransformTime import transform_time, time_stamp_transform
 
 
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
            'startTime': time_stamp_transform(task_item[3]),
            'endTime': time_stamp_transform(task_item[4]),
            'taskStatus': self.status_dict[task_item[5]],
            'creator': task_item[6],
            'version': task_item[7],
            'caseSuite': task_item[8]
        }

    # 测试任务列表
    def get_task_list(self, pro_id):
        sql = ''' select task_id, task_name, task.create_time, task_start_time,
                task_end_time, task_status, username, version, suite_name from
                task left join user on creator = user_id left join version on 
                task.ver_id = version.ver_id left join suite on 
                task.suite_id = suite.suite_id where task.pro_id="{}"
                order by task.create_time desc; '''.format(pro_id)
        data_obj = db.session.execute(sql)
        data = [self.__task_info_serializer(item) for item in data_obj]
        res = Result(data).success()
        return make_response(res)

    # 新增任务信息
    def add_task_info(self, task_name, suite_id, ver_id, env_id, start_time, pro_id, user_id):
        if task_name == '':
            res = Result(msg='任务名称不能为空').success()
        else:
            task_id = self.__create_uuid()
            task_info = TaskModel(
                task_id=task_id,
                task_name=task_name,
                suite_id=suite_id,
                ver_id=ver_id,
                env_id=env_id,
                pro_id=pro_id,
                creator=user_id,
                task_status=0,
                task_start_time=start_time,
                task_end_time=start_time
            )
            db.session.add(task_info)
            db.session.commit()
            db.session.close()
            res = Result(msg='新增测试任务成功').success()
        return make_response(res)

    # 删除任务信息
    def del_task_info(self, task_id):
        task_info = TaskModel.query.filter_by(task_id=task_id).first()
        if task_info is None:
            res = Result(msg='taskID无效，没有查找到对应的任务信息').success()
        else:
            db.session.delete(task_info)
            db.session.commit()
            res = Result(msg='删除测试任务成功').success()
        return make_response(res)
