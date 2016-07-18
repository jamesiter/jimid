#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import jimit as ji
from mysql.connector import errorcode, errors

from database import Database as db


__author__ = 'James Iter'
__date__ = '16/6/8'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


class Auth(object):
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
        sql_stmt = ("INSERT INTO auth (login_name, password, create_time, mobile_phone, email,"
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

        sql_stmt = ("UPDATE auth SET login_name = %(login_name)s, password = %(password)s,"
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

        sql_stmt = ("DELETE FROM auth WHERE id = %(id)s")

        cnx = db.cnxpool.get_connection()
        cursor = cnx.cursor(dictionary=True, buffered=True)
        try:
            cursor.execute(sql_stmt, self.__dict__)
            cnx.commit()
        finally:
            cursor.close()
            cnx.close()

    def get(self):
        sql_stmt = ("SELECT " + ', '.join(self.__dict__.keys()) + " FROM auth WHERE id = %(id)s LIMIT 1")

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
        sql_stmt = ("SELECT id FROM auth WHERE id = %(id)s LIMIT 1")

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
                    " FROM auth WHERE login_name = %(login_name)s LIMIT 1")

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
        sql_stmt = ("SELECT id FROM auth WHERE login_name = %(login_name)s LIMIT 1")

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

