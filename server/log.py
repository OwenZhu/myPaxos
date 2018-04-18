#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 22:17
# @Author  : Hanwei Zhu
# @File    : log.py


class Log(object):
    def __init__(self):
        self.entries = list()


class Entry(object):
    def __init__(self, term, index, command):
        self.term = term
        self.index = index
        self.command = command
