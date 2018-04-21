#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 19:48
# @Author  : Hanwei Zhu
# @File    : server.py

from servers_config import ServersConfig
from log import Log
import threading
from state_machine import StateMachine


class Server(object):
    def __init__(self, name, state, conf):
        self._name = name

        # consensus module
        self._state = state

        self._log = Log()
        self._state_machine = StateMachine()
        self._server_list = conf.server_list
        self._total_nodes = conf.total_node

        self._commit_index = 0
        self._current_term = 0

        self._last_applied = 0
        self._last_log_index = 0
        self._last_log_term = None

        self._state.set_server(self)

        class ReadThread(threading.Thread):
            def run(thread):
                pass

        class WriteThread(threading.Thread):
            def run(thread):
                pass

        self.read_thread = ReadThread()
        self.write_thread = WriteThread()

        self.read_thread.daemon = True
        self.read_thread.start()
        self.write_thread.daemon = True
        self.write_thread.start()
