#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2024.02.02 17:00:00                  #
# ================================================== #

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QHBoxLayout, QWidget, QSplitter, QSizePolicy, QRadioButton

from pygpt_net.ui.widget.calendar.select import CalendarSelect
from pygpt_net.ui.widget.element.labels import HelpLabel
from pygpt_net.ui.widget.textarea.calendar_note import CalendarNote
from pygpt_net.utils import trans


class Calendar:
    def __init__(self, window=None):
        """
        Calendar UI

        :param window: Window instance
        """
        self.window = window

    def setup(self) -> QWidget:
        """
        Setup calendar

        :return: QWidget
        """
        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.setup_calendar())
        layout.setContentsMargins(0, 0, 0, 0)

        widget = QWidget()
        widget.setLayout(layout)

        return widget

    def setup_filters(self) -> QWidget:
        """
        Setup calendar filters

        :return: QWidget
        """
        self.window.ui.nodes['filter.ctx.label'] = QLabel(trans("filter.ctx.label"))

        # display: all
        self.window.ui.nodes['filter.ctx.radio.all'] = QRadioButton(trans("filter.ctx.radio.all"))
        self.window.ui.nodes['filter.ctx.radio.all'].clicked.connect(
            lambda: self.window.controller.ctx.common.toggle_display_filter("all"))

        # display: only pinned
        self.window.ui.nodes['filter.ctx.radio.pinned'] = QRadioButton(trans("filter.ctx.radio.pinned"))
        self.window.ui.nodes['filter.ctx.radio.pinned'].clicked.connect(
            lambda: self.window.controller.ctx.common.toggle_display_filter("pinned"))

        # display: only labeled
        self.window.ui.nodes['filter.ctx.radio.labeled'] = QRadioButton(trans("filter.ctx.radio.labeled"))
        self.window.ui.nodes['filter.ctx.radio.labeled'].clicked.connect(
            lambda: self.window.controller.ctx.common.toggle_display_filter("labeled"))

        # display: only indexed
        self.window.ui.nodes['filter.ctx.radio.indexed'] = QRadioButton(trans("filter.ctx.radio.indexed"))
        self.window.ui.nodes['filter.ctx.radio.indexed'].clicked.connect(
            lambda: self.window.controller.ctx.common.toggle_display_filter("indexed"))

        # layout
        layout = QHBoxLayout()
        layout.addWidget(self.window.ui.nodes['filter.ctx.label'])
        layout.addWidget(self.window.ui.nodes['filter.ctx.radio.all'])
        layout.addWidget(self.window.ui.nodes['filter.ctx.radio.pinned'])
        layout.addWidget(self.window.ui.nodes['filter.ctx.radio.labeled'])
        layout.addWidget(self.window.ui.nodes['filter.ctx.radio.indexed'])
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        return widget

    def setup_calendar(self) -> QHBoxLayout:
        """
        Setup calendar

        :return: QSplitter
        """
        # calendar
        self.window.ui.calendar['select'] = CalendarSelect(self.window)
        self.window.ui.calendar['select'].setMinimumHeight(200)
        self.window.ui.calendar['select'].setMinimumWidth(200)
        self.window.ui.calendar['select'].setGridVisible(True)

        self.window.ui.calendar['note'] = CalendarNote(self.window)

        self.window.ui.nodes['tip.output.tab.calendar'] = HelpLabel(trans('tip.output.tab.calendar'), self.window)

        # note
        self.window.ui.calendar['note.label'] = QLabel(trans('calendar.note.label'))
        layout = QVBoxLayout()
        layout.addWidget(self.window.ui.calendar['note.label'])
        layout.addWidget(self.window.ui.calendar['note'])
        layout.addWidget(self.window.ui.nodes['tip.output.tab.calendar'])
        layout.setContentsMargins(0, 0, 0, 0)

        widget = QWidget()
        widget.setLayout(layout)

        filters = self.setup_filters()

        # layout / splitter
        self.window.ui.splitters['calendar'] = QSplitter(Qt.Horizontal)
        self.window.ui.splitters['calendar'].addWidget(self.window.ui.calendar['select'])
        self.window.ui.splitters['calendar'].addWidget(widget)
        self.window.ui.splitters['calendar'].setStretchFactor(0, 6)  # 60%
        self.window.ui.splitters['calendar'].setStretchFactor(1, 4)  # 40%

        self.window.ui.splitters['calendar'].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        filters.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout = QVBoxLayout()
        layout.addWidget(self.window.ui.splitters['calendar'])
        layout.addWidget(filters)

        widget = QWidget()
        widget.setLayout(layout)

        return widget

