#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/10 18:21
# @Author  : xtmin
# @Email   : wangdaomin123@hotmail.com
# @File    : utils.py 
# @Software: PyCharm
import re
import functools
from app import app
from datetime import timedelta
from flask import json, request
from dateutil.parser import parse as d_parse

time_patten = re.compile('^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}$')


def return_code(error_code, msg=None, data=None):
    json_obj = {'code': error_code}
    if error_code != 200:
        app.logger.info(f'<--- ERROR code:{error_code}, msg:{msg} --->')
    else:
        success_return = f' msg: {msg}' if msg else ''
        success_return += f' data: {data}' if data else ''
        app.logger.info(f'<--- SUCCESS code:200, {success_return} --->')

    if msg is not None:
        json_obj['msg'] = msg

    if data is not None:
        json_obj['data'] = data

    json_str = json.dumps(json_obj, ensure_ascii=False)
    return json_str


def trans_time_to_utc_time_str(time_str):
    p_datetime = d_parse(time_str)
    utc_datetime = p_datetime - timedelta(hours=8)
    return utc_datetime.strftime('%Y-%m-%d %H:%M:%S')


def check_time_str(time_str):
    return time_patten.search(time_str)


def log_for_request(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        app.logger.info(f'{request.method} {request.full_path} ({request.remote_addr}) {request.user_agent}')
        return func(*args, **kwargs)

    return wrapper


if __name__ == '__main__':
    print(check_time_str('2019-12-12 08:00'))
