# -*- coding: utf-8 -*-
# @Time    : 2020/12/01 15:39:55
# @Author  : DannyDong
# @File    : factory.py
# @Describe: flask工厂函数

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from app.Common import bp
from app.Common.Error import handle_404_error, handle_500_error
from app.Router.ProjectRouter import ProjectBlue

db = SQLAlchemy()

# 工厂函数
def create_app():
    # 实例化Flask
    app = Flask(__name__)
    # 处理跨域
    CORS(app, supports_credentials=True)
    # 配置数据库信息
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin@127.0.0.1:3306/mintblue_auto_test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # 初始化各种扩展库
    db.init_app(app)
    # 注册异常处理方法
    app.register_error_handler(404, handle_404_error)
    app.register_error_handler(500, handle_500_error)
    # 蓝图注册写在这里
    app.register_blueprint(ProjectBlue, url_prefix='/api/v1')

    return app
