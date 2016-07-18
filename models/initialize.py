#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask
import logging
from logging.handlers import TimedRotatingFileHandler
import json
import os
import sys

import jimit as ji
from state_code import *


reload(sys)
sys.setdefaultencoding('utf8')


__author__ = 'James Iter'
__date__ = '16/6/8'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


app = Flask(__name__)


class Init(object):
    @staticmethod
    def init_config():
        with open('config.json', 'r') as f:
            config = json.load(f)
        app.config = dict(app.config, **config)
        ji.index_state['branch'] = dict(ji.index_state['branch'], **own_state_branch)

    @staticmethod
    def init_logger():
        app.config['log_file_base'] = ''.join([os.getcwd(), '/logs/log'])
        log_dir = os.path.dirname(app.config['log_file_base'])
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir, 0755)

        process_title = 'jimauth'
        log_file_path = '.'.join([app.config['log_file_base'], process_title])
        _logger = logging.getLogger(log_file_path)

        if app.config['debug']:
            app.config['DEBUG'] = True
            _logger.setLevel(logging.DEBUG)
        else:
            app.config['DEBUG'] = False
            _logger.setLevel(logging.INFO)

        fh = TimedRotatingFileHandler(log_file_path, when=app.config['log_cycle'], interval=1, backupCount=7)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(lineno)s - %(message)s')
        fh.setFormatter(formatter)
        _logger.addHandler(fh)
        return _logger


Init.init_config()
logger = Init.init_logger()

