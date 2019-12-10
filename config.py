#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/10 17:45
# @Author  : xtmin
# @Email   : wangdaomin123@hotmail.com
# @File    : config.py
# @Software: PyCharm


class Config:
    APP_PORT = 5000  # web服务端口
    NUM_PROCESSES = 4  # 启动进程数
    SECRET_KEY = '2M8Sa6NGy8Sqcc57TEtaQz6n6iVEsUHE'
    MONGO_URI = 'mongodb://localhost:27017/rotowire'
    LOG_FILE = 'flask.log'
    LOG_FORMAT = '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s'
