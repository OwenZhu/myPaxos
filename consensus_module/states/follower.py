#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 23:33
# @Author  : Hanwei Zhu
# @File    : follower.py

from .state import State


class Follower(State):
    def __init__(self):
        super().__init__()
