#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import json
import unittest


__author__ = 'James Iter'
__date__ = '16/06/08'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


class TestUserMgmt(unittest.TestCase):

    base_url = 'http://jimauth.dev.iit.im/api'

    cookies = None
    batch_login_name_prefix = 'jamesc'
    login_name = batch_login_name_prefix + '1'
    password = 'password'
    password2 = 'password2'
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
    def test_10_sign_up(self):
        for i in range(1, TestUserMgmt.count):
            payload = {
                "login_name": TestUserMgmt.batch_login_name_prefix + i.__str__(),
                "password": TestUserMgmt.password
            }

            url = TestUserMgmt.base_url + '/user/_sign_up'
            headers = {'content-type': 'application/json'}
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            j_r = json.loads(r.content)
            print json.dumps(j_r, ensure_ascii=False)
            TestUserMgmt.uid_s.append(j_r['data']['id'])
            self.assertEqual('200', j_r['state']['code'])

    # ------------------------------------------------超级用户---------------------------------------------------------
    # 超级用户登录
    def test_11_sign_in_superuser(self):
        payload = {
            "login_name": TestUserMgmt.superuser_name,
            "password": TestUserMgmt.superuser_password
        }

        url = TestUserMgmt.base_url + '/user/_sign_in'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        TestUserMgmt.superuser_cookies = r.cookies
        self.assertEqual('200', j_r['state']['code'])

    # 超级用户通过用户登录名称获取用户信息
    def test_12_get_by_login_name(self):
        url = TestUserMgmt.base_url + '/user_mgmt/_by_login_name/' + TestUserMgmt.login_name
        r = requests.get(url, cookies=TestUserMgmt.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 普通用户登录
    def test_13_sign_in(self):
        payload = {
            "login_name": TestUserMgmt.login_name,
            "password": TestUserMgmt.password
        }

        url = TestUserMgmt.base_url + '/user/_sign_in'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        TestUserMgmt.cookies = r.cookies
        self.assertEqual('200', j_r['state']['code'])

    # 超级用户禁用普通用户
    def test_14_disable(self):
        url = TestUserMgmt.base_url + '/user_mgmt/_disable/' + TestUserMgmt.uid_s[0].__str__()
        r = requests.patch(url, cookies=TestUserMgmt.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 禁用普通用户后,普通用户重新获取自己的用户信息,应该返回失败,应该该用户已经被禁用
    def test_15_get(self):
        url = TestUserMgmt.base_url + '/user'
        r = requests.get(url, cookies=TestUserMgmt.cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('403', j_r['state']['code'])

    # 超级用户解禁普通用户
    def test_16_enable(self):
        url = TestUserMgmt.base_url + '/user_mgmt/_enable/' + TestUserMgmt.uid_s[0].__str__()
        r = requests.patch(url, cookies=TestUserMgmt.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 超级用户更改指定用户密码
    def test_17_change_password(self):
        payload = {
            "password": TestUserMgmt.password2
        }
        url = TestUserMgmt.base_url + '/user_mgmt/_change_password/' + TestUserMgmt.uid_s[0].__str__()
        headers = {'content-type': 'application/json'}
        r = requests.patch(url, cookies=TestUserMgmt.superuser_cookies, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 普通用户解禁后重新登录
    def test_18_re_sign_in(self):
        payload = {
            "login_name": TestUserMgmt.login_name,
            "password": TestUserMgmt.password2
        }

        url = TestUserMgmt.base_url + '/user/_sign_in'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        TestUserMgmt.cookies = r.cookies
        self.assertEqual('200', j_r['state']['code'])

    # 解禁普通用户后,普通用户重新获取自己的用户信息
    def test_19_get(self):
        url = TestUserMgmt.base_url + '/user'
        r = requests.get(url, cookies=TestUserMgmt.cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 超级用户自我禁用,应该返回失败,该系统不允许自我删除
    def test_20_disable(self):
        url = TestUserMgmt.base_url + '/user_mgmt/_disable/1'
        r = requests.patch(url, cookies=TestUserMgmt.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('403', j_r['state']['code'])

    # 超级用户自我删除,应该返回失败,该系统不允许自我删除
    def test_22_delete_superuser(self):
        url = TestUserMgmt.base_url + '/user_mgmt/1'
        r = requests.delete(url, cookies=TestUserMgmt.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('403', j_r['state']['code'])

    # ------------------------------------------------超级用户---------------------------------------------------------
    # 超级用户登录
    def test_31_sign_in_superuser(self):
        payload = {
            "login_name": TestUserMgmt.superuser_name,
            "password": TestUserMgmt.superuser_password
        }

        url = TestUserMgmt.base_url + '/user/_sign_in'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        TestUserMgmt.superuser_cookies = r.cookies
        self.assertEqual('200', j_r['state']['code'])

    # 超级用户获取用户列表，通过偏移量查询参数
    def test_32_get_list(self):
        url = TestUserMgmt.base_url + '/users_mgmt?offset=10&limit=5'
        r = requests.get(url, cookies=TestUserMgmt.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 超级用户获取用户列表，通过页控制查询参数
    def test_33_get_list_via_page(self):
        url = TestUserMgmt.base_url + '/users_mgmt?page=2&page_size=5'
        r = requests.get(url, cookies=TestUserMgmt.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 超级用户更新用户字段
    def test_34_update(self):
        payload = {
            "login_name": "new_login_namex",
            "mobile_phone": "15601603671",
            "mobile_phone_verified": True,
            "email": "jimit@qq.comm",
            "email_verified": True,
            "role_id": 0
        }

        url = TestUserMgmt.base_url + '/user_mgmt/' + TestUserMgmt.uid_s[10].__str__()
        headers = {'content-type': 'application/json'}
        r = requests.patch(url, cookies=TestUserMgmt.superuser_cookies, headers=headers, data=json.dumps(payload))
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 超级用户更新用户字段
    def test_35_update(self):
        payload = {
            "login_name": "new_login_name3",
        }

        url = TestUserMgmt.base_url + '/user_mgmt/' + TestUserMgmt.uid_s[11].__str__()
        headers = {'content-type': 'application/json'}
        r = requests.patch(url, cookies=TestUserMgmt.superuser_cookies, headers=headers, data=json.dumps(payload))
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 超级用户获取用户列表
    def test_37_get_list_via_page(self):
        url = TestUserMgmt.base_url + '/users_mgmt?page=3&page_size=5'
        r = requests.get(url, cookies=TestUserMgmt.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 超级用户全文检索
    def test_37_get_list_via_content_search(self):
        url = TestUserMgmt.base_url + '/users_mgmt/_search?page=1&page_size=5&keyword=a'
        r = requests.get(url, cookies=TestUserMgmt.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 超级用户删除普通用户
    def test_38_delete_via_superuser(self):
        for uid in TestUserMgmt.uid_s:
            url = TestUserMgmt.base_url + '/user_mgmt/' + uid.__str__()
            r = requests.delete(url, cookies=TestUserMgmt.superuser_cookies)
            j_r = json.loads(r.content)
            print json.dumps(j_r, ensure_ascii=False)
            self.assertEqual('200', j_r['state']['code'])

    # ------------------------------------------------普通用户---------------------------------------------------------
    # 注册普通用户
    def test_41_sign_up(self):
        TestUserMgmt.uid_s = list()
        for i in range(1, 4):
            payload = {
                "login_name": TestUserMgmt.login_name + i.__str__(),
                "password": TestUserMgmt.password
            }

            url = TestUserMgmt.base_url + '/user/_sign_up'
            headers = {'content-type': 'application/json'}
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            j_r = json.loads(r.content)
            print json.dumps(j_r, ensure_ascii=False)
            TestUserMgmt.uid_s.append(j_r['data']['id'])
            self.assertEqual('200', j_r['state']['code'])

    # 超级用户批量更新用户字段
    def test_42_update_by_uid_s(self):
        payload = {
            "ids": ','.join([str(TestUserMgmt.uid_s[0]), str(TestUserMgmt.uid_s[1]), str(TestUserMgmt.uid_s[2])]),
            "login_name": "new_login_name2",
            "email_verified": True,
            "mobile_phone_verified": True,
        }

        url = TestUserMgmt.base_url + '/users_mgmt'
        headers = {'content-type': 'application/json'}
        r = requests.patch(url, cookies=TestUserMgmt.superuser_cookies, headers=headers, data=json.dumps(payload))
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 超级用户批量删除普通用户
    def test_43_delete_by_uid_s(self):
        payload = {
            "ids": ','.join([str(TestUserMgmt.uid_s[0]), str(TestUserMgmt.uid_s[1]), str(TestUserMgmt.uid_s[2])]),
        }

        url = TestUserMgmt.base_url + '/users_mgmt'
        headers = {'content-type': 'application/json'}
        r = requests.delete(url, cookies=TestUserMgmt.superuser_cookies, headers=headers, data=json.dumps(payload))
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])


if __name__ == '__main__':
    unittest.main()
