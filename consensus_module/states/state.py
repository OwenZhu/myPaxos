#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 20:00
# @Author  : Hanwei Zhu
# @File    : states.py


class State(object):
    def __init__(self):
        self._server = None

    def set_server(self, server):
        self._server = server
