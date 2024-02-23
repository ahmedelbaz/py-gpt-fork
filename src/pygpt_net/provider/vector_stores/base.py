#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2024.02.23 01:00:00                  #
# ================================================== #
import os
import shutil

from llama_index.indices.base import BaseIndex
from llama_index import (
    ServiceContext,
)


class BaseStore:
    def __init__(self, *args, **kwargs):
        """
        Base vector store provider

        :param args: args
        :param kwargs: kwargs
        """
        self.window = kwargs.get('window', None)
        self.id = None
        self.prefix = ""  # prefix for index directory
        self.indexes = {}

    def attach(self, window=None):
        """
        Attach window instance

        :param window: Window instance
        """
        self.window = window

    def get_path(self, id: str) -> str:
        """
        Get database path

        :param id: index name
        :return: database path
        """
        return os.path.join(
            self.window.core.config.get_user_dir('idx'),
            self.prefix + id,
        )

    def exists(self, id: str = None) -> bool:
        """
        Check if index with id exists

        :param id: index name
        :return: True if exists
        """
        path = self.get_path(id)
        return os.path.exists(path)

    def create(self, id: str):
        """
        Create empty index

        :param id: index name
        """
        pass

    def get(self, id: str, service_context: ServiceContext = None) -> BaseIndex:
        """
        Get index instance

        :param id: index name
        :param service_context: Service context
        :return: index instance
        """
        pass

    def store(self, id: str, index: BaseIndex = None):
        """
        Store/persist index

        :param id: index name
        :param index: index instance
        """
        pass

    def remove(self, id: str) -> bool:
        """
        Clear index

        :param id: index name
        :return: True if success
        """
        if id in self.indexes:
            self.indexes[id] = None
        path = self.get_path(id)
        if os.path.exists(path):
            shutil.rmtree(path)
        return True

    def truncate(self, id: str) -> bool:
        """
        Truncate index

        :param id: index name
        :return: True if success
        """
        return self.remove(id)

    def remove_document(self, id: str, doc_id: str) -> bool:
        """
        Remove document from index

        :param id: index name
        :param doc_id: document ID
        :return: True if success
        """
        index = self.get(id)
        index.delete(doc_id)
        self.store(
            id=id,
            index=index,
        )
        return True
