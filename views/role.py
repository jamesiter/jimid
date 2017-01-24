#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from flask import Blueprint, request, g, make_response
import jimit as ji

from models import AppKey
from models import RoleAppMapping
from models import User
from models import Utils, Rules, Role


__author__ = 'James Iter'
__date__ = '2017/1/21'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


blueprint = Blueprint(
    'role',
    __name__,
    url_prefix='/api/role'
)

blueprints = Blueprint(
    'roles',
    __name__,
    url_prefix='/api/roles'
)


@Utils.dumps2response
@Utils.superuser
def r_create():

    role = Role()

    args_rules = [
        Rules.ROLE_NAME.value,
        Rules.ROLE_REMARK.value
    ]

    role.name = request.json.get('name', '')
    role.remark = request.json.get('remark', '')

    try:
        ji.Check.previewing(args_rules, role.__dict__)
        role.create()
        role.get_by('name')
        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        ret['data'] = role.__dict__
        return ret
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_get(_id):
    role = Role()

    args_rules = [
        Rules.ROLE_ID.value
    ]

    role.id = _id

    try:
        ji.Check.previewing(args_rules, role.__dict__)
    except ji.PreviewingError, e:
        return json.loads(e.message)

    try:
        role.get()

        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        ret['data'] = role.__dict__
        return ret
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_delete(_id):
    role = Role()

    args_rules = [
        Rules.ROLE_ID.value
    ]

    role.id = _id

    try:
        ji.Check.previewing(args_rules, role.__dict__)

        role.delete()
        # 删除依赖于该AppKey的openid
        RoleAppMapping.delete_by_filter(filter_str='role_id:in:' + _id)
        User.update_by_filter(kv={'role_id': 0}, filter_str='role_id:in:' + _id)
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_update(_id):
    role = Role()

    args_rules = [
        Rules.ROLE_ID.value
    ]

    if 'name' in request.json:
        args_rules.append(
            Rules.ROLE_NAME.value
        )

    if 'remark' in request.json:
        args_rules.append(
            Rules.ROLE_REMARK.value
        )

    if args_rules.__len__() < 2:
        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        return ret

    request.json['id'] = _id

    try:
        ji.Check.previewing(args_rules, request.json)
        role.id = _id
        role.get()

        role.name = request.json.get('name', role.name)
        role.remark = request.json.get('remark', role.remark)
        role.update()
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

    try:
        offset = int(offset)
        limit = int(limit)
        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        ret['data'] = list()
        ret['paging'] = {'total': 0, 'offset': offset, 'limit': limit, 'page': page, 'page_size': page_size,
                         'next': '', 'prev': '', 'first': '', 'last': ''}

        ret['paging'] = {'total': 0, 'offset': offset, 'limit': limit, 'page': page, 'page_size': page_size,
                         'next': '', 'prev': '', 'first': '', 'last': ''}

        ret['data'], ret['paging']['total'] = Role.get_by_filter(offset=offset, limit=limit, order_by=order_by,
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

        ret['data'], ret['paging']['total'] = Role.content_search(offset=offset, limit=limit, order_by=order_by,
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

        return ret
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_get_user_role_app_mapping():
    order_by = request.args.get('order_by', 'id')
    order = request.args.get('order', 'asc')

    args_rules = [
        Rules.ORDER_BY.value,
        Rules.ORDER.value
    ]

    try:
        ji.Check.previewing(args_rules, {'order_by': order_by, 'order': order})
    except ji.PreviewingError, e:
        return json.loads(e.message)

    app_map_by_id = dict()
    user_map_by_role_id = dict()
    app_map_by_role_id = dict()
    role_ids = list()

    try:
        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        ret['data'] = list()
        ret['paging'] = {'total': 0, 'offset': 0, 'limit': 0, 'page': 1, 'page_size': 9999,
                         'next': '', 'prev': '', 'first': '', 'last': ''}

        app_key_data, app_key_total = AppKey.get_all(order_by='create_time', order='asc')

        for app_key in app_key_data:
            del app_key['secret']
            app_map_by_id[app_key['id']] = app_key

        roles, ret['paging']['total'] = Role.get_all(order_by=order_by, order=order)

        for role in roles:
            role_ids.append(role['id'])

        if role_ids.__len__() > 0:
            users, users_total = User.get_by_filter(offset=0, limit=1000, order_by='id', order='asc',
                                                    filter_str='role_id:in:' + ','.join(str(rid) for rid in role_ids))

            for _user in users:
                if _user['role_id'] not in user_map_by_role_id:
                    user_map_by_role_id[_user['role_id']] = list()

                del _user['password']
                user_map_by_role_id[_user['role_id']].append(_user)

        role_app_mapping = RoleAppMapping()
        role_app_data, role_app_total = role_app_mapping.get_all(order_by='role_id', order='asc')

        for role_app in role_app_data:
            if role_app['role_id'] not in app_map_by_role_id:
                app_map_by_role_id[role_app['role_id']] = list()

            app_map_by_role_id[role_app['role_id']].append(app_map_by_id[role_app['appid']])

        for role in roles:
            role['users'] = user_map_by_role_id.get(role['id'], list())
            role['apps'] = app_map_by_role_id.get(role['id'], list())
            ret['data'].append(role)

        return ret
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_add_user_to_role(role_id, uid):
    args_rules = [
        Rules.ROLE_ID_EXT.value,
        Rules.UID_EXT.value
    ]

    try:
        ji.Check.previewing(args_rules, {'role_id': role_id, 'uid': uid})
        user = User()
        user.id = uid
        user.get()
        user.role_id = role_id
        user.update()
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_delete_user_from_role(role_id, uid):
    args_rules = [
        Rules.ROLE_ID_EXT.value,
        Rules.UID_EXT.value
    ]

    try:
        ji.Check.previewing(args_rules, {'role_id': role_id, 'uid': uid})
        user = User()
        user.id = uid
        user.get()
        user.role_id = 0
        user.update()
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_add_app_to_role(role_id, appid):
    role_app_mapping = RoleAppMapping()

    args_rules = [
        Rules.ROLE_ID.value,
        Rules.APP_ID_EXT.value,
    ]

    role_app_mapping.role_id = role_id
    role_app_mapping.appid = appid

    try:
        ji.Check.previewing(args_rules, role_app_mapping.__dict__)
        role_app_mapping.create()

        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        ret['data'] = role_app_mapping.__dict__
        return ret
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_delete_app_from_role(role_id, appid):
    args_rules = [
        Rules.ROLE_ID_EXT.value,
        Rules.APP_ID_EXT.value
    ]

    try:
        ji.Check.previewing(args_rules, {'role_id': role_id, 'appid': appid})
        role_app_mapping = RoleAppMapping()
        role_app_mapping.role_id = role_id
        role_app_mapping.appid = appid
        role_app_mapping.delete()
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_content_search_with_free_users():
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

        ret['data'], ret['paging']['total'] = User.content_search_for_role_free_users(
            offset=offset, limit=limit, order_by=order_by, order=order, keyword=keyword)

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
