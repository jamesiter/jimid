#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
from flask import Blueprint, request, g, make_response
import urllib
import jimit as ji

from models import Utils, Rules, AppKey, UidOpenidMapping


__author__ = 'James Iter'
__date__ = '2016/11/5'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


blueprint = Blueprint(
    'openid',
    __name__,
    url_prefix='/openid'
)

blueprints = Blueprint(
    'openids',
    __name__,
    url_prefix='/openids'
)


def exchange_302(state_code, attach=None, secret=''):
    if attach is None:
        attach = dict()

    ret = dict()
    ret['state'] = ji.Common.exchange_state(state_code)
    ret['redirect'] = {
        'code': '302',
        'location': request.args['redirect_url'].split('?', 1)
    }

    attach['code'] = state_code.__str__()
    if ret['redirect']['location'].__len__() == 2:
        for item in ret['redirect']['location'][1].split('&'):
            kv = item.split('=', 1)
            attach[kv[0]] = kv[1]

    sign = ji.Security.ji_hash_sign(algorithm='sha1', secret=secret, content=attach)
    attach['sign'] = sign

    url_parm = list()
    for k, v in attach.items():
        url_parm.append('='.join([k, v]))

    url_parm = '&'.join(url_parm)

    ret['redirect']['location'] = ''.join([ret['redirect']['location'][0], '?', url_parm])

    return ret


@Utils.dumps2response
def r_sign_up():
    """
    JimID服务主动生成openid给资源服务器
    """

    # 所有必须参数得到满足,才去认真对待该请求。即,当所有必须参数满足后,才把返回结果通过302重定向传给资源服务器。
    # 在必须参数没有得到满足的情况下,直接把结果抛给请求的客户端。
    args_rules = [
        Rules.APP_ID_EXT.value,
        Rules.TS.value,
        Rules.SIGN.value,
        Rules.REDIRECT_URL.value
    ]

    try:
        ji.Check.previewing(args_rules, request.args)
    except ji.PreviewingError, e:
        return json.loads(e.message)

    app_key = AppKey()
    openid = UidOpenidMapping()

    # 校验appid及获取appid对应的secret
    app_key.id = request.args['appid']

    if app_key.exist():
        app_key.get()
    else:
        # 此处比较特殊,如果appid不存在,则使用空字符串作为签名秘钥
        return exchange_302(state_code=40450)

    # TODO: 校验重定向的资源服务器地址,是否是合法、有效、备案过的地址(域名或IP).避免被用作让客户端去攻击其它服务器;
    # 通过secret校验签名
    # TODO: 加入判断时间戳的逻辑,时间范围由配置文件指定
    needs = ['appid', 'ts', 'redirect_url']
    args = dict()
    for k in needs:
        args[k] = urllib.quote_plus(request.args[k])

    args['method'] = request.method.upper()
    args['base_url'] = request.base_url

    sign = ji.Security.ji_hash_sign(algorithm='sha1', secret=app_key.secret, content=args)

    if sign != request.args['sign']:
        return exchange_302(state_code=41250, secret=app_key.secret)

    # 判断该用户是否已经在该appid下绑定过openid
    openid.uid = g.token.get('uid', 0).__str__()
    openid.appid = app_key.id

    try:
        if openid.exist():
            openid.get()
            return exchange_302(state_code=40901, attach={'openid': openid.openid}, secret=app_key.secret)
        else:
            openid.openid = ji.Common.generate_random_code(length=30)
            openid.create()
            openid.get()
            return exchange_302(state_code=20000, attach={'openid': openid.openid}, secret=app_key.secret)
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
def r_bind():
    """
    接受资源服务器主动提供的openid
    """

    # 所有必须参数得到满足,才去认真对待该请求。即,当所有必须参数满足后,才把返回结果通过302重定向传给资源服务器。
    # 在必须参数没有得到满足的情况下,直接把结果抛给请求的客户端。
    args_rules = [
        Rules.APP_ID_EXT.value,
        Rules.OPENID.value,
        Rules.TS.value,
        Rules.SIGN.value,
        Rules.REDIRECT_URL.value
    ]

    try:
        ji.Check.previewing(args_rules, request.args)
    except ji.PreviewingError, e:
        return json.loads(e.message)

    app_key = AppKey()
    openid = UidOpenidMapping()

    # 校验appid及获取appid对应的secret
    app_key.id = request.args['appid']

    if app_key.exist():
        app_key.get()
    else:
        # 此处比较特殊,如果appid不存在,则使用空字符串作为签名秘钥
        return exchange_302(state_code=40450)

    # TODO: 校验重定向的资源服务器地址,是否是合法、有效、备案过的地址(域名或IP).避免被用作让客户端去攻击其它服务器;

    # 通过secret校验签名
    # TODO: 加入判断时间戳的逻辑,时间范围由配置文件指定
    needs = ['appid', 'openid', 'ts', 'redirect_url']
    args = dict()
    for k in needs:
        args[k] = urllib.quote_plus(request.args[k])

    args['method'] = request.method.upper()
    args['base_url'] = request.base_url

    sign = ji.Security.ji_hash_sign(algorithm='sha1', secret=app_key.secret, content=args)

    if sign != request.args['sign']:
        return exchange_302(state_code=41250, secret=app_key.secret)

    # 判断该用户是否已经在该appid下绑定过openid
    openid.uid = g.token.get('uid', 0).__str__()
    openid.appid = app_key.id

    try:
        if openid.exist():
            openid.get()
            return exchange_302(state_code=40901, attach={'openid': openid.openid}, secret=app_key.secret)
        else:
            openid.openid = request.args['openid']
            openid.create()
            openid.get()
            return exchange_302(state_code=20000, attach={'openid': openid.openid}, secret=app_key.secret)
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
def r_unbind():
    """
    解除已绑定的openid
    """

    # 所有必须参数得到满足,才去认真对待该请求。即,当所有必须参数满足后,才把返回结果通过302重定向传给资源服务器。
    # 在必须参数没有得到满足的情况下,直接把结果抛给请求的客户端。
    args_rules = [
        Rules.APP_ID_EXT.value,
        Rules.TS.value,
        Rules.SIGN.value,
        Rules.REDIRECT_URL.value
    ]

    try:
        ji.Check.previewing(args_rules, request.args)
    except ji.PreviewingError, e:
        return json.loads(e.message)

    app_key = AppKey()
    openid = UidOpenidMapping()

    # 校验appid及获取appid对应的secret
    app_key.id = request.args['appid']

    if app_key.exist():
        app_key.get()
    else:
        # 此处比较特殊,如果appid不存在,则使用空字符串作为签名秘钥
        return exchange_302(state_code=40450)

    # TODO: 校验重定向的资源服务器地址,是否是合法、有效、备案过的地址(域名或IP).避免被用作让客户端去攻击其它服务器;

    # 通过secret校验签名
    # TODO: 加入判断时间戳的逻辑,时间范围由配置文件指定
    needs = ['appid', 'ts', 'redirect_url']
    args = dict()
    for k in needs:
        args[k] = urllib.quote_plus(request.args[k])

    args['method'] = request.method.upper()
    args['base_url'] = request.base_url

    sign = ji.Security.ji_hash_sign(algorithm='sha1', secret=app_key.secret, content=args)

    if sign != request.args['sign']:
        return exchange_302(state_code=41250, secret=app_key.secret)

    # 判断该用户是否已经在该appid下绑定过openid
    openid.uid = g.token.get('uid', 0).__str__()
    openid.appid = app_key.id

    try:
        if openid.exist():
            openid.delete()
            return exchange_302(state_code=20000, secret=app_key.secret)
        else:
            return exchange_302(state_code=40401, secret=app_key.secret)
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
def r_auth():
    """
    帮资源服务器验证,对应appid下该用户是否合法,如果验证通过,则携带用户对应的openid返回到资源服务器
    """

    # 所有必须参数得到满足,才去认真对待该请求。即,当所有必须参数满足后,才把返回结果通过302重定向传给资源服务器。
    # 在必须参数没有得到满足的情况下,直接把结果抛给请求的客户端。
    args_rules = [
        Rules.APP_ID_EXT.value,
        Rules.TS.value,
        Rules.SIGN.value,
        Rules.REDIRECT_URL.value
    ]

    try:
        ji.Check.previewing(args_rules, request.args)
    except ji.PreviewingError, e:
        return json.loads(e.message)

    app_key = AppKey()
    openid = UidOpenidMapping()

    # 校验appid及获取appid对应的secret
    app_key.id = request.args['appid']

    if app_key.exist():
        app_key.get()
    else:
        # 此处比较特殊,如果appid不存在,则使用空字符串作为签名秘钥
        return exchange_302(state_code=40450)

    # TODO: 校验重定向的资源服务器地址,是否是合法、有效、备案过的地址(域名或IP).避免被用作让客户端去攻击其它服务器;

    # 通过secret校验签名
    # TODO: 加入判断时间戳的逻辑,时间范围由配置文件指定
    needs = ['appid', 'ts', 'redirect_url']
    args = dict()
    for k in needs:
        args[k] = urllib.quote_plus(request.args[k])

    args['method'] = request.method.upper()
    args['base_url'] = request.base_url

    sign = ji.Security.ji_hash_sign(algorithm='sha1', secret=app_key.secret, content=args)

    if sign != request.args['sign']:
        return exchange_302(state_code=41250, secret=app_key.secret)

    # 判断该用户是否已经在该appid下绑定过openid
    openid.uid = g.token.get('uid', 0).__str__()
    openid.appid = app_key.id

    try:
        if openid.exist():
            openid.get()
            return exchange_302(state_code=20000, attach={'openid': openid.openid}, secret=app_key.secret)
        else:
            return exchange_302(state_code=40401, secret=app_key.secret)
    except ji.PreviewingError, e:
        return json.loads(e.message)

