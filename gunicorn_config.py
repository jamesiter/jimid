#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
import json
import multiprocessing


__author__ = 'James Iter'
__date__ = '2017/2/20'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2017 by James Iter.'


with open('./config.json', 'r') as f:
    config = json.load(f)

if not os.path.isdir(config['log_file_dir']):
    os.makedirs(config['log_file_dir'], 0755)


bind = '127.0.0.1:8001'
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'eventlet'
worker_connections = 1000
daemon = True

accesslog = sys.path[0] + '/logs/access.log'
errorlog = sys.path[0] + '/logs/error.log'
loglevel = 'info'

pidfile = './jimid.pid'
