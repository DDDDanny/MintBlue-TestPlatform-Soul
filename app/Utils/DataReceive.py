# -*- coding: utf-8 -*-
# @Time    : 2021/3/13 17:40
# @Author  : DannyDong
# @File    : DataReceive.py
# @describe: 数据接收解析


class DataReceive(object):
    def __init__(self, data_dict):
        self.dict = data_dict

    def data_resolve(self):
        """
        此方法用于数据解析，入参是个字典类型数据
        self.dict：存放Https请求数据
        """
        data_list = []
        try:
            data_list.append(self.dict['method'])
            data_list.append(self.dict['header'])
            data_list.append(self.dict['url'])
            data_list.append(self.dict['body'])
            data_list.append(self.dict['assert'])
            data_list.append(self.dict['judge'])
        except Exception as e:
            raise Exception('请求数据解析错误', e)
        return data_list
