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


def exchange_302(state_code, attach=None):
    if attach is None:
        attach = dict()

    ret = dict()
    ret['state'] = ji.Common.exchange_state(state_code)
    ret['redirect'] = {
        'code': '302',
        'location': request.args['redirect_url'].split('?', 1)
    }

    if ret['redirect']['location'].__len__() < 2:
        ret['redirect']['location'] = urllib.quote_plus(''.join([ret['redirect']['location'][0], '?',
                                                                 'state=', json.dumps(ret['state'])]))
    else:
        ret['redirect']['location'] = urllib.quote_plus(''.join([
            ret['redirect']['location'][0], '?', ret['redirect']['location'][1],
            '&state=', json.dumps(ret['state'])]))

    ret.update(attach)
    return ret


@Utils.dumps2response
def r_sign_up():
    """
    JimID服务主动生成openid给资源服务器
    """

    # 所有必须参数得到满足,才去认真对待该请求。即,当所有必须参数满足后,才把返回结果通过302重定向传给资源服务器。
    # 在必须参数没有得到满足的情况下,直接把结果抛给请求的客户端。
    args_rules = [
        Rules.APP_ID.value,
        Rules.OPENID.value,
        Rules.TS.value,
        Rules.SIGN.value,
        Rules.REDIRECT_URL.value
    ]

    try:
        ji.Check.previewing(args_rules, request.args)
    except ji.PreviewingError, e:
        return json.loads(e.message)

    # TODO: 校验重定向的资源服务器地址,是否是合法、有效、备案过的地址(域名或IP).避免被用作让客户端去攻击其它服务器;

    app_key = AppKey()
    openid = UidOpenidMapping()

    # 校验appid及获取appid对应的secret
    app_key.id = request.args['appid']

    if app_key.exist():
        app_key.get()
    else:
        return exchange_302(41250)

    # 通过secret校验签名
    # TODO: 加入判断时间戳的逻辑,时间范围由配置文件指定
    needs = ['appid', 'ts', 'redirect_url']
    args = dict()
    for k in needs:
        args[k] = urllib.quote_plus(request.args[k])

    sign = ji.Security.ji_hash_sign(algorithm='sha1', secret=app_key.secret, content=args)

    if sign != request.args['sign']:
        return exchange_302(41250)

    # 判断该用户是否已经在该appid下绑定过openid
    openid.uid = g.token.get('uid', 0).__str__()
    openid.appid = app_key.id

    try:
        if openid.exist():
            openid.get()
            return exchange_302(40901, {'data': {'openid': openid.openid}})
        else:
            openid.openid = ji.Common.generate_random_code(length=30)
            openid.create()
            openid.get()
            return exchange_302(20000, {'data': {'openid': openid.openid}})
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_bind(_id):
    """
    接受资源服务器主动提供的openid
    """
    app_key = UidOpenidMapping()

    args_rules = [
        Rules.APP_ID.value
    ]
    app_key.id = _id

    try:
        ji.Check.previewing(args_rules, app_key.__dict__)
        app_key.delete()
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_unbind():

    args_rules = [
        Rules.APP_ID.value
    ]

    if 'secret' in request.json:
        args_rules.append(
            Rules.APP_SECRET.value
        )

    if 'remark' in request.json:
        args_rules.append(
            Rules.APP_REMARK.value
        )

    if args_rules.__len__() < 2:
        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        return ret

    try:
        ji.Check.previewing(args_rules, request.json)
        app_key = UidOpenidMapping()
        app_key.id = request.json.get('id')
        app_key.get()

        app_key.secret = request.json.get('secret', app_key.secret)
        app_key.remark = request.json.get('remark', app_key.remark)

        app_key.update()
    except ji.PreviewingError, e:
        return json.loads(e.message)

