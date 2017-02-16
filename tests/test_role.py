#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import json
import unittest

import jimit as ji


__author__ = 'James Iter'
__date__ = '16/06/08'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


class TestRole(unittest.TestCase):

    base_url = 'http://jimauth.dev.iit.im/api'
    cookies = None

    superuser_cookies = None
    superuser_name = 'admin'
    superuser_password = 'admin'

    uid = None
    app_id = None
    role_id = None

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # ------------------------------------------------超级用户---------------------------------------------------------
    # 超级用户登录
    def test_11_sign_in_superuser(self):
        payload = {
            "login_name": TestRole.superuser_name,
            "password": TestRole.superuser_password
        }

        url = TestRole.base_url + '/user/_sign_in'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        TestRole.superuser_cookies = r.cookies
        self.assertEqual('200', j_r['state']['code'])

    # 创建角色
    def test_12_create_role(self):
        payload = {
            "name": ji.Common.generate_random_code(length=6),
            "remark": ji.Common.generate_random_code(length=10, numeral=False)
        }
        url = TestRole.base_url + '/role'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, cookies=TestRole.superuser_cookies, headers=headers, data=json.dumps(payload))
        j_r = json.loads(r.content)
        TestRole.role_id = j_r['data']['id']
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 获取角色列表
    def test_13_get_list_via_page(self):
        url = TestRole.base_url + '/roles?page=1&page_size=5'
        r = requests.get(url, cookies=TestRole.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])
        TestRole.roles = j_r

    # 依据角色id获取应用
    def test_14_get_apps_via_role_id(self):
        url = TestRole.base_url + '/roles/_get_app_by_role_id/' + TestRole.role_id.__str__()
        r = requests.get(url, cookies=TestRole.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 更新角色字段
    def test_15_update(self):
        payload = {
            "name": ji.Common.generate_random_code(length=2),
            "remark": ji.Common.generate_random_code(length=20),
        }

        url = TestRole.base_url + '/role/' + TestRole.role_id.__str__()
        headers = {'content-type': 'application/json'}
        r = requests.patch(url, cookies=TestRole.superuser_cookies, headers=headers, data=json.dumps(payload))
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 注册普通用户
    def test_17_sign_up(self):
        payload = {
            "login_name": ji.Common.generate_random_code(length=6),
            "password": ji.Common.generate_random_code(length=16)
        }

        url = TestRole.base_url + '/user/_sign_up'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        TestRole.uid = j_r['data']['id']
        self.assertEqual('200', j_r['state']['code'])

    # 添加用户到角色
    def test_18_add_user_to_role(self):
        url = TestRole.base_url + '/role/_add_user_to_role/' + TestRole.role_id.__str__() + '/' + TestRole.uid.__str__()
        r = requests.post(url, cookies=TestRole.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 从角色删除用户
    def test_19_delete_user_from_role(self):
        url = TestRole.base_url + '/role/_delete_user_from_role/' + TestRole.role_id.__str__() + '/' + \
              TestRole.uid.__str__()
        r = requests.delete(url, cookies=TestRole.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 删除用户
    def test_20_delete_user(self):
        url = TestRole.base_url + '/user_mgmt/' + TestRole.uid.__str__()
        r = requests.delete(url, cookies=TestRole.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 创建应用
    def test_21_create_app(self):
        payload = {
            "name": ji.Common.generate_random_code(length=6),
        }
        url = TestRole.base_url + '/app'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, cookies=TestRole.superuser_cookies, headers=headers, data=json.dumps(payload))
        j_r = json.loads(r.content)
        TestRole.app_id = j_r['data']['id']
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 添加应用到角色
    def test_22_add_app_to_role(self):
        url = TestRole.base_url + '/role/_add_app_to_role/' + TestRole.role_id.__str__() + '/' + TestRole.app_id
        r = requests.post(url, cookies=TestRole.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 从角色中删除应用
    def test_23_delete_app_from_role(self):
        url = TestRole.base_url + '/role/_delete_app_from_role/' + TestRole.role_id.__str__() + '/' + TestRole.app_id
        r = requests.delete(url, cookies=TestRole.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 删除应用
    def test_24_delete_app(self):
        url = TestRole.base_url + '/app/' + TestRole.app_id
        r = requests.delete(url, cookies=TestRole.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 模糊查找不属于任何角色的用户
    def test_25_search_with_free_users(self):
        url = TestRole.base_url + '/roles/_search_with_free_users?keyword=james'
        r = requests.get(url, cookies=TestRole.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 删除角色
    def test_26_delete_role(self):
        url = TestRole.base_url + '/role/' + TestRole.role_id.__str__()
        r = requests.delete(url, cookies=TestRole.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

if __name__ == '__main__':
    unittest.main()
