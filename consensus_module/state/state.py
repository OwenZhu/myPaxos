#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 20:00
# @Author  : Hanwei Zhu
# @File    : state.py


class State(object):
    def __init__(self):
        self.current_term = 0
        self.vote_for = None

    def set_server(self, server):
        pass
