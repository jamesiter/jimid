#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import json
import unittest


__author__ = 'James Iter'
__date__ = '16/06/08'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


class TestAuth(unittest.TestCase):

    cookies = None
    uid = 0
    login_name = 'james'
    password = 'password'
    password2 = 'password2'

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
            "login_name": TestAuth.login_name,
            "password": TestAuth.password
        }

        url = 'http://jimauth.dev.iit.im/auth/_sign_up'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 普通用户登录
    def test_12_sign_in(self):
        payload = {
            "login_name": TestAuth.login_name,
            "password": TestAuth.password
        }

        url = 'http://jimauth.dev.iit.im/auth/_sign_in'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        TestAuth.cookies = r.cookies
        self.assertEqual('200', j_r['state']['code'])

    # 普通用户获取自己的用户信息
    def test_13_get(self):
        url = 'http://jimauth.dev.iit.im/auth'
        r = requests.get(url, cookies=TestAuth.cookies)
        j_r = json.loads(r.content)
        TestAuth.uid = j_r['obj']['id']
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 普通用户通过token自我验证
    def test_14_auth(self):
        url = 'http://jimauth.dev.iit.im/auth/_auth'
        r = requests.get(url, cookies=TestAuth.cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 普通用户更改登录密码
    def test_15_change_password(self):
        payload = {
            "password": TestAuth.password2
        }
        url = 'http://jimauth.dev.iit.im/auth/_change_password'
        headers = {'content-type': 'application/json'}
        r = requests.patch(url, cookies=TestAuth.cookies, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 普通用户更改密码后重新登录
    def test_16_re_sign_in(self):
        payload = {
            "login_name": TestAuth.login_name,
            "password": TestAuth.password2
        }

        url = 'http://jimauth.dev.iit.im/auth/_sign_in'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        TestAuth.cookies = r.cookies
        self.assertEqual('200', j_r['state']['code'])

    # 普通用户重新获取自己的用户信息
    def test_17_get(self):
        url = 'http://jimauth.dev.iit.im/auth'
        r = requests.get(url, cookies=TestAuth.cookies)
        j_r = json.loads(r.content)
        TestAuth.uid = j_r['obj']['id']
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 测试普通用户通过登录名获取用户信息,应该返回失败,该接口只给超级用户使用
    def test_18_get_by_login_name(self):
        url = 'http://jimauth.dev.iit.im/mgmt/_by_login_name/' + TestAuth.login_name
        r = requests.get(url, cookies=TestAuth.cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('403', j_r['state']['code'])

    # 测试普通用户通过token禁用自己,应该返回失败,该接口只给超级用户使用
    def test_19_disable(self):
        url = 'http://jimauth.dev.iit.im/mgmt/_disable/' + TestAuth.uid.__str__()
        r = requests.patch(url, cookies=TestAuth.cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('403', j_r['state']['code'])

    # 测试普通用户通过token解禁自己,应该返回失败,该接口只给超级用户使用
    def test_20_enable(self):
        url = 'http://jimauth.dev.iit.im/mgmt/_enable/' + TestAuth.uid.__str__()
        r = requests.patch(url, cookies=TestAuth.cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('403', j_r['state']['code'])

    # 测试普通用户自我删除,应该返回失败,该系统不允许自我删除,而且删除权限只有超级用户拥有
    def test_21_delete(self):
        url = 'http://jimauth.dev.iit.im/mgmt/' + TestAuth.uid.__str__()
        r = requests.delete(url, cookies=TestAuth.cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('403', j_r['state']['code'])

    # ------------------------------------------------超级用户---------------------------------------------------------
    # 超级用户登录
    def test_31_sign_in_superuser(self):
        payload = {
            "login_name": TestAuth.superuser_name,
            "password": TestAuth.superuser_password
        }

        url = 'http://jimauth.dev.iit.im/auth/_sign_in'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        TestAuth.superuser_cookies = r.cookies
        self.assertEqual('200', j_r['state']['code'])

    # 超级用户通过用户登录名称获取用户信息
    def test_32_get_by_login_name(self):
        url = 'http://jimauth.dev.iit.im/mgmt/_by_login_name/' + TestAuth.login_name
        r = requests.get(url, cookies=TestAuth.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 超级用户禁用普通用户
    def test_33_disable(self):
        url = 'http://jimauth.dev.iit.im/mgmt/_disable/' + TestAuth.uid.__str__()
        r = requests.patch(url, cookies=TestAuth.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 禁用普通用户后,普通用户重新获取自己的用户信息,应该返回失败,应该该用户已经被禁用
    def test_34_get(self):
        url = 'http://jimauth.dev.iit.im/auth'
        r = requests.get(url, cookies=TestAuth.cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('403', j_r['state']['code'])

    # 超级用户解禁普通用户
    def test_35_enable(self):
        url = 'http://jimauth.dev.iit.im/mgmt/_enable/' + TestAuth.uid.__str__()
        r = requests.patch(url, cookies=TestAuth.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 解禁普通用户后,普通用户重新获取自己的用户信息
    def test_36_get(self):
        url = 'http://jimauth.dev.iit.im/auth'
        r = requests.get(url, cookies=TestAuth.cookies)
        j_r = json.loads(r.content)
        TestAuth.uid = j_r['obj']['id']
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 超级用户自我禁用,应该返回失败,该系统不允许自我删除
    def test_37_disable(self):
        url = 'http://jimauth.dev.iit.im/mgmt/_disable/1'
        r = requests.patch(url, cookies=TestAuth.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('403', j_r['state']['code'])

    # 超级用户删除普通用户
    def test_38_delete_via_superuser(self):
        url = 'http://jimauth.dev.iit.im/mgmt/' + TestAuth.uid.__str__()
        r = requests.delete(url, cookies=TestAuth.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 超级用户自我删除,应该返回失败,该系统不允许自我删除
    def test_39_delete_superuser(self):
        url = 'http://jimauth.dev.iit.im/mgmt/1'
        r = requests.delete(url, cookies=TestAuth.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('403', j_r['state']['code'])


if __name__ == '__main__':
    unittest.main()
