#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
from flask import Blueprint, request, g, make_response
import jimit as ji

from models import Utils, Rules, User


__author__ = 'James Iter'
__date__ = '16/6/8'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


blueprint = Blueprint(
    'user',
    __name__,
    url_prefix='/user'
)


@Utils.dumps2response
def r_sign_up():

    user = User()

    args_rules = [
        Rules.LOGIN_NAME.value,
        Rules.PASSWORD.value
    ]
    user.login_name = request.json.get('login_name')
    user.password = request.json.get('password')

    try:
        ji.Check.previewing(args_rules, user.__dict__)
        user.password = ji.Security.ji_pbkdf2(user.password)
        user.create()
        user.get_by_login_name()
        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        ret['data'] = user.__dict__
        del ret['data']['password']
        return ret
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
def r_sign_in():

    user = User()

    args_rules = [
        Rules.LOGIN_NAME.value,
        Rules.PASSWORD.value
    ]
    user.login_name = request.json.get('login_name')
    user.password = request.json.get('password')

    try:
        ji.Check.previewing(args_rules, user.__dict__)
        plain_password = user.password
        user.get_by_login_name()

        if not ji.Security.ji_pbkdf2_check(password=plain_password, password_hash=user.password):
            ret = dict()
            ret['state'] = ji.Common.exchange_state(40101)
            ret['state']['sub']['zh-cn'] = ''.join([ret['state']['sub']['zh-cn'], u': 鉴权失败'])
            raise ji.PreviewingError(json.dumps(ret, ensure_ascii=False))

        token = Utils.generate_token(user.id)
        rep = make_response()
        rep.set_cookie('token', token)
        rep.data = json.dumps({'state': ji.Common.exchange_state(20000)}, ensure_ascii=False)
        return rep

    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
def r_sign_out():
    rep = make_response()
    rep.delete_cookie('token')
    return rep


@Utils.dumps2response
def r_get():
    user = User()

    args_rules = [
        Rules.ID.value
    ]
    user.id = g.token.get('uid', 0).__str__()

    try:
        ji.Check.previewing(args_rules, user.__dict__)
        user.id = long(user.id)
        user.get()
        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        ret['data'] = user.__dict__
        del ret['data']['password']
        return ret
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
def r_change_password():

    user = User()

    args_rules = [
        Rules.ID.value
    ]
    user.id = g.token.get('uid', 0).__str__()

    try:
        ji.Check.previewing(args_rules, user.__dict__)
        user.get()
    except ji.PreviewingError, e:
        return json.loads(e.message)

    args_rules = [
        Rules.PASSWORD.value
    ]
    user.password = request.json.get('password')

    try:
        ji.Check.previewing(args_rules, user.__dict__)
        user.password = ji.Security.ji_pbkdf2(user.password)
        user.update()
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
def r_auth():
    user = User()

    args_rules = [
        Rules.ID.value
    ]
    user.id = g.token.get('uid', 0).__str__()

    try:
        ji.Check.previewing(args_rules, user.__dict__)
        user.id = long(user.id)
        user.get()
        if not user.enabled:
            ret = dict()
            ret['state'] = ji.Common.exchange_state(40301)
            raise ji.PreviewingError(json.dumps(ret, ensure_ascii=False))

    except ji.PreviewingError, e:
        return json.loads(e.message)


