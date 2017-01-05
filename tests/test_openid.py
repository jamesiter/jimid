#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import json
import unittest
import urllib

import jimit as ji


__author__ = 'James Iter'
__date__ = '16/06/08'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


class TestOpenid(unittest.TestCase):

    base_url = 'http://jimauth.dev.iit.im/api'

    app_id = None
    app_secret = None
    sign_with_sign_up = None
    sign_with_bind = None
    openid = ''
    now_ts = ji.Common.ts()

    cookies = None
    login_name = 'james'
    password = 'password'
    uid = None

    superuser_cookies = None
    superuser_name = 'admin'
    superuser_password = 'admin'

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # ------------------------------------------------超级用户---------------------------------------------------------
    # 超级用户登录
    def test_11_sign_in_superuser(self):
        payload = {
            "login_name": TestOpenid.superuser_name,
            "password": TestOpenid.superuser_password
        }

        url = TestOpenid.base_url + '/user/_sign_in'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        TestOpenid.superuser_cookies = r.cookies
        self.assertEqual('200', j_r['state']['code'])

    # 创建appkey
    def test_12_create_app_key(self):
        payload = {
            "remark": "remark",
        }
        url = TestOpenid.base_url + '/app_key'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, cookies=TestOpenid.superuser_cookies, headers=headers, data=json.dumps(payload))
        j_r = json.loads(r.content)
        TestOpenid.app_id = j_r['data']['id']
        TestOpenid.app_secret = j_r['data']['secret']
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 注册普通用户
    def test_13_sign_up(self):
        payload = {
            "login_name": TestOpenid.login_name,
            "password": TestOpenid.password
        }

        url = TestOpenid.base_url + '/user/_sign_up'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 普通用户登录,获得普通用户cookie
    def test_14_sign_in(self):
        payload = {
            "login_name": TestOpenid.login_name,
            "password": TestOpenid.password
        }

        url = TestOpenid.base_url + '/user/_sign_in'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        TestOpenid.cookies = r.cookies
        self.assertEqual('200', j_r['state']['code'])

    def test_15_get(self):
        url = TestOpenid.base_url + '/user'
        r = requests.get(url, cookies=TestOpenid.cookies)
        j_r = json.loads(r.content)
        TestOpenid.uid = j_r['data']['id']
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    def test_17_generate_sign_with_bind(self):
        args = {
            'ts': urllib.quote_plus(TestOpenid.now_ts.__str__()),
            'appid': urllib.quote_plus(TestOpenid.app_id),
            'redirect_url': urllib.quote_plus('http://www.baidu.com'),
            'openid': '1'
        }
        TestOpenid.sign_with_bind = ji.Security.ji_hash_sign(algorithm='sha1', secret=TestOpenid.app_secret,
                                                             content=args)

    def test_21_openid_sign_up_no_user_cookie(self):
        args = {
            'ts': urllib.quote_plus(TestOpenid.now_ts.__str__()),
            'appid': urllib.quote_plus(TestOpenid.app_id),
            'redirect_url': urllib.quote_plus('http://www.baidu.com'),
            'method': 'GET',
            'base_url': TestOpenid.base_url + '/openid/_sign_up'
        }
        sign = ji.Security.ji_hash_sign(algorithm='sha1', secret=TestOpenid.app_secret,
                                        content=args)
        url = '&'.join(['appid=' + TestOpenid.app_id, 'ts=' + TestOpenid.now_ts.__str__(),
                        'redirect_url=http://www.baidu.com', 'sign=' + sign])
        url = TestOpenid.base_url + '/openid/_sign_up?' + url
        r = requests.get(url)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual(278, r.status_code)
        self.assertEqual('41208', j_r['state']['sub']['code'])

    def test_22_openid_sign_up(self):
        args = {
            'ts': urllib.quote_plus(TestOpenid.now_ts.__str__()),
            'appid': urllib.quote_plus(TestOpenid.app_id),
            'redirect_url': urllib.quote_plus('http://www.baidu.com'),
            'method': 'GET',
            'base_url': TestOpenid.base_url + '/openid/_sign_up'
        }
        sign = ji.Security.ji_hash_sign(algorithm='sha1', secret=TestOpenid.app_secret,
                                        content=args)
        url = '&'.join(['appid=' + TestOpenid.app_id, 'ts=' + TestOpenid.now_ts.__str__(),
                        'redirect_url=http://www.baidu.com', 'sign=' + sign])
        url = TestOpenid.base_url + '/openid/_sign_up?' + url
        r = requests.get(url, cookies=TestOpenid.cookies, allow_redirects=False)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        print r.headers._store['location']

        for item in r.headers._store['location'][1].split('?')[1].split('&'):
            kv = item.split('=')
            if kv[0] == 'openid':
                TestOpenid.openid = kv[1]

        self.assertEqual(302, r.status_code)

    def test_23_openid_bind(self):
        args = {
            'ts': urllib.quote_plus(TestOpenid.now_ts.__str__()),
            'appid': urllib.quote_plus(TestOpenid.app_id),
            'redirect_url': urllib.quote_plus('http://www.baidu.com'),
            'openid': '1',
            'method': 'GET',
            'base_url': TestOpenid.base_url + '/openid/_bind'
        }
        sign = ji.Security.ji_hash_sign(algorithm='sha1', secret=TestOpenid.app_secret,
                                        content=args)

        url = '&'.join(['appid=' + TestOpenid.app_id, 'ts=' + TestOpenid.now_ts.__str__(), 'openid=1',
                        'redirect_url=http://www.baidu.com', 'sign=' + sign])
        url = TestOpenid.base_url + '/openid/_bind?' + url
        r = requests.get(url, cookies=TestOpenid.cookies, allow_redirects=False)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        print r.headers._store['location']
        self.assertEqual(302, r.status_code)
        self.assertEqual('40901', j_r['state']['sub']['code'])

    def test_24_openid_unbind(self):
        args = {
            'ts': urllib.quote_plus(TestOpenid.now_ts.__str__()),
            'appid': urllib.quote_plus(TestOpenid.app_id),
            'redirect_url': urllib.quote_plus('http://www.baidu.com'),
            'method': 'GET',
            'base_url': TestOpenid.base_url + '/openid/_unbind'
        }
        sign = ji.Security.ji_hash_sign(algorithm='sha1', secret=TestOpenid.app_secret,
                                        content=args)

        url = '&'.join(['appid=' + TestOpenid.app_id, 'ts=' + TestOpenid.now_ts.__str__(),
                        'redirect_url=http://www.baidu.com', 'sign=' + sign])
        url = TestOpenid.base_url + '/openid/_unbind?' + url
        r = requests.get(url, cookies=TestOpenid.cookies, allow_redirects=False)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        print r.headers._store['location']
        self.assertEqual(302, r.status_code)

    def test_25_openid_rebind(self):
        args = {
            'ts': urllib.quote_plus(TestOpenid.now_ts.__str__()),
            'appid': urllib.quote_plus(TestOpenid.app_id),
            'redirect_url': urllib.quote_plus('http://www.baidu.com'),
            'openid': '1',
            'method': 'GET',
            'base_url': TestOpenid.base_url + '/openid/_bind'
        }
        sign = ji.Security.ji_hash_sign(algorithm='sha1', secret=TestOpenid.app_secret,
                                        content=args)

        url = '&'.join(['appid=' + TestOpenid.app_id, 'ts=' + TestOpenid.now_ts.__str__(), 'openid=1',
                        'redirect_url=http://www.baidu.com', 'sign=' + sign])
        url = TestOpenid.base_url + '/openid/_bind?' + url
        r = requests.get(url, cookies=TestOpenid.cookies, allow_redirects=False)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        print r.headers._store['location']
        self.assertEqual(302, r.status_code)

    def test_26_openid_auth(self):
        args = {
            'ts': urllib.quote_plus(TestOpenid.now_ts.__str__()),
            'appid': urllib.quote_plus(TestOpenid.app_id),
            'redirect_url': urllib.quote_plus('http://www.baidu.com'),
            'method': 'GET',
            'base_url': TestOpenid.base_url + '/openid/_auth'
        }
        sign = ji.Security.ji_hash_sign(algorithm='sha1', secret=TestOpenid.app_secret,
                                        content=args)

        url = '&'.join(['appid=' + TestOpenid.app_id, 'ts=' + TestOpenid.now_ts.__str__(),
                        'redirect_url=http://www.baidu.com', 'sign=' + sign])
        url = TestOpenid.base_url + '/openid/_auth?' + url
        r = requests.get(url, cookies=TestOpenid.cookies, allow_redirects=False)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        print r.headers._store['location']
        self.assertEqual(302, r.status_code)

    # 删除appkey
    def test_31_delete(self):
        url = TestOpenid.base_url + '/app_key/' + TestOpenid.app_id
        r = requests.delete(url, cookies=TestOpenid.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 超级用户删除普通用户
    def test_32_delete_via_superuser(self):
        url = TestOpenid.base_url + '/mgmt/' + TestOpenid.uid.__str__()
        r = requests.delete(url, cookies=TestOpenid.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])


if __name__ == '__main__':
    unittest.main()
