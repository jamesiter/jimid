#!/usr/bin/env python
# -*- coding: utf-8 -*-


from abc import ABCMeta, abstractmethod


__author__ = 'James Iter'
__date__ = '2016/10/2'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


class CURD(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass


class ExtCURD(CURD):
    __metaclass__ = ABCMeta

    def __init__(self):
        super(ExtCURD, self).__init__()

    @abstractmethod
    def get_by_filter(self):
        pass

    @abstractmethod
    def update_by_filter(self):
        pass

    @abstractmethod
    def delete_by_filter(self):
        pass

