#!/usr/bin/env python
# -*- coding: utf-8 -*-


import traceback
import thread
import json
from flask import request, g, make_response
from flask import session
from flask.ext.session import Session
from datetime import timedelta
import jimit as ji

from models.initialize import app, logger
import route_table
from models import Database as db
from models import Utils
from models import User
from views.user import blueprint as user_blueprint
from views.mgmt import blueprint as mgmt_blueprint
from views.mgmt import blueprints as mgmts_blueprint
from views.app_key import blueprint as app_key_blueprint
from views.app_key import blueprints as app_keys_blueprint
from views.openid import blueprint as openid_blueprint
from views.openid import blueprints as openids_blueprint
from views.openid_admin import blueprint as openid_admin_blueprint
from views.openid_admin import blueprints as openids_admin_blueprint
from views.role import blueprint as role_blueprint
from views.role import blueprints as roles_blueprint


__author__ = 'James Iter'
__date__ = '16/6/8'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


# 替换为Flask-Session
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=app.config['PERMANENT_SESSION_LIFETIME'])
Session(app)


def is_not_need_to_auth(endpoint):
    not_auth_table = [
        'user.r_sign_up',
        'user.r_sign_up_by_mobile_phone',
        'user.r_sign_up_by_email',
        'user.r_sign_in',
        'user.r_sign_in_by_mobile_phone',
        'user.r_sign_in_by_email'
    ]
    if endpoint in not_auth_table:
        return True
    return False


@app.before_request
@Utils.dumps2response
def r_before_request():
    try:
        if not is_not_need_to_auth(request.endpoint) and request.blueprint is not None and request.method != 'OPTIONS':
            token = session.get('token', '')
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

            # 如果账号禁用,则删除token
            if not auth.enabled:
                ret = dict()
                ret['state'] = ji.Common.exchange_state(40301)
                for key in session.keys():
                    session.pop(key=key)
                response = make_response()
                response.data = json.dumps(ret, ensure_ascii=False)
                response.status_code = int(ret['state']['code'])
                return response

    except ji.JITError, e:
        ret = json.loads(e.message)
        if ret['state']['sub']['code'] in ['41208']:
            ret['redirect'] = {
                # 非官方的,专为解决jquery ajax 302跳转问题,由民间开发者普遍认可的一个代替码。
                # 参考链接: http://hunterford.me/how-to-handle-http-redirects-with-jquery-and-django/
                'code': '278',
                'location': request.host_url + 'login.html'
            }

        return ret


@app.after_request
@Utils.dumps2response
def r_after_request(response):
    try:
        # 由于浏览器同源策略，凡是发送请求url的协议、域名、端口三者之间任意一与当前页面地址不同即为跨域。
        response.headers['Access-Control-Allow-Origin'] = '/'.join(request.referrer.split('/')[:3])
        # response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        response.headers['Access-Control-Allow-Methods'] = 'HEAD, GET, POST, DELETE, OPTIONS, PATCH, PUT'
        response.headers['Access-Control-Allow-Headers'] = 'X-Request-With, Content-Type'
        response.headers['Access-Control-Expose-Headers'] = 'Set-Cookie'

        # 少于token生命周期一半时,自动对其续期
        if not is_not_need_to_auth(request.endpoint) and hasattr(g, 'token') and \
                        g.token['exp'] < (ji.Common.ts() + (app.config['token_ttl'] / 2)):
            token = Utils.generate_token(g.token['uid'])
            session['token'] = token
        return response
    except ji.JITError, e:
        return json.loads(e.message)


# noinspection PyBroadException
try:
    db.init_conn()
    thread.start_new_thread(db.keepalived, ())

    app.register_blueprint(user_blueprint)
    app.register_blueprint(mgmt_blueprint)
    app.register_blueprint(mgmts_blueprint)
    app.register_blueprint(app_key_blueprint)
    app.register_blueprint(app_keys_blueprint)
    app.register_blueprint(openid_blueprint)
    app.register_blueprint(openids_blueprint)
    app.register_blueprint(openid_admin_blueprint)
    app.register_blueprint(openids_admin_blueprint)
    app.register_blueprint(role_blueprint)
    app.register_blueprint(roles_blueprint)
except:
    logger.error(traceback.format_exc())

if __name__ == '__main__':
    # noinspection PyBroadException
    try:
        app.run(host='127.0.0.1', port=7001, use_reloader=False, threaded=True)
    except:
        logger.error(traceback.format_exc())
