# -*- coding: utf-8 -*-
# @Time    : 2020/12/01 15:39:55
# @Author  : DannyDong
# @File    : factory.py
# @Describe: flask工厂函数

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 工厂函数
def create_app():
    # 实例化Flask
    app = Flask(__name__)
    # 处理跨域
    CORS(app, supports_credentials=True)
    # 初始化各种扩展库
    db.init_app(app)
    # 蓝图注册写在这里
    #
    #
    return app
