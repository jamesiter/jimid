#!/usr/bin/env python
# -*- coding: utf-8 -*-


import traceback
import thread
import sys
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
from views.user_mgmt import blueprint as mgmt_blueprint
from views.user_mgmt import blueprints as mgmts_blueprint
from views.app import blueprint as app_blueprint
from views.app import blueprints as apps_blueprint
from views.openid import blueprint as openid_blueprint
from views.openid import blueprints as openids_blueprint
from views.openid_mgmt import blueprint as openid_admin_blueprint
from views.openid_mgmt import blueprints as openids_admin_blueprint
from views.role import blueprint as role_blueprint
from views.role import blueprints as roles_blueprint


__author__ = 'James Iter'
__date__ = '16/6/8'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


# 替换为Flask-Session
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=app.config['PERMANENT_SESSION_LIFETIME'])
app.config['SESSION_FILE_DIR'] = '/'.join([sys.path[0], app.config['SESSION_FILE_DIR']])
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
                # 如果该用户获取失败，则清除该用户对应的session。因为该用户可能已经被删除。
                for key in session.keys():
                    session.pop(key=key)
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
        # https://developer.mozilla.org/en/HTTP_access_control
        # (中文版) https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Access_control_CORS#Access-Control-Allow-Credentials
        # http://www.w3.org/TR/cors/
        # 由于浏览器同源策略，凡是发送请求url的协议、域名、端口三者之间任意一与当前页面地址不同即为跨域。

        if request.referrer is None:
            # 跑测试脚本时，用该规则。
            response.headers['Access-Control-Allow-Origin'] = '*'
        else:
            # 生产环境中，如果前后端分离。那么请指定具体的前端域名地址，不要用如下在开发环境中的便捷方式。
            # -- Access-Control-Allow-Credentials为true，携带cookie时，不允许Access-Control-Allow-Origin为通配符，是浏览器对用户的一种安全保护。
            # -- 至少能避免登录山寨网站，骗取用户相关信息。
            response.headers['Access-Control-Allow-Origin'] = '/'.join(request.referrer.split('/')[:3])

        response.headers['Access-Control-Allow-Credentials'] = 'true'
        response.headers['Access-Control-Allow-Methods'] = 'HEAD, GET, POST, DELETE, OPTIONS, PATCH, PUT'
        response.headers['Access-Control-Allow-Headers'] = 'X-Request-With, Content-Type'
        response.headers['Access-Control-Expose-Headers'] = 'Set-Cookie'

        # 少于session生命周期一半时,自动对其续期
        if not is_not_need_to_auth(request.endpoint) and hasattr(g, 'token') and \
                g.token['exp'] < (ji.Common.ts() + (app.config['token_ttl'] / 2)):
            token = Utils.generate_token(g.token['uid'])
            # 清除原有session，由新session代替
            for key in session.keys():
                session.pop(key=key)
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
    app.register_blueprint(app_blueprint)
    app.register_blueprint(apps_blueprint)
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
