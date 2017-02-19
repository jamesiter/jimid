#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import json
import unittest
import urllib

import jimit as ji


__author__ = 'James Iter'
__date__ = '2017/2/17'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2017 by James Iter.'


class TestOpenidMgmt(unittest.TestCase):

    base_url = 'http://jimauth.dev.iit.im/api'
    now_ts = ji.Common.ts()

    cookies = None
    login_name = ji.Common.generate_random_code(length=6)
    password = 'password'

    superuser_cookies = None
    superuser_name = 'admin'
    superuser_password = 'admin'

    uid = None
    app_id = None
    app_secret = None

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # ------------------------------------------------超级用户---------------------------------------------------------
    # 超级用户登录
    def test_11_sign_in_superuser(self):
        payload = {
            "login_name": TestOpenidMgmt.superuser_name,
            "password": TestOpenidMgmt.superuser_password
        }

        url = TestOpenidMgmt.base_url + '/user/_sign_in'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        TestOpenidMgmt.superuser_cookies = r.cookies
        self.assertEqual('200', j_r['state']['code'])

    # 创建应用
    def test_12_create_app(self):
        payload = {
            "name": ji.Common.generate_random_code(length=6)
        }
        url = TestOpenidMgmt.base_url + '/app'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, cookies=TestOpenidMgmt.superuser_cookies, headers=headers, data=json.dumps(payload))
        j_r = json.loads(r.content)
        TestOpenidMgmt.app_id = j_r['data']['id']
        TestOpenidMgmt.app_secret = j_r['data']['secret']
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 注册普通用户
    def test_13_sign_up(self):
        payload = {
            "login_name": TestOpenidMgmt.login_name,
            "password": TestOpenidMgmt.password
        }

        url = TestOpenidMgmt.base_url + '/user/_sign_up'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])
        TestOpenidMgmt.uid = j_r['data']['id']

    # 普通用户登录,获得普通用户cookie
    def test_14_sign_in(self):
        payload = {
            "login_name": TestOpenidMgmt.login_name,
            "password": TestOpenidMgmt.password
        }

        url = TestOpenidMgmt.base_url + '/user/_sign_in'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        TestOpenidMgmt.cookies = r.cookies
        self.assertEqual('200', j_r['state']['code'])

    # 生成绑定所用签名
    def test_20_generate_sign_with_bind(self):
        args = {
            'ts': urllib.quote_plus(TestOpenidMgmt.now_ts.__str__()),
            'appid': urllib.quote_plus(TestOpenidMgmt.app_id),
            'redirect_url': urllib.quote_plus('http://service.iit.im'),
            'openid': '1'
        }
        TestOpenidMgmt.sign_with_bind = ji.Security.ji_hash_sign(algorithm='sha1', secret=TestOpenidMgmt.app_secret,
                                                                 content=args)

    # 绑定
    def test_21_openid_bind(self):
        args = {
            'ts': urllib.quote_plus(TestOpenidMgmt.now_ts.__str__()),
            'appid': urllib.quote_plus(TestOpenidMgmt.app_id),
            'redirect_url': urllib.quote_plus('http://service.iit.im'),
            'openid': '1',
            'method': 'GET',
            'base_url': TestOpenidMgmt.base_url + '/openid/_bind'
        }
        sign = ji.Security.ji_hash_sign(algorithm='sha1', secret=TestOpenidMgmt.app_secret,
                                        content=args)

        url = '&'.join(['appid=' + TestOpenidMgmt.app_id, 'ts=' + TestOpenidMgmt.now_ts.__str__(), 'openid=1',
                        'redirect_url=http://service.iit.im', 'sign=' + sign])
        url = TestOpenidMgmt.base_url + '/openid/_bind?' + url
        r = requests.get(url, cookies=TestOpenidMgmt.cookies, allow_redirects=False)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        print r.headers._store['location']
        self.assertEqual(302, r.status_code)
        self.assertEqual('200', j_r['state']['code'])

    def test_22_get(self):
        url = TestOpenidMgmt.base_url + '/openids_mgmt'
        r = requests.get(url, cookies=TestOpenidMgmt.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 更新openid
    def test_23_openid_update(self):
        payload = {
            'openid': '2'
        }

        url = TestOpenidMgmt.base_url + '/openid_mgmt/' + TestOpenidMgmt.app_id + '/' + TestOpenidMgmt.uid.__str__()
        headers = {'content-type': 'application/json'}
        r = requests.patch(url, cookies=TestOpenidMgmt.superuser_cookies, headers=headers, data=json.dumps(payload))
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 全文检索
    def test_24_get_list_via_content_search(self):
        url = TestOpenidMgmt.base_url + '/openids_mgmt/_search?page=1&page_size=5&keyword=' + TestOpenidMgmt.login_name
        r = requests.get(url, cookies=TestOpenidMgmt.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 删除openid
    def test_31_delete_openid(self):
        url = TestOpenidMgmt.base_url + '/openid_mgmt/' + TestOpenidMgmt.app_id + '/' + TestOpenidMgmt.uid.__str__()
        r = requests.delete(url, cookies=TestOpenidMgmt.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 删除应用
    def test_32_delete_app(self):
        url = TestOpenidMgmt.base_url + '/app/' + TestOpenidMgmt.app_id
        r = requests.delete(url, cookies=TestOpenidMgmt.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 删除用户
    def test_33_delete_user(self):
        url = TestOpenidMgmt.base_url + '/user_mgmt/' + TestOpenidMgmt.uid.__str__()
        r = requests.delete(url, cookies=TestOpenidMgmt.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])
