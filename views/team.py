#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/10 18:12
# @Author  : xtmin
# @Email   : wangdaomin123@hotmail.com
# @File    : team.py 
# @Software: PyCharm
import utils
from . import view
from flask import request
from app import mongo, app


@view.route('/get/match/team', methods=['GET'])
@utils.log_for_request
def match_team():
    team_name = request.values.get('team_name')
    match_time = request.values.get('match_time')
    app.logger.debug(f'team_name: {team_name}, match_time: {match_time}')

    if not team_name or not match_time:
        return utils.return_code(500, msg='参数错误')
    if not utils.check_time_str(match_time):
        return utils.return_code(500, msg='时间格式不正确')

    match_time = utils.trans_time_to_utc_time_str(match_time)
    team_info = mongo.db.team_info.find_one({'team_name': team_name, 'match_time': match_time})
    if not team_info:
        return utils.return_code(500, msg='对不起，指定信息不存在')

    return_data = {
        'team_name': team_info.get('team_name') or '',
        'lineup_players': team_info.get('lineup_player') or [],
        'injurie_players': team_info.get('injure_players') or []
    }
    return utils.return_code(200, data=return_data)
