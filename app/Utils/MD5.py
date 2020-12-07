# -*- coding: utf-8 -*-
# @Time    : 2020/12/07 15:01:40
# @Author  : DannyDong
# @File    : MD5.py
# @Describe: 密码加密工具

import hashlib

# MD5加密（message-digest algorithm 5 信息-摘要算法）
def md5_encrypt(wait_str) -> str:
    md5_obj = hashlib.md5(bytes('AutoTest', encoding='utf-8'))  # 加盐后会在原md5加密上再进行一次加密
    md5_obj.update(wait_str.encode('utf-8'))  # 需要转成bytes字节符
    return md5_obj.hexdigest()
