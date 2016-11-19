#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import jimit as ji
from mysql.connector import errorcode, errors

from database import Database as db
from filter import FilterFieldType, Filter


__author__ = 'James Iter'
__date__ = '16/11/5'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


class UidOpenidMapping(object):
    def __init__(self, **kwargs):
        self.uid = kwargs.get('uid', 0)
        self.appid = kwargs.get('appid', None)
        self.openid = kwargs.get('openid', None)
        self.create_time = ji.Common.tus()

    def create(self):
        sql_stmt = ("INSERT INTO uid_openid_mapping (uid, appid, openid, create_time) VALUES (%(uid)s, %(appid)s, "
                    "%(openid)s, %(create_time)s)")

        cnx = db.cnxpool.get_connection()
        cursor = cnx.cursor(dictionary=True, buffered=True)
        try:
            cursor.execute(sql_stmt, self.__dict__)
            cnx.commit()
        except errors.IntegrityError, e:
            if e.errno == errorcode.ER_DUP_ENTRY:
                ret = dict()
                ret['state'] = ji.Common.exchange_state(40901)
                ret['state']['sub']['zh-cn'] = ''.join([ret['state']['sub']['zh-cn'], ': ', e.msg])
                raise ji.PreviewingError(json.dumps(ret, ensure_ascii=False))
        finally:
            cursor.close()
            cnx.close()

    def update(self):

        if not self.exist():
            ret = dict()
            ret['state'] = ji.Common.exchange_state(40401)
            ret['state']['sub']['zh-cn'] = ''.join([ret['state']['sub']['zh-cn'], ': uid -> ', self.uid.__str__(),
                                                   ', appid -> ', self.appid])
            raise ji.PreviewingError(json.dumps(ret, ensure_ascii=False))

        sql_stmt = ("UPDATE uid_openid_mapping SET uid = %(uid)s, appid = %(appid)s "
                    "WHERE uid = %(id)s AND appid = %(appid)s")

        cnx = db.cnxpool.get_connection()
        cursor = cnx.cursor(dictionary=True, buffered=True)
        try:
            cursor.execute(sql_stmt, self.__dict__)
            cnx.commit()
        except errors.IntegrityError, e:
            if e.errno == errorcode.ER_DUP_ENTRY:
                ret = dict()
                ret['state'] = ji.Common.exchange_state(40901)
                ret['state']['sub']['zh-cn'] = ''.join([ret['state']['sub']['zh-cn'], ': ', e.msg])
                raise ji.PreviewingError(json.dumps(ret, ensure_ascii=False))
        finally:
            cursor.close()
            cnx.close()

    def delete(self):
        if not self.exist():
            ret = dict()
            ret['state'] = ji.Common.exchange_state(40401)
            ret['state']['sub']['zh-cn'] = ''.join([ret['state']['sub']['zh-cn'], ': uid -> ', self.uid.__str__(),
                                                    ', appid -> ', self.appid])
            raise ji.PreviewingError(json.dumps(ret, ensure_ascii=False))

        sql_stmt = ("DELETE FROM uid_openid_mapping WHERE uid = %(uid)s AND appid = %(appid)s")

        cnx = db.cnxpool.get_connection()
        cursor = cnx.cursor(dictionary=True, buffered=True)
        try:
            cursor.execute(sql_stmt, self.__dict__)
            cnx.commit()
        finally:
            cursor.close()
            cnx.close()

    def get(self):
        sql_stmt = ("SELECT " + ', '.join(self.__dict__.keys()) + " FROM uid_openid_mapping "
                                                                  "WHERE uid = %(uid)s AND appid = %(appid)s LIMIT 1")

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
            ret['state']['sub']['zh-cn'] = ''.join([ret['state']['sub']['zh-cn'], ': uid -> ', self.uid.__str__(),
                                                    ', appid -> ', self.appid])
            raise ji.PreviewingError(json.dumps(ret, ensure_ascii=False))

    def exist(self):
        sql_stmt = ("SELECT uid FROM uid_openid_mapping WHERE uid = %(uid)s AND appid = %(appid)s LIMIT 1")

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

    def get_by(self, field):
        """
        必须在实例中指定appid
        :param field: 过滤的字段
        :return: 成功则返回None
        """
        sql_field = field + ' = %(' + field + ')s'
        sql_stmt = ("SELECT " + ', '.join(self.__dict__.keys()) +
                    " FROM uid_openid_mapping WHERE appid = %(appid)s " + sql_field + " LIMIT 1")

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
            ret['state']['sub']['zh-cn'] = ''.join([ret['state']['sub']['zh-cn'], ': uid -> ', self.uid.__str__(),
                                                    ', appid -> ', self.appid])
            raise ji.PreviewingError(json.dumps(ret, ensure_ascii=False))

    def exist_by(self, field):
        sql_field = field + ' = %(' + field + ')s'
        sql_stmt = ("SELECT uid FROM uid_openid_mapping WHERE appid = %(appid)s " + sql_field + " LIMIT 1")

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
            'uid': FilterFieldType.INT.value,
            'appid': FilterFieldType.STR.value,
            'openid': FilterFieldType.STR.value,
            'create_time': FilterFieldType.INT.value
        }

        return keywords

    @classmethod
    def get_by_filter(cls, offset=0, limit=50, order_by='uid', order='asc', filter_str=''):
        sql_stmt = ("SELECT * FROM uid_openid_mapping ORDER BY " + order_by + " " + order +
                    " LIMIT %(offset)s, %(limit)s")
        sql_stmt_count = ("SELECT count(uid) FROM uid_openid_mapping")
        where_str = Filter.filter_str_to_sql(allow_keywords=cls.get_filter_keywords(), filter_str=filter_str)
        if where_str != '':
            sql_stmt = ("SELECT * FROM uid_openid_mapping WHERE " + where_str + " ORDER BY " + order_by + " " + order +
                        " LIMIT %(offset)s, %(limit)s")
            sql_stmt_count = ("SELECT count(uid) FROM uid_openid_mapping WHERE " + where_str)

        cnx = db.cnxpool.get_connection()
        cursor = cnx.cursor(dictionary=True, buffered=True)
        try:
            cursor.execute(sql_stmt, {'offset': offset, 'limit': limit})
            rows = cursor.fetchall()
            cursor.execute(sql_stmt_count)
            count = cursor.fetchone()
            return rows, count['count(uid)']
        finally:
            cursor.close()
            cnx.close()

    @classmethod
    def update_by_filter(cls, kv, filter_str=''):
        allow_field = ['uid', 'appid', 'openid']

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
        sql_stmt = ("UPDATE uid_openid_mapping SET " + set_str + " WHERE " + where_str)

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
        sql_stmt = ("DELETE FROM uid_openid_mapping WHERE " + where_str)

        cnx = db.cnxpool.get_connection()
        cursor = cnx.cursor(dictionary=True, buffered=True)
        try:
            cursor.execute(sql_stmt)
            cnx.commit()
        finally:
            cursor.close()
            cnx.close()

    @classmethod
    def content_search(cls, offset=0, limit=50, order_by='uid', order='asc', keyword=''):
        allow_field = ['uid', 'appid', 'openid']
        _kv = dict()
        _kv = _kv.fromkeys(allow_field, '%' + keyword + '%')
        where_str = ' OR '.join([k + ' LIKE %(' + k + ')s' for k in _kv.keys()])
        sql_stmt = ("SELECT * FROM uid_openid_mapping WHERE " + where_str + " ORDER BY " + order_by + " " + order +
                    " LIMIT %(offset)s, %(limit)s")
        sql_stmt_count = ("SELECT count(uid) FROM uid_openid_mapping WHERE " + where_str)

        _kv.update({'offset': offset, 'limit': limit})
        cnx = db.cnxpool.get_connection()
        cursor = cnx.cursor(dictionary=True, buffered=True)
        try:
            cursor.execute(sql_stmt, _kv)
            rows = cursor.fetchall()
            cursor.execute(sql_stmt_count, _kv)
            count = cursor.fetchone()
            return rows, count['count(uid)']
        finally:
            cursor.close()
            cnx.close()
