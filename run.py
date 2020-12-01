# -*- coding: utf-8 -*-
# @Time    : 2020/12/01 15:44:11
# @Author  : DannyDong
# @File    : run.py
# @Describe: flask应用入口

from factory import create_app


if __name__ == "__main__":
    app = create_app()
    app.run()
