#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import json
import unittest


__author__ = 'James Iter'
__date__ = '16/06/08'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


class TestAppKey(unittest.TestCase):

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
            "login_name": TestAppKey.superuser_name,
            "password": TestAppKey.superuser_password
        }

        url = 'http://jimauth.dev.iit.im/user/_sign_in'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        TestAppKey.superuser_cookies = r.cookies
        self.assertEqual('200', j_r['state']['code'])

    # 创业appkey
    def test_12_create_app_key(self):
        payload = {
            "remark": "remark",
        }
        url = 'http://jimauth.dev.iit.im/app_key'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, cookies=TestAppKey.superuser_cookies, headers=headers, data=json.dumps(payload))
        j_r = json.loads(r.content)
        TestAppKey.app_id = j_r['data']['id']
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 获取appkey列表
    def test_13_get_list_via_page(self):
        url = 'http://jimauth.dev.iit.im/app_keys?page=1&page_size=5'
        r = requests.get(url, cookies=TestAppKey.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 更新appkey字段
    def test_14_update(self):
        payload = {
            "id": TestAppKey.app_id,
            "remark": "new remark"
        }

        url = 'http://jimauth.dev.iit.im/app_key'
        headers = {'content-type': 'application/json'}
        r = requests.patch(url, cookies=TestAppKey.superuser_cookies, headers=headers, data=json.dumps(payload))
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # appkey全文检索
    def test_17_get_list_via_content_search(self):
        url = 'http://jimauth.dev.iit.im/app_keys/_search?page=1&page_size=5&keyword=a'
        r = requests.get(url, cookies=TestAppKey.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])

    # 删除appkey
    def test_18_delete(self):
        url = 'http://jimauth.dev.iit.im/app_key/' + TestAppKey.app_id
        r = requests.delete(url, cookies=TestAppKey.superuser_cookies)
        j_r = json.loads(r.content)
        print json.dumps(j_r, ensure_ascii=False)
        self.assertEqual('200', j_r['state']['code'])


if __name__ == '__main__':
    unittest.main()
