# -*- coding: utf-8 -*-
# @Time    : 2021/3/13 17:50
# @Author  : DannyDong
# @File    : Request.py
# @describe: 二次封装requests库

import requests


class Request(object):
    def __init__(self, header, url, cookie=None, timeout=5):
        self.header = header
        self.url = url
        self.cookie = cookie
        self.timeout = timeout

    @staticmethod
    # 获取Response数据方法
    def get_response_data(result):
        # time_milli为响应时间，单位为毫秒
        time_milli = result.elapsed.microseconds / 1000
        # time_seconds为响应时间，单位为秒
        time_seconds = result.elapsed.total_seconds()
        response_dict = dict()
        try:
            response_dict['body'] = result.json()
        except Exception as e:
            raise Exception('请求Response错误:', e)
        response_dict['code'] = result.status_code
        response_dict['time_milli'] = time_milli
        response_dict['time_seconds'] = time_seconds
        response_dict['cookies'] = result.cookies
        return response_dict

    # Post请求
    def post_request(self, json):
        try:
            if self.cookie is None:
                result = requests.request(
                    method='POST', url=self.url, headers=self.header, json=json, timeout=self.timeout
                )
            else:
                result = requests.request(
                    method='POST', url=self.url, headers=self.header, json=json, cookies=self.cookie, timeout=self.timeout
                )
        except Exception as e:
            raise Exception('Post请求错误：', e)
        return self.get_response_data(result)

    # Get请求
    def get_request(self, params):
        try:
            result = requests.request(
                method='GET', url=self.url, headers=self.header, params=params,
                cookies=self.cookie, timeout=self.timeout
            )
        except Exception as e:
            raise Exception('Get请求错误:', e)
        return self.get_response_data(result)

    # Pull请求
    def pull_request(self):
        pass

    # Delete请求
    def delete_request(self):
        pass
