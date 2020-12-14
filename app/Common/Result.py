# -*- coding: utf-8 -*-
# @Time    : 2020/10/22 23:12
# @Author  : DannyDong
# @File    : Result.py
# @describe: 封装处理请求结果

from app.Common.Constant import SUCCESS_CODE, ERROR_CODE


class Result(object):
    def __init__(self, data=None, msg='请求成功'):
        """
        构造函数，初始化数据
        :param data: Response Data
        :param msg: Response Message
        """
        self.data = data
        self.msg = msg
        self.code = SUCCESS_CODE

    # 生产Response结果
    def create_result(self):
        base = {
            'code': self.code,
            'msg': self.msg
        }
        if self.data is not None:
            base['data'] = self.data
        return base

    # 成功
    def success(self):
        self.code = SUCCESS_CODE
        return self.create_result()

    # 失败
    def fail(self):
        self.code = ERROR_CODE
        return self.create_result()


if __name__ == '__main__':
    Result().success()
