#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
from flask import Blueprint, request
import jimit as ji

from models import Utils, Rules, App, UidOpenidMapping, User


__author__ = 'James Iter'
__date__ = '2016/11/5'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


blueprint = Blueprint(
    'openid_mgmt',
    __name__,
    url_prefix='/api/openid_mgmt'
)

blueprints = Blueprint(
    'openids_mgmt',
    __name__,
    url_prefix='/api/openids_mgmt'
)


@Utils.dumps2response
@Utils.superuser
def r_get(appid, uid):
    app = App()
    user = User()
    openid = UidOpenidMapping()

    args_rules = [
        Rules.APP_ID_EXT.value,
    ]
    app.id = appid

    try:
        ji.Check.previewing(args_rules, app.__dict__)
    except ji.PreviewingError, e:
        return json.loads(e.message)

    args_rules = [
        Rules.UID.value
    ]
    user.id = uid

    try:
        ji.Check.previewing(args_rules, user.__dict__)
    except ji.PreviewingError, e:
        return json.loads(e.message)

    openid.appid = appid
    openid.uid = uid

    try:
        app.get()

        user.id = long(user.id)
        user.get()

        openid.get()

        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        ret['data'] = openid.__dict__
        ret['data']['user'] = user.__dict__
        del ret['data']['user']['password']
        ret['data']['app'] = app.__dict__
        return ret
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_get_by_login_name_without_appid(login_name=None):
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
    except ji.PreviewingError, e:
        return json.loads(e.message)

    user = User()
    app_map_by_id = dict()

    args_rules = [
        Rules.LOGIN_NAME.value
    ]
    user.login_name = login_name

    try:
        ji.Check.previewing(args_rules, user.__dict__)

        user.get_by('login_name')

        offset = int(offset)
        limit = int(limit)
        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        ret['data'] = list()
        ret['paging'] = {'total': 0, 'offset': offset, 'limit': limit, 'page': page, 'page_size': page_size,
                         'next': '', 'prev': '', 'first': '', 'last': ''}
        app_data, app_total = App.get_by_filter(offset=0, limit=1000, order_by='create_time',
                                                order=order, filter_str='')

        for app in app_data:
            del app['secret']
            app_map_by_id[app['id']] = app

        openid_data, ret['paging']['total'] = UidOpenidMapping.get_by_filter(
            offset=offset, limit=limit, order_by=order_by, order=order, filter_str='uid:in:' + user.id.__str__())

        for openid in openid_data:
            openid['user'] = user.__dict__
            del openid['user']['password']
            openid['app'] = app_map_by_id[openid['appid']]
            ret['data'].append(openid)

        host_url = request.host_url.rstrip('/')
        other_str = '&order=' + order + '&order_by=' + order_by
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

        return ret
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_delete(appid, uid):
    openid = UidOpenidMapping()

    args_rules = [
        Rules.APP_ID_EXT.value,
        Rules.UID_EXT.value
    ]

    openid.appid = appid
    openid.uid = uid

    try:
        ji.Check.previewing(args_rules, openid.__dict__)
        openid.uid = long(openid.uid)

        openid.delete()
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_update(appid, uid):

    openid = UidOpenidMapping()

    args_rules = [
        Rules.APP_ID_EXT.value,
        Rules.UID_EXT.value
    ]

    if 'openid' in request.json:
        args_rules.append(
            Rules.OPENID.value
        )

    if args_rules.__len__() < 3:
        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        return ret

    try:
        ji.Check.previewing(args_rules, {'appid': appid, 'uid': uid})
        openid.appid = appid
        openid.uid = uid
        openid.get()

        openid.openid = request.json.get('openid', openid.openid)
        openid.update()
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_get_by_filter():
    page = str(request.args.get('page', 1))
    page_size = str(request.args.get('page_size', 50))
    filter_str = request.args.get('filter', '')

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

    order_by = request.args.get('order_by', 'create_time')
    order = request.args.get('order', 'asc')

    args_rules = [
        Rules.OFFSET.value,
        Rules.LIMIT.value,
        Rules.ORDER_BY.value,
        Rules.ORDER.value
    ]

    try:
        ji.Check.previewing(args_rules, {'offset': offset, 'limit': limit, 'order_by': order_by, 'order': order})
    except ji.PreviewingError, e:
        return json.loads(e.message)

    app_map_by_id = dict()
    user_map_by_id = dict()

    try:
        offset = int(offset)
        limit = int(limit)
        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        ret['data'] = list()
        ret['paging'] = {'total': 0, 'offset': offset, 'limit': limit, 'page': page, 'page_size': page_size,
                         'next': '', 'prev': '', 'first': '', 'last': ''}
        app_data, app_total = App.get_by_filter(offset=0, limit=1000, order_by='create_time',
                                                order='asc', filter_str='')

        for app in app_data:
            del app['secret']
            app_map_by_id[app['id']] = app

        users, users_total = User.get_by_filter(offset=0, limit=limit, order_by='id',
                                                order='asc', filter_str=filter_str)

        for _user in users:
            user_map_by_id[_user['id']] = _user

        openid_data, ret['paging']['total'] = UidOpenidMapping.get_by_filter(
            offset=offset, limit=limit, order_by=order_by, order=order,
            filter_str='uid:in:' + ','.join(str(uid) for uid in user_map_by_id.keys()))

        for openid in openid_data:
            openid['user'] = user_map_by_id[openid['uid']]
            del openid['user']['password']
            openid['app'] = app_map_by_id[openid['appid']]
            ret['data'].append(openid)

        host_url = request.host_url.rstrip('/')
        other_str = '&order=' + order + '&order_by=' + order_by
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

        return ret
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

    order_by = request.args.get('order_by', 'create_time')
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
    except ji.PreviewingError, e:
        return json.loads(e.message)

    app_map_by_id = dict()
    user_map_by_id = dict()

    try:
        offset = int(offset)
        limit = int(limit)
        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        ret['data'] = list()
        ret['paging'] = {'total': 0, 'offset': offset, 'limit': limit, 'page': page, 'page_size': page_size,
                         'next': '', 'prev': '', 'first': '', 'last': ''}
        app_data, app_total = App.get_by_filter(offset=0, limit=1000, order_by='create_time',
                                                order='asc', filter_str='')

        for app in app_data:
            del app['secret']
            app_map_by_id[app['id']] = app

        users, users_total = User.content_search(offset=0, limit=limit, order_by='id',
                                                 order='asc', keyword=keyword)

        for _user in users:
            user_map_by_id[_user['id']] = _user

        openid_data, ret['paging']['total'] = UidOpenidMapping.get_by_filter(
            offset=offset, limit=limit, order_by=order_by, order=order,
            filter_str='uid:in:' + ','.join(str(uid) for uid in user_map_by_id.keys()))

        for openid in openid_data:
            openid['user'] = user_map_by_id[openid['uid']]
            del openid['user']['password']
            openid['app'] = app_map_by_id[openid['appid']]
            ret['data'].append(openid)

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

        return ret
    except ji.PreviewingError, e:
        return json.loads(e.message)

