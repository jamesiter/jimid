#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import json
import unittest


__author__ = 'James Iter'
__date__ = '16/06/08'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


class TestUser(unittest.TestCase):

    base_url = 'http://jimauth.dev.iit.im/api'

    cookies = None
    uid_s = []
    login_name = 'james'
    password = 'password'
    password2 = 'password2'
    mobile_phone = '15600000000'
    email = 'james.iter.cn@gmail.com'

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
        payload = {
            "login_name": TestUser.login_name,
            "password": TestUser.password
        }

        url = TestUser.base_url + '/user/_sign_up'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    def test_12_sign_up_by_mobile_phone(self):
        payload = {
            "mobile_phone": TestUser.mobile_phone,
            "password": TestUser.password
        }

        url = TestUser.base_url + '/user/_sign_up_by_mobile_phone'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    def test_13_sign_up_by_email(self):
        payload = {
            "email": TestUser.email,
            "password": TestUser.password
        }

        url = TestUser.base_url + '/user/_sign_up_by_email'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 普通用户登录
    def test_14_sign_in_by_email(self):
        payload = {
            "email": TestUser.email,
            "password": TestUser.password
        }

        url = TestUser.base_url + '/user/_sign_in_by_email'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        TestUser.cookies = r.cookies
        self.assertEqual('200', j_r['state']['code'])

    def test_15_get(self):
        url = TestUser.base_url + '/user'
        r = requests.get(url, cookies=TestUser.cookies)
        j_r = json.loads(r.content)
        TestUser.uid_s.insert(0, j_r['data']['id'])
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    def test_16_sign_in_by_mobile_phone(self):
        payload = {
            "mobile_phone": TestUser.mobile_phone,
            "password": TestUser.password
        }

        url = TestUser.base_url + '/user/_sign_in_by_mobile_phone'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        TestUser.cookies = r.cookies
        self.assertEqual('200', j_r['state']['code'])

    def test_17_get(self):
        url = TestUser.base_url + '/user'
        r = requests.get(url, cookies=TestUser.cookies)
        j_r = json.loads(r.content)
        TestUser.uid_s.insert(0, j_r['data']['id'])
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    def test_18_sign_in(self):
        payload = {
            "login_name": TestUser.login_name,
            "password": TestUser.password
        }

        url = TestUser.base_url + '/user/_sign_in'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        TestUser.cookies = r.cookies
        self.assertEqual('200', j_r['state']['code'])

    # 普通用户获取自己的用户信息
    def test_19_get(self):
        url = TestUser.base_url + '/user'
        r = requests.get(url, cookies=TestUser.cookies)
        j_r = json.loads(r.content)
        TestUser.uid_s.append(j_r['data']['id'])
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 普通用户通过session id自我验证
    def test_20_user(self):
        url = TestUser.base_url + '/user/_auth'
        r = requests.get(url, cookies=TestUser.cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 普通用户更改登录密码
    def test_21_change_password(self):
        payload = {
            "password": TestUser.password2
        }
        url = TestUser.base_url + '/user/_change_password'
        headers = {'content-type': 'application/json'}
        r = requests.patch(url, cookies=TestUser.cookies, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 普通用户更改密码后重新登录
    def test_22_re_sign_in(self):
        payload = {
            "login_name": TestUser.login_name,
            "password": TestUser.password2
        }

        url = TestUser.base_url + '/user/_sign_in'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        TestUser.cookies = r.cookies
        self.assertEqual('200', j_r['state']['code'])

    # 普通用户重新获取自己的用户信息
    def test_23_get(self):
        url = TestUser.base_url + '/user'
        r = requests.get(url, cookies=TestUser.cookies)
        j_r = json.loads(r.content)
        TestUser.uid_s[-1] = j_r['data']['id']
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 测试普通用户通过登录名获取用户信息,应该返回失败,该接口只给超级用户使用
    def test_24_get_by_login_name(self):
        url = TestUser.base_url + '/user_mgmt/_by_login_name/' + TestUser.login_name
        r = requests.get(url, cookies=TestUser.cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('403', j_r['state']['code'])

    # 测试普通用户通过 session id 禁用自己,应该返回失败,该接口只给超级用户使用
    def test_25_disable(self):
        url = TestUser.base_url + '/user_mgmt/_disable/' + TestUser.uid_s[-1].__str__()
        r = requests.patch(url, cookies=TestUser.cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('403', j_r['state']['code'])

    # 测试普通用户通过 session id 解禁自己,应该返回失败,该接口只给超级用户使用
    def test_26_enable(self):
        url = TestUser.base_url + '/user_mgmt/_enable/' + TestUser.uid_s[-1].__str__()
        r = requests.patch(url, cookies=TestUser.cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('403', j_r['state']['code'])

    # 测试普通用户自我删除,应该返回失败,该系统不允许自我删除,而且删除权限只有超级用户拥有
    def test_27_delete(self):
        url = TestUser.base_url + '/user_mgmt/' + TestUser.uid_s[-1].__str__()
        r = requests.delete(url, cookies=TestUser.cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('403', j_r['state']['code'])


if __name__ == '__main__':
    unittest.main()
