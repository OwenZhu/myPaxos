#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 20:52
# @Author  : Hanwei Zhu
# @File    : leader.py

from .state import State
from collections import defaultdict


class Leader(State):
    def __init__(self):
        self._nextIndexes = defaultdict(int)
        self._matchIndex = defaultdict(int)

    pass
