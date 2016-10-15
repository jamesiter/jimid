#!/usr/bin/env python
# -*- coding: utf-8 -*-


import traceback
import thread
import json
from flask import request, g, make_response
import jimit as ji

from models.initialize import app, logger
import route_table
from models import Database as db
from models import Utils
from models import User
from views.user import blueprint as auth_blueprint
from views.mgmt import blueprint as mgmt_blueprint
from views.mgmt import blueprints as mgmts_blueprint


__author__ = 'James Iter'
__date__ = '16/6/8'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


def is_not_need_to_auth(endpoint):
    not_auth_table = [
        'user.r_sign_up',
        'user.r_sign_in'
    ]
    if endpoint in not_auth_table:
        return True
    return False


@app.before_request
@Utils.dumps2response
def r_before_request():
    try:
        if not is_not_need_to_auth(request.endpoint) and request.method != 'OPTIONS':
            token = request.cookies.get('token', '')
            g.token = Utils.verify_token(token)
            g.superuser = False
            if g.token['uid'] == 1:
                g.superuser = True

            auth = User()
            auth.id = g.token['uid']

            try:
                auth.get()
            except ji.PreviewingError, e:
                return json.loads(e.message)

            # 如果账号禁用,则删除客户端token
            if not auth.enabled:
                ret = dict()
                ret['state'] = ji.Common.exchange_state(40301)
                response = make_response()
                response.delete_cookie('token')
                response.data = json.dumps(ret, ensure_ascii=False)
                response.status_code = int(ret['state']['code'])
                return response

    except ji.JITError, e:
        return json.loads(e.message)


@app.after_request
@Utils.dumps2response
def r_after_request(response):
    try:
        # 由于浏览器同源策略，凡是发送请求url的协议、域名、端口三者之间任意一与当前页面地址不同即为跨域。
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        response.headers['Access-Control-Allow-Methods'] = 'HEAD, GET, POST, DELETE, OPTIONS, PATCH, PUT'
        response.headers['Access-Control-Allow-Headers'] = 'X-Request-With, Content-Type'
        response.headers['Access-Control-Expose-Headers'] = 'Set-Cookie'

        # 分两个if语句, 是因为即使r_before_request无法通过, 但还是会走r_after_request流程, 整个请求周期不会因为r_before_request的异常而跳过r_after_request
        if not is_not_need_to_auth(request.endpoint) and hasattr(g, 'token') and \
                        g.token['exp'] < (ji.Common.ts() + (app.config['token_ttl'] / 2)):
            token = Utils.generate_token(g.token['uid'])
            response.set_cookie('token', token)
        return response
    except ji.JITError, e:
        return json.loads(e.message)


# noinspection PyBroadException
try:
    db.init_conn()
    thread.start_new_thread(db.keepalived, ())

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(mgmt_blueprint)
    app.register_blueprint(mgmts_blueprint)
except:
    logger.error(traceback.format_exc())

if __name__ == '__main__':
    # noinspection PyBroadException
    try:
        app.run(host='127.0.0.1', port=7001, use_reloader=False, threaded=True)
    except:
        logger.error(traceback.format_exc())
