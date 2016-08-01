#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
from flask import Blueprint, request
import jimit as ji

from models import Utils, Rules, Auth


__author__ = 'James Iter'
__date__ = '16/6/8'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


blueprint = Blueprint(
    'mgmt',
    __name__,
    url_prefix='/mgmt'
)


@Utils.dumps2response
@Utils.superuser
def r_get_by_login_name(login_name=None):
    auth = Auth()

    args_rules = [
        Rules.LOGIN_NAME.value
    ]
    auth.login_name = login_name

    try:
        ji.Check.previewing(args_rules, auth.__dict__)
        auth.get_by_login_name()
        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        ret['data'] = auth.__dict__
        del ret['data']['password']
        return ret
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_enable(_id):

    auth = Auth()

    args_rules = [
        Rules.ID.value
    ]
    auth.id = _id

    try:
        ji.Check.previewing(args_rules, auth.__dict__)
        auth.id = long(auth.id)
        if auth.id == 1:
            ret = dict()
            ret['state'] = ji.Common.exchange_state(40301)
            raise ji.PreviewingError(json.dumps(ret, ensure_ascii=False))
        auth.get()
    except ji.PreviewingError, e:
        return json.loads(e.message)

    args_rules = [
        Rules.ENABLED.value
    ]
    auth.enabled = True

    try:
        ji.Check.previewing(args_rules, auth.__dict__)
        auth.update()
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_disable(_id):

    auth = Auth()

    args_rules = [
        Rules.ID.value
    ]
    auth.id = _id

    try:
        ji.Check.previewing(args_rules, auth.__dict__)
        auth.id = long(auth.id)
        if auth.id == 1:
            ret = dict()
            ret['state'] = ji.Common.exchange_state(40301)
            raise ji.PreviewingError(json.dumps(ret, ensure_ascii=False))
        auth.get()
    except ji.PreviewingError, e:
        return json.loads(e.message)

    args_rules = [
        Rules.ENABLED.value
    ]
    auth.enabled = False

    try:
        ji.Check.previewing(args_rules, auth.__dict__)
        auth.update()
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
@Utils.superuser
def r_delete(_id):
    auth = Auth()

    args_rules = [
        Rules.ID.value
    ]
    auth.id = _id

    try:
        ji.Check.previewing(args_rules, auth.__dict__)
        auth.id = long(auth.id)
        if auth.id == 1:
            ret = dict()
            ret['state'] = ji.Common.exchange_state(40301)
            raise ji.PreviewingError(json.dumps(ret, ensure_ascii=False))

        auth.delete()
    except ji.PreviewingError, e:
        return json.loads(e.message)



