# -*- coding: utf-8 -*-
# @Time    : 2020/12/01 15:39:55
# @Author  : DannyDong
# @File    : factory.py
# @Describe: flask工厂函数

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


db = SQLAlchemy()
jwt = JWTManager()


def register_center(app):
    """
    desc: 注册中心
    """
    # 解决无法引用db的问题，可能是循环依赖导致的
    from app.Common.Error import handle_404_error, handle_500_error, handle_401_error
    from app.Router.ProjectRouter import ProjectBlue
    from app.Router.UserRouter import UserBlue
    from app.Router.VersionRouter import VersionBlue

    # 注册异常处理方法
    app.register_error_handler(401, handle_401_error)
    app.register_error_handler(404, handle_404_error)
    app.register_error_handler(500, handle_500_error)
    # 蓝图注册写在这里
    app.register_blueprint(ProjectBlue, url_prefix='/api/v1')
    app.register_blueprint(UserBlue, url_prefix='/api/v1')
    app.register_blueprint(VersionBlue, url_prefix='/api/v1')


def create_app():
    """
    desc：工厂函数
    """
    # 实例化Flask
    app = Flask(__name__)
    # 处理跨域
    CORS(app, supports_credentials=True)
    # 配置数据库信息
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456.@127.0.0.1:3306/mintblue_auto_test'
    # 禁止数据的修改追踪(需要消耗资源)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    # Only allow JWT cookies to be sent over https. 
    # In production, this should likely be True
    app.config['JWT_COOKIE_SECURE'] = False
    app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/v1'
    # app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh'
    app.config['JWT_COOKIE_CSRF_PROTECT'] = True
    # Set the secret key to sign the JWTs with
    app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
    # 初始化各种扩展库
    db.init_app(app)
    jwt = JWTManager(app)
    # 蓝图注册中心
    register_center(app)

    return app
