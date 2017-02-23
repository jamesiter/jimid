#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import json
import unittest


__author__ = 'James Iter'
__date__ = '16/06/08'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


class TestApp(unittest.TestCase):

    base_url = 'http://127.0.0.1:8001/api'

    app_id = None

    cookies = None
    login_name = 'james'
    password = 'password'

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
            "login_name": TestApp.superuser_name,
            "password": TestApp.superuser_password
        }

        url = TestApp.base_url + '/user/_sign_in'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        TestApp.superuser_cookies = r.cookies
        self.assertEqual('200', j_r['state']['code'])

    # 创建app
    def test_12_create_app(self):
        payload = {
            "name": "OA",
            "home_page": "http://oa.jimid.org",
            "remark": "办公自动化系统",
        }
        url = TestApp.base_url + '/app'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, cookies=TestApp.superuser_cookies, headers=headers, data=json.dumps(payload))
        j_r = json.loads(r.content)
        TestApp.app_id = j_r['data']['id']
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 获取app列表
    def test_13_get_list_via_page(self):
        url = TestApp.base_url + '/apps?page=1&page_size=5'
        r = requests.get(url, cookies=TestApp.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 更新app字段
    def test_14_update(self):
        payload = {
            "secret": True,
            "name": "新应用",
            "home_page": "http://new.jimid.org",
        }

        url = TestApp.base_url + '/app/' + TestApp.app_id
        headers = {'content-type': 'application/json'}
        r = requests.patch(url, cookies=TestApp.superuser_cookies, headers=headers, data=json.dumps(payload))
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # app全文检索
    def test_15_get_list_via_content_search(self):
        url = TestApp.base_url + '/apps/_search?page=1&page_size=5&keyword=oa'
        r = requests.get(url, cookies=TestApp.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 删除app
    def test_16_delete(self):
        url = TestApp.base_url + '/app/' + TestApp.app_id
        r = requests.delete(url, cookies=TestApp.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])


if __name__ == '__main__':
    unittest.main()
