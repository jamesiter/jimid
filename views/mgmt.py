#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
from flask import Blueprint, request
import jimit as ji

from models import Utils, Rules, User


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
    user = User()

    args_rules = [
        Rules.LOGIN_NAME.value
    ]
    user.login_name = login_name

    try:
        ji.Check.previewing(args_rules, user.__dict__)
        user.get_by_login_name()
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
        Rules.ID.value
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
        Rules.ID.value
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
        Rules.ID.value
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
    except ji.PreviewingError, e:
        return json.loads(e.message)



