#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2023.12.25 21:00:00                  #
# ================================================== #


class ModelItem:
    def __init__(self, id=None):
        """
        Model data item

        :param id: Model ID
        """
        self.id = id
        self.name = None
        self.mode = []
        self.langchain = {}
        self.ctx = 0
        self.tokens = 0
        self.default = False