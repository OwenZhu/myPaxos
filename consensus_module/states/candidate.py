#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 22:20
# @Author  : Hanwei Zhu
# @File    : candidate.py

from .state import State


class Candidate(State):
    def __init__(self):
        super().__init__()

    def request_vote(self):
        pass
