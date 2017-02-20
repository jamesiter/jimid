#!/usr/bin/env python
# -*- coding: utf-8 -*-


import multiprocessing


__author__ = 'James Iter'
__date__ = '2017/2/20'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2017 by James Iter.'


bind = '127.0.0.1:8001'
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'eventlet'
worker_connections = 1000
daemon = True

