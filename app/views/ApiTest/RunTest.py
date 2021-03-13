# -*- coding: utf-8 -*-
# @Time    : 2021/03/13 17:31:29
# @Author  : DannyDong
# @File    : RunTest.py
# @Describe: 用例执行逻辑

from app.Utils import DataReceive


# 测试执行类
class RunTest(object):
    def __init__(self, data, cookie):
        self.data_list = DataReceive(data).data_resolve()
        self.cookie = cookie

    # 处理前置条件
    def case_forward(self):
        pass

    # 用例执行逻辑
    def run(self):
        pass
