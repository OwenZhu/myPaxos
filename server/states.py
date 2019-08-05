#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 20:00
# @Author  : Hanwei Zhu
# @File    : states.py


from collections import defaultdict
from threading import Timer
import random


def creat_timer(interval, hook=None):
    """Create a timer"""
    return Timer(interval, hook)


class BaseState(object):
    """Base state"""

    def __init__(self):
        pass


class Leader(BaseState):
    """Leader state
    """

    def __init__(self):
        super().__init__()
        self._next_indexes = defaultdict(int)
        self._match_index = defaultdict(int)

    def _append_entries(self):
        pass


ELECTION_TIMEOUT_MIN = 15  # sec
ELECTION_TIMEOUT_MAX = 30  # sec


class Follower(BaseState):
    """Follower state
    """

    def __init__(self):
        super().__init__()
        # Create timer to detect missing leader
        self.hooks = []
        self.election_timer = creat_timer(
            random.randint(ELECTION_TIMEOUT_MIN, ELECTION_TIMEOUT_MAX)
        )


class Candidate(BaseState):
    """Candidate state
    """

    def __init__(self):
        super().__init__()

    def request_vote(self):
        pass
