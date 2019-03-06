#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide2.QtGui import QGuiApplication, QColor
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import Qt, QAbstractListModel, QModelIndex

'''
Class for each issue raised in the board
'''
class Todo():
    def __init__(self, width=100, height=70, color=QColor('blue')):
        self._width = width
        self._height = height
        self._color = color

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_color(self):
        return self._color

class BoardColumn(QAbstractListModel):

    WidthRole = Qt.UserRole + 1
    HeightRole = Qt.UserRole + 2
    ColorRole = Qt.UserRole + 3

    # allows QAbstractListModel to know which functions to call to
    # access issue attributes
    _roles = {WidthRole: b"get_width", HeightRole: b"get_height", ColorRole: b"get_color"}

    def __init__(self, parent=None):
        QAbstractListModel.__init__(self, parent)
        self._todos = []

    def addData(self, todo):
            self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
            self._todos.append(todo)
            self.endInsertRows()

    def rowCount(self, parent=QModelIndex()):
        return len(self._todos)

    def data(self, index, role=Qt.DisplayRole):
        try:
            data = self._todos[index.row()]
        except IndexError:
            return QVariant()

        if role == self.WidthRole:
            return data.get_width()
        if role == self.HeightRole:
            return data.get_height()
        if role == self.ColorRole:
            return data.get_color()

        return QVariant()

    def roleNames(self):
        return self._roles



if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    board_col1 = BoardColumn()
    board_col1.addData(Todo(100, 70, QColor('lightblue')))
    board_col1.addData(Todo(120, 70, QColor('lightgreen')))
    board_col1.addData(Todo(80, 70, QColor('lightblue')))
    board_col1.addData(Todo(50, 70, QColor('lightgreen')))
    board_col1.addData(Todo(100, 70, QColor('lightblue')))
    board_col1.addData(Todo(120, 70, QColor('lightgreen')))
    board_col1.addData(Todo(130, 70, QColor('lightblue')))
    board_col1.addData(Todo(180, 70, QColor('lightgreen')))

    root_context = engine.rootContext()
    root_context.setContextProperty('board_col1', board_col1)

    engine.load("PyTodo.qml")


    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
