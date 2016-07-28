#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
from flask import Blueprint, request, g, make_response
import jimit as ji

from models import Utils, Rules, Auth


__author__ = 'James Iter'
__date__ = '16/6/8'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


blueprint = Blueprint(
    'auth',
    __name__,
    url_prefix='/auth'
)


@Utils.dumps2response
def r_sign_up():

    auth = Auth()

    args_rules = [
        Rules.LOGIN_NAME.value,
        Rules.PASSWORD.value
    ]
    auth.login_name = request.json.get('login_name')
    auth.password = request.json.get('password')

    try:
        ji.Check.previewing(args_rules, auth.__dict__)
        auth.password = ji.Security.ji_pbkdf2(auth.password)
        auth.create()
        auth.get_by_login_name()
        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        ret['data'] = auth.__dict__
        del ret['data']['password']
        return ret
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
def r_sign_in():

    auth = Auth()

    args_rules = [
        Rules.LOGIN_NAME.value,
        Rules.PASSWORD.value
    ]
    auth.login_name = request.json.get('login_name')
    auth.password = request.json.get('password')

    try:
        ji.Check.previewing(args_rules, auth.__dict__)
        plain_password = auth.password
        auth.get_by_login_name()

        if not ji.Security.ji_pbkdf2_check(password=plain_password, password_hash=auth.password):
            ret = dict()
            ret['state'] = ji.Common.exchange_state(40101)
            ret['state']['sub']['zh-cn'] = ''.join([ret['state']['sub']['zh-cn'], u': 鉴权失败'])
            raise ji.PreviewingError(json.dumps(ret, ensure_ascii=False))

        token = Utils.generate_token(auth.id)
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
    auth = Auth()

    args_rules = [
        Rules.ID.value
    ]
    auth.id = g.token.get('uid', 0).__str__()

    try:
        ji.Check.previewing(args_rules, auth.__dict__)
        auth.id = long(auth.id)
        auth.get()
        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        ret['data'] = auth.__dict__
        del ret['data']['password']
        return ret
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
def r_change_password():

    auth = Auth()

    args_rules = [
        Rules.ID.value
    ]
    auth.id = g.token.get('uid', 0).__str__()

    try:
        ji.Check.previewing(args_rules, auth.__dict__)
        auth.get()
    except ji.PreviewingError, e:
        return json.loads(e.message)

    args_rules = [
        Rules.PASSWORD.value
    ]
    auth.password = request.json.get('password')

    try:
        ji.Check.previewing(args_rules, auth.__dict__)
        auth.password = ji.Security.ji_pbkdf2(auth.password)
        auth.update()
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
def r_auth():
    auth = Auth()

    args_rules = [
        Rules.ID.value
    ]
    auth.id = g.token.get('uid', 0).__str__()

    try:
        ji.Check.previewing(args_rules, auth.__dict__)
        auth.id = long(auth.id)
        auth.get()
        if not auth.enabled:
            ret = dict()
            ret['state'] = ji.Common.exchange_state(40301)
            raise ji.PreviewingError(json.dumps(ret, ensure_ascii=False))

    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_get_list():
    page = str(request.args.get('page', 1))
    page_size = str(request.args.get('page_size', 50))

    args_rules = [
        Rules.PAGE.value,
        Rules.PAGE_SIZE.value
    ]

    try:
        ji.Check.previewing(args_rules, {'page': page, 'page_size': page_size})
    except ji.PreviewingError, e:
        return json.loads(e.message)

    page = int(page)
    page_size = int(page_size)

    # 把page和page_size换算成offset和limit
    offset = (page - 1) * page_size
    # offset, limit将覆盖page及page_size的影响
    offset = str(request.args.get('offset', offset))
    limit = str(request.args.get('limit', page_size))

    order_by = request.args.get('order_by', 'id')
    order = request.args.get('order', 'asc')

    args_rules = [
        Rules.OFFSET.value,
        Rules.LIMIT.value,
        Rules.ORDER_BY.value,
        Rules.ORDER.value
    ]

    try:
        ji.Check.previewing(args_rules, {'offset': offset, 'limit': limit, 'order_by': order_by, 'order': order})
        offset = int(offset)
        limit = int(limit)
        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        ret['data'] = list()
        ret['paging'] = {'total': 0, 'offset': offset, 'limit': limit}

        ret['data'], ret['paging']['total'] = Auth.get_list(offset=offset, limit=limit, order_by=order_by, order=order)
        return ret
    except ji.PreviewingError, e:
        return json.loads(e.message)
