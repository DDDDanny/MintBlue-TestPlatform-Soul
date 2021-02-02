# -*- coding: utf-8 -*-
# @Time    : 2021/01/21 14:30:02
# @Author  : DannyDong
# @File    : TransformTime.py
# @Describe: 时间转换工具

import time

def transform_time(datetime_Obj):
    """
    datetime to YYYY-MM-DD HH:mm:SS
    """    
    return time.strftime("%Y-%m-%d %H:%M:%S", datetime_Obj.timetuple())


def time_stamp_transform(datetime_obj):
    """
    时间戳转时间
    """
    # 转化成时间结构体，并且转化成秒
    time_struct = time.localtime(datetime_obj // 1000)
    # 格式化输出
    new_time = time.strftime("%Y-%m-%d %H:%M:%S", time_struct)
    return new_time
