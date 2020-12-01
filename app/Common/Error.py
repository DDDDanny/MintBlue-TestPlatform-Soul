# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 15:11:44
# @Author  : DannyDong
# @File    : Error.py
# @Describe: 异常处理

from Common import bp
from Common.Result import Result

from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

# 错误请求处理
def error_response(error_code, errMsg=None):
    payload = {
        'error_code': error_code,
        'error': HTTP_STATUS_CODES.get(error_code, 'Unknown Error')
    }
    if errMsg:
        payload['errMsg'] = errMsg
    
    return Result(data=payload, msg='请求错误').fail()


# 处理404错误
@bp.errorhandler(404)
def handle_404_error(error):
    return error_response(404)

# 处理500错误
@bp.errorhandler(500)
def handle_500_error(error):
    return error_response(500)