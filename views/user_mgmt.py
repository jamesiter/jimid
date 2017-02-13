#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
from flask import Blueprint, request
import jimit as ji

from models import UidOpenidMapping
from models import Utils, Rules, User


__author__ = 'James Iter'
__date__ = '16/6/8'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


blueprint = Blueprint(
    'user_mgmt',
    __name__,
    url_prefix='/api/user_mgmt'
)

blueprints = Blueprint(
    'users_mgmt',
    __name__,
    url_prefix='/api/users_mgmt'
)


@Utils.dumps2response
@Utils.superuser
def r_get(_id):
    user = User()

    args_rules = [
        Rules.UID.value
    ]
    user.id = _id

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
@Utils.superuser
def r_get_by_login_name(login_name=None):
    user = User()

    args_rules = [
        Rules.LOGIN_NAME.value
    ]
    user.login_name = login_name

    try:
        ji.Check.previewing(args_rules, user.__dict__)
        user.get_by('login_name')
        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        ret['data'] = user.__dict__
        del ret['data']['password']
        return ret
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_enable(_id):

    user = User()

    args_rules = [
        Rules.UID.value
    ]
    user.id = _id

    try:
        ji.Check.previewing(args_rules, user.__dict__)
        user.id = long(user.id)
        if user.id == 1:
            ret = dict()
            ret['state'] = ji.Common.exchange_state(40301)
            raise ji.PreviewingError(json.dumps(ret, ensure_ascii=False))
        user.get()
    except ji.PreviewingError, e:
        return json.loads(e.message)

    args_rules = [
        Rules.ENABLED.value
    ]
    user.enabled = True

    try:
        ji.Check.previewing(args_rules, user.__dict__)
        user.update()
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_disable(_id):

    user = User()

    args_rules = [
        Rules.UID.value
    ]
    user.id = _id

    try:
        ji.Check.previewing(args_rules, user.__dict__)
        user.id = long(user.id)
        if user.id == 1:
            ret = dict()
            ret['state'] = ji.Common.exchange_state(40301)
            raise ji.PreviewingError(json.dumps(ret, ensure_ascii=False))
        user.get()
    except ji.PreviewingError, e:
        return json.loads(e.message)

    args_rules = [
        Rules.ENABLED.value
    ]
    user.enabled = False

    try:
        ji.Check.previewing(args_rules, user.__dict__)
        user.update()
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_delete(_id):
    user = User()

    args_rules = [
        Rules.UID.value
    ]
    user.id = _id

    try:
        ji.Check.previewing(args_rules, user.__dict__)
        user.id = long(user.id)
        if user.id == 1:
            ret = dict()
            ret['state'] = ji.Common.exchange_state(40301)
            raise ji.PreviewingError(json.dumps(ret, ensure_ascii=False))

        user.delete()
        # 删除依赖于该用户的openid
        UidOpenidMapping.delete_by_filter('uid:in:' + _id)
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_update(_id):

    user = User()

    args_rules = [
        Rules.UID.value
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

    if 'role_id' in request.json:
        args_rules.append(
            Rules.ROLE_ID_EXT.value
        )

    if args_rules.__len__() < 2:
        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        return ret

    request.json['id'] = _id
    try:
        ji.Check.previewing(args_rules, request.json)
        user.id = int(request.json.get('id'))
        user.get()

        user.login_name = request.json.get('login_name', user.login_name)
        user.mobile_phone = request.json.get('mobile_phone', user.mobile_phone)
        user.mobile_phone_verified = request.json.get('mobile_phone_verified', user.mobile_phone_verified)
        user.email = request.json.get('email', user.email)
        user.email_verified = request.json.get('email_verified', user.email_verified)
        user.role_id = request.json.get('role_id', user.role_id)

        user.update()
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_change_password(_id):

    user = User()

    args_rules = [
        Rules.UID.value
    ]

    user.id = _id
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
@Utils.superuser
def r_get_by_filter():
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
    filter_str = request.args.get('filter', '')

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
        ret['paging'] = {'total': 0, 'offset': offset, 'limit': limit, 'page': page, 'page_size': page_size,
                         'next': '', 'prev': '', 'first': '', 'last': ''}

        ret['data'], ret['paging']['total'] = User.get_by_filter(offset=offset, limit=limit, order_by=order_by,
                                                                 order=order, filter_str=filter_str)

        host_url = request.host_url.rstrip('/')
        other_str = '&filter=' + filter_str + '&order=' + order + '&order_by=' + order_by
        last_pagination = (ret['paging']['total'] + page_size - 1) / page_size

        if page <= 1:
            ret['paging']['prev'] = host_url + blueprint.url_prefix + '?page=1&page_size=' + page_size.__str__() + \
                                    other_str
        else:
            ret['paging']['prev'] = host_url + blueprint.url_prefix + '?page=' + str(page-1) + '&page_size=' + \
                                    page_size.__str__() + other_str

        if page >= last_pagination:
            ret['paging']['next'] = host_url + blueprint.url_prefix + '?page=' + last_pagination.__str__() + \
                                    '&page_size=' + page_size.__str__() + other_str
        else:
            ret['paging']['next'] = host_url + blueprint.url_prefix + '?page=' + str(page+1) + '&page_size=' + \
                                    page_size.__str__() + other_str

        ret['paging']['first'] = host_url + blueprint.url_prefix + '?page=1&page_size=' + \
            page_size.__str__() + other_str
        ret['paging']['last'] = \
            host_url + blueprint.url_prefix + '?page=' + last_pagination.__str__() + '&page_size=' + \
            page_size.__str__() + other_str

        for i in range(ret['data'].__len__()):
            del ret['data'][i]['password']

        return ret
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_update_by_uid_s():
    args_rules = [
        Rules.UIDS.value
    ]

    if 'mobile_phone_verified' in request.json:
        args_rules.append(
            Rules.MOBILE_PHONE_VERIFIED.value
        )

    if 'enabled' in request.json:
        args_rules.append(
            Rules.ENABLED.value
        )

    if 'email_verified' in request.json:
        args_rules.append(
            Rules.EMAIL_VERIFIED.value
        )

    if 'role_id' in request.json:
        args_rules.append(
            Rules.ROLE_ID_EXT.value
        )

    if args_rules.__len__() < 2:
        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        return ret

    try:
        ji.Check.previewing(args_rules, request.json)
        filter_str = 'id:IN:' + request.json.get('ids')
        User.update_by_filter(kv=request.json, filter_str=filter_str)
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_delete_by_uid_s():
    args_rules = [
        Rules.UIDS.value
    ]

    try:
        ji.Check.previewing(args_rules, request.json)
        uid_s = request.json.get('ids')
        if '1' in uid_s.split(','):
            ret = dict()
            ret['state'] = ji.Common.exchange_state(40301)
            raise ji.PreviewingError(json.dumps(ret, ensure_ascii=False))

        filter_str = 'id:IN:' + request.json.get('ids')
        User.delete_by_filter(filter_str=filter_str)
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_content_search():
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
    keyword = request.args.get('keyword', '')

    args_rules = [
        Rules.OFFSET.value,
        Rules.LIMIT.value,
        Rules.ORDER_BY.value,
        Rules.ORDER.value,
        Rules.KEYWORD.value
    ]

    try:
        ji.Check.previewing(args_rules, {'offset': offset, 'limit': limit, 'order_by': order_by, 'order': order,
                                         'keyword': keyword})
        offset = int(offset)
        limit = int(limit)
        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        ret['data'] = list()
        ret['paging'] = {'total': 0, 'offset': offset, 'limit': limit, 'page': page, 'page_size': page_size}

        ret['data'], ret['paging']['total'] = User.content_search(offset=offset, limit=limit, order_by=order_by,
                                                                  order=order, keyword=keyword)

        host_url = request.host_url.rstrip('/')
        other_str = '&keyword=' + keyword + '&order=' + order + '&order_by=' + order_by
        last_pagination = (ret['paging']['total'] + page_size - 1) / page_size

        if page <= 1:
            ret['paging']['prev'] = host_url + blueprints.url_prefix + '/_search?page=1&page_size=' + \
                                    page_size.__str__() + other_str
        else:
            ret['paging']['prev'] = host_url + blueprints.url_prefix + '/_search?page=' + str(page-1) + \
                                    '&page_size=' + page_size.__str__() + other_str

        if page >= last_pagination:
            ret['paging']['next'] = host_url + blueprints.url_prefix + '/_search?page=' + last_pagination.__str__() + \
                                    '&page_size=' + page_size.__str__() + other_str
        else:
            ret['paging']['next'] = host_url + blueprints.url_prefix + '/_search?page=' + str(page+1) + \
                                    '&page_size=' + page_size.__str__() + other_str

        ret['paging']['first'] = host_url + blueprints.url_prefix + '/_search?page=1&page_size=' + \
            page_size.__str__() + other_str
        ret['paging']['last'] = \
            host_url + blueprints.url_prefix + '/_search?page=' + last_pagination.__str__() + '&page_size=' + \
            page_size.__str__() + other_str

        for i in range(ret['data'].__len__()):
            del ret['data'][i]['password']

        return ret
    except ji.PreviewingError, e:
        return json.loads(e.message)
