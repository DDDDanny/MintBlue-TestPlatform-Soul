# -*- coding: utf-8 -*-
# @Time    : 2021/01/21 14:30:02
# @Author  : DannyDong
# @File    : TransformTime.py
# @Describe: 时间转换工具

import time

# datetime to YYYY-MM-DD HH:mm:SS
def transform_time(datetime_Obj):
    return time.strftime("%Y-%m-%d %H:%M:%S", datetime_Obj.timetuple())
