#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/18 22:52
# @Author  : Hanwei Zhu
# @File    : state_machine.py


class StateMachine(object):
    def __init__(self):
        self.state_machine = dict()

    def read(self):
        return self.state_machine

    def write(self, key, value):
        self.state_machine[key] = value
