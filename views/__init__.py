#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/10 18:12
# @Author  : xtmin
# @Email   : wangdaomin123@hotmail.com
# @File    : __init__.py.py 
# @Software: PyCharm
from flask import Blueprint

view = Blueprint('view', __name__)

from .team import *
