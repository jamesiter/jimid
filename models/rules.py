#!/usr/bin/env python
# -*- coding: utf-8 -*-


from enum import Enum


__author__ = 'James Iter'
__date__ = '15/12/16'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'


class Rules(Enum):
    UID = ('regex:^\d{1,17}$', 'id')
    UIDS = ('regex:^(\d{1,17}(,)?)+$', 'ids')
    LOGIN_NAME = (basestring, 'login_name', (5, 30))
    PASSWORD = (basestring, 'password', (1, 100))
    CREATE_TIME = ((int, long), 'create_time', (0, 9223372036854775807))
    MOBILE_PHONE = (basestring, 'mobile_phone', (0, 13))
    EMAIL = (basestring, 'email', (0, 30))
    # 邮件不区分大小写，地址部分起始必须为字母或数字，句点(.)和下划线(_)不可以组合及连续出现，邮件域部分遵循域名命名规则
    EMAIL_PATTERN = ('regex:^[a-z0-9]{1,20}([._][a-z0-9]{1,20}){0,5}@'
                     '[a-z0-9]{1,20}([-][a-z0-9]{1,20}){0,2}\.[a-z]{1,5}$', 'email')

    MOBILE_PHONE_VERIFIED = (bool, 'mobile_phone_verified', [False, True])
    EMAIL_VERIFIED = (bool, 'email_verified', [False, True])
    MANAGER = (bool, 'manager', [False, True])
    ENABLED = (bool, 'enabled', [False, True])

    OFFSET = ('regex:^\d{1,17}$', 'offset')
    LIMIT = ('regex:^\d{1,17}$', 'limit')
    PAGE = ('regex:^\d{1,17}$', 'page')
    PAGE_SIZE = ('regex:^\d{1,17}$', 'page_size')
    ORDER_BY = (basestring, 'order_by', (1, 30))
    ORDER = (basestring, 'order', ['asc', 'desc'])
    KEYWORD = (basestring, 'keyword')
    # TODO: 加入filter正则表达式
    APP_ID = (basestring, 'id', (16, 16))
    # EXT for external(客观的)
    APP_ID_EXT = (basestring, 'appid', (16, 16))
    APP_SECRET = (basestring, 'secret', (32, 32))
    APP_NAME = (basestring, 'name', (0, 255))
    APP_REMARK = (basestring, 'remark', (0, 1024))
    OPENID = (basestring, 'openid', (0, 30))
    # 9999999999 @ Sat, 20 Nov 2286 17:46:39 GMT, 10个9能记录到2286年
    TS = ('regex:^\d{1,10}$', 'ts')
    SIGN = (basestring, 'sign')
    REDIRECT_URL = (basestring, 'redirect_url')
