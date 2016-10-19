#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import jimit as ji
from mysql.connector import errorcode, errors

from database import Database as db
from filter import FilterFieldType, Filter


__author__ = 'James Iter'
__date__ = '16/6/8'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


class User(object):
    def __init__(self, **kwargs):
        self.id = 0
        self.login_name = kwargs.get('login_name', None)
        self.password = kwargs.get('password', None)
        self.create_time = ji.Common.tus()
        self.mobile_phone = ''
        self.email = ''
        self.mobile_phone_verified = False
        self.email_verified = False
        self.enabled = True

    def create(self):
        sql_stmt = ("INSERT INTO user (login_name, password, create_time, mobile_phone, email,"
                    "mobile_phone_verified, email_verified, enabled) VALUES (%(login_name)s, %(password)s,"
                    "%(create_time)s, %(mobile_phone)s, %(email)s, %(mobile_phone_verified)s,"
                    "%(email_verified)s, %(enabled)s)")

        cnx = db.cnxpool.get_connection()
        cursor = cnx.cursor(dictionary=True, buffered=True)
        try:
            cursor.execute(sql_stmt, self.__dict__)
            cnx.commit()
        except errors.IntegrityError, e:
            if e.errno == errorcode.ER_DUP_ENTRY:
                ret = dict()
                ret['state'] = ji.Common.exchange_state(40901)
                ret['state']['sub']['zh-cn'] = ''.join([ret['state']['sub']['zh-cn'], ': ', self.login_name])
                raise ji.PreviewingError(json.dumps(ret, ensure_ascii=False))
        finally:
            cursor.close()
            cnx.close()

    def update(self):

        if not self.exist():
            ret = dict()
            ret['state'] = ji.Common.exchange_state(40401)
            ret['state']['sub']['zh-cn'] = ''.join([ret['state']['sub']['zh-cn'], ': ', self.id.__str__()])
            raise ji.PreviewingError(json.dumps(ret, ensure_ascii=False))

        sql_stmt = ("UPDATE user SET login_name = %(login_name)s, password = %(password)s,"
                    "create_time = %(create_time)s, mobile_phone = %(mobile_phone)s, email = %(email)s,"
                    "mobile_phone_verified = %(mobile_phone_verified)s, email_verified = %(email_verified)s,"
                    "enabled = %(enabled)s WHERE id = %(id)s")

        cnx = db.cnxpool.get_connection()
        cursor = cnx.cursor(dictionary=True, buffered=True)
        try:
            cursor.execute(sql_stmt, self.__dict__)
            cnx.commit()
        finally:
            cursor.close()
            cnx.close()

    def delete(self):
        if not self.exist():
            ret = dict()
            ret['state'] = ji.Common.exchange_state(40401)
            ret['state']['sub']['zh-cn'] = ''.join([ret['state']['sub']['zh-cn'], ': ', self.id.__str__()])
            raise ji.PreviewingError(json.dumps(ret, ensure_ascii=False))

        sql_stmt = ("DELETE FROM user WHERE id = %(id)s")

        cnx = db.cnxpool.get_connection()
        cursor = cnx.cursor(dictionary=True, buffered=True)
        try:
            cursor.execute(sql_stmt, self.__dict__)
            cnx.commit()
        finally:
            cursor.close()
            cnx.close()

    def get(self):
        sql_stmt = ("SELECT " + ', '.join(self.__dict__.keys()) + " FROM user WHERE id = %(id)s LIMIT 1")

        cnx = db.cnxpool.get_connection()
        cursor = cnx.cursor(dictionary=True, buffered=True)
        try:
            cursor.execute(sql_stmt, self.__dict__)
            row = cursor.fetchone()
        finally:
            cursor.close()
            cnx.close()

        if isinstance(row, dict):
            self.__dict__ = row
        else:
            ret = dict()
            ret['state'] = ji.Common.exchange_state(40401)
            ret['state']['sub']['zh-cn'] = ''.join([ret['state']['sub']['zh-cn'], ': ', self.id.__str__()])
            raise ji.PreviewingError(json.dumps(ret, ensure_ascii=False))

    def exist(self):
        sql_stmt = ("SELECT id FROM user WHERE id = %(id)s LIMIT 1")

        cnx = db.cnxpool.get_connection()
        cursor = cnx.cursor(dictionary=True, buffered=True)
        try:
            cursor.execute(sql_stmt, self.__dict__)
            row = cursor.fetchone()
        finally:
            cursor.close()
            cnx.close()

        if isinstance(row, dict):
            return True

        return False

    def get_by_login_name(self):
        sql_stmt = ("SELECT " + ', '.join(self.__dict__.keys()) +
                    " FROM user WHERE login_name = %(login_name)s LIMIT 1")

        cnx = db.cnxpool.get_connection()
        cursor = cnx.cursor(dictionary=True, buffered=True)
        try:
            cursor.execute(sql_stmt, self.__dict__)
            row = cursor.fetchone()
        finally:
            cursor.close()
            cnx.close()

        if isinstance(row, dict):
            self.__dict__ = row
        else:
            ret = dict()
            ret['state'] = ji.Common.exchange_state(40401)
            ret['state']['sub']['zh-cn'] = ''.join([ret['state']['sub']['zh-cn'], ': ', self.id.__str__()])
            raise ji.PreviewingError(json.dumps(ret, ensure_ascii=False))

    def exist_by_login_name(self):
        sql_stmt = ("SELECT id FROM user WHERE login_name = %(login_name)s LIMIT 1")

        cnx = db.cnxpool.get_connection()
        cursor = cnx.cursor(dictionary=True, buffered=True)
        try:
            cursor.execute(sql_stmt, self.__dict__)
            row = cursor.fetchone()
        finally:
            cursor.close()
            cnx.close()

        if isinstance(row, dict):
            return True

        return False

    @staticmethod
    def get_filter_keywords():
        # 指定参与过滤的关键字及其数据库对应字段类型
        keywords = {
            'id': FilterFieldType.INT.value,
            'login_name': FilterFieldType.STR.value,
            'create_time': FilterFieldType.INT.value,
            'mobile_phone': FilterFieldType.STR.value,
            'email': FilterFieldType.STR.value,
            'mobile_phone_verified': FilterFieldType.BOOL.value,
            'email_verified': FilterFieldType.BOOL.value,
            'enabled': FilterFieldType.BOOL.value
        }

        return keywords

    @classmethod
    def get_by_filter(cls, offset=0, limit=50, order_by='id', order='asc', filter_str=''):
        sql_stmt = ("SELECT * FROM user ORDER BY " + order_by + " " + order + " LIMIT %(offset)s, %(limit)s")
        sql_stmt_count = ("SELECT count(id) FROM user")
        where_str = Filter.filter_str_to_sql(allow_keywords=cls.get_filter_keywords(), filter_str=filter_str)
        if where_str != '':
            sql_stmt = ("SELECT * FROM user WHERE " + where_str + " ORDER BY " + order_by + " " + order +
                        " LIMIT %(offset)s, %(limit)s")
            sql_stmt_count = ("SELECT count(id) FROM user WHERE " + where_str)

        cnx = db.cnxpool.get_connection()
        cursor = cnx.cursor(dictionary=True, buffered=True)
        try:
            cursor.execute(sql_stmt, {'offset': offset, 'limit': limit})
            rows = cursor.fetchall()
            cursor.execute(sql_stmt_count)
            count = cursor.fetchone()
            return rows, count['count(id)']
        finally:
            cursor.close()
            cnx.close()

    @classmethod
    def update_by_filter(cls, kv, filter_str=''):
        allow_field = ['mobile_phone_verified', 'email_verified', 'enabled']

        # 过滤掉不予支持批量更新的字段
        _kv = {}
        for k, v in kv.iteritems():
            if k in allow_field:
                _kv[k] = v

        if _kv.__len__() < 1:
            return

        # set_str = ', '.join(map(lambda x: x + ' = %(' + x + ')s', _kv.keys()))
        # 上面为通过map实现的方式
        set_str = ', '.join([k + ' = %(' + k + ')s' for k in _kv.keys()])
        where_str = Filter.filter_str_to_sql(allow_keywords=cls.get_filter_keywords(), filter_str=filter_str)
        sql_stmt = ("UPDATE user SET " + set_str + " WHERE " + where_str)

        cnx = db.cnxpool.get_connection()
        cursor = cnx.cursor(dictionary=True, buffered=True)
        try:
            cursor.execute(sql_stmt, _kv)
            cnx.commit()
        finally:
            cursor.close()
            cnx.close()

    @classmethod
    def delete_by_filter(cls, filter_str=''):
        where_str = Filter.filter_str_to_sql(allow_keywords=cls.get_filter_keywords(), filter_str=filter_str)
        sql_stmt = ("DELETE FROM user WHERE " + where_str)

        cnx = db.cnxpool.get_connection()
        cursor = cnx.cursor(dictionary=True, buffered=True)
        try:
            cursor.execute(sql_stmt)
            cnx.commit()
        finally:
            cursor.close()
            cnx.close()

    @classmethod
    def content_search(cls, offset=0, limit=50, order_by='id', order='asc', keyword=''):
        allow_field = ['login_name', 'mobile_phone', 'email']
        _kv = dict()
        _kv = _kv.fromkeys(allow_field, '%' + keyword + '%')
        where_str = ' OR '.join([k + ' LIKE %(' + k + ')s' for k in _kv.keys()])
        sql_stmt = ("SELECT * FROM user WHERE " + where_str + " ORDER BY " + order_by + " " + order +
                    " LIMIT %(offset)s, %(limit)s")
        sql_stmt_count = ("SELECT count(id) FROM user WHERE " + where_str)

        _kv.update({'offset': offset, 'limit': limit})
        cnx = db.cnxpool.get_connection()
        cursor = cnx.cursor(dictionary=True, buffered=True)
        try:
            cursor.execute(sql_stmt, _kv)
            rows = cursor.fetchall()
            cursor.execute(sql_stmt_count, _kv)
            count = cursor.fetchone()
            return rows, count['count(id)']
        finally:
            cursor.close()
            cnx.close()
