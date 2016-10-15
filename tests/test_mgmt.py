#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import json
import unittest


__author__ = 'James Iter'
__date__ = '16/06/08'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


class TestMgmt(unittest.TestCase):

    login_name = 'james'
    password = 'password'
    count = 20
    uid_s = list()

    superuser_cookies = None
    superuser_name = 'admin'
    superuser_password = 'admin'

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # ------------------------------------------------普通用户---------------------------------------------------------
    # 注册普通用户
    def test_11_sign_up(self):
        for i in range(1, TestMgmt.count):
            payload = {
                "login_name": TestMgmt.login_name + i.__str__(),
                "password": TestMgmt.password
            }

            url = 'http://jimauth.dev.iit.im/user/_sign_up'
            headers = {'content-type': 'application/json'}
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            j_r = json.loads(r.content)
            print json.dumps(j_r, ensure_ascii=False)
            TestMgmt.uid_s.append(j_r['data']['id'])
            self.assertEqual('200', j_r['state']['code'])

    # ------------------------------------------------超级用户---------------------------------------------------------
    # 超级用户登录
    def test_31_sign_in_superuser(self):
        payload = {
            "login_name": TestMgmt.superuser_name,
            "password": TestMgmt.superuser_password
        }

        url = 'http://jimauth.dev.iit.im/user/_sign_in'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        TestMgmt.superuser_cookies = r.cookies
        self.assertEqual('200', j_r['state']['code'])

    # 超级用户获取用户列表
    def test_32_get_list(self):
        url = 'http://jimauth.dev.iit.im/mgmts?offset=10&limit=5'
        r = requests.get(url, cookies=TestMgmt.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 超级用户获取用户列表
    def test_33_get_list_via_page(self):
        url = 'http://jimauth.dev.iit.im/mgmts?page=2&page_size=5'
        r = requests.get(url, cookies=TestMgmt.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 超级用户获取用户列表
    def test_34_update(self):
        payload = {
            "id": TestMgmt.uid_s[10],
            "login_name": "new_login_name",
            "mobile_phone": "15601603670",
            "mobile_phone_verified": True,
            "email": "jimit@qq.com",
            "email_verified": True
        }

        url = 'http://jimauth.dev.iit.im/mgmt/_update'
        headers = {'content-type': 'application/json'}
        r = requests.put(url, cookies=TestMgmt.superuser_cookies, headers=headers, data=json.dumps(payload))
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 超级用户获取用户列表
    def test_35_update(self):
        payload = {
            "id": TestMgmt.uid_s[11],
            "login_name": "new_login_name2",
        }

        url = 'http://jimauth.dev.iit.im/mgmt/_update'
        headers = {'content-type': 'application/json'}
        r = requests.put(url, cookies=TestMgmt.superuser_cookies, headers=headers, data=json.dumps(payload))
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 超级用户获取用户列表
    def test_36_get_list_via_page(self):
        url = 'http://jimauth.dev.iit.im/mgmts?page=3&page_size=5'
        r = requests.get(url, cookies=TestMgmt.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 超级用户删除普通用户
    def test_38_delete_via_superuser(self):
        for uid in TestMgmt.uid_s:
            url = 'http://jimauth.dev.iit.im/mgmt/' + uid.__str__()
            r = requests.delete(url, cookies=TestMgmt.superuser_cookies)
            j_r = json.loads(r.content)
            print json.dumps(j_r, ensure_ascii=False)
            self.assertEqual('200', j_r['state']['code'])


if __name__ == '__main__':
    unittest.main()
