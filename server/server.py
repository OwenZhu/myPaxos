#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 19:48
# @Author  : Hanwei Zhu
# @File    : server.py

from servers_config import ServersConfig
from log import Log
from ..state.candidate import Candidate


class Server(object):
    def __init__(self, name, state, log, conf):
        self._name = name
        self._state = state
        self._log = log
        self._server_list = conf.server_list
        self._total_nodes = conf.total_node

        self._commitIndex = 0
        self._currentTerm = 0

        self._lastApplied = 0

        self._lastLogIndex = 0
        self._lastLogTerm = None

        self._state.set_server(self)
        pass

    def run(self):
        pass

    def close(self):
        pass


if __name__ == '__main__':
    config = ServersConfig()
    server = Server(name="node_1", state=Candidate(), log=Log(), conf=config)
