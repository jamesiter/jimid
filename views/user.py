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
        ret['paging'] = {'total': 0, 'offset': offset, 'limit': limit, 'page': page, 'page_size': page_size}

        ret['data'], ret['paging']['total'] = User.get_list(offset=offset, limit=limit, order_by=order_by, order=order)

        for i in range(ret['data'].__len__()):
            del ret['data'][i]['password']

        return ret
    except ji.PreviewingError, e:
        return json.loads(e.message)


# 不支持用户自我更新, 用户更新各字段, 将有专门的接口
@Utils.dumps2response
@Utils.superuser
def r_update():

    user = User()

    args_rules = [
        Rules.ID.value
    ]

    if 'login_name' in request.json:
        args_rules.append(
            Rules.LOGIN_NAME.value
        )

    if 'mobile_phone' in request.json:
        args_rules.append(
            Rules.MOBILE_PHONE.value
        )

    if 'mobile_phone_verified' in request.json:
        args_rules.append(
            Rules.MOBILE_PHONE_VERIFIED.value
        )

    if 'email' in request.json:
        args_rules.append(
            Rules.EMAIL.value
        )

    if 'email_verified' in request.json:
        args_rules.append(
            Rules.EMAIL_VERIFIED.value
        )

    if args_rules.__len__() < 2:
        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        return ret

    request.json['id'] = request.json.get('id', 0).__str__()
    try:
        ji.Check.previewing(args_rules, request.json)
        user.id = int(request.json.get('id'))
        user.get()

        user.login_name = request.json.get('login_name', user.login_name)
        user.mobile_phone = request.json.get('mobile_phone', user.mobile_phone)
        user.mobile_phone_verified = request.json.get('mobile_phone_verified', user.mobile_phone_verified)
        user.email = request.json.get('email', user.email)
        user.email_verified = request.json.get('email_verified', user.email_verified)

        user.update()
    except ji.PreviewingError, e:
        return json.loads(e.message)


