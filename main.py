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
    def __init__(self, color=QColor('blue'), text="Default"):
        self._color = color
        self._text = text

    def get_color(self):
        return self._color

    def get_text(self):
        return self._text

class BoardColumn(QAbstractListModel):

    ColorRole = Qt.UserRole + 1
    TextRole = Qt.UserRole + 2

    # allows QAbstractListModel to know which functions to call to
    # access issue attributes
    _roles = {ColorRole: b"get_color", TextRole: b"get_text"}

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

        if role == self.ColorRole:
            return data.get_color()
        if role == self.TextRole:
            return data.get_text()

        return QVariant()

    def roleNames(self):
        return self._roles



if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    board_col_todo = BoardColumn()
    board_col_towork = BoardColumn()
    board_col_done = BoardColumn()

    board_col_todo.addData(Todo(QColor('lightblue'), "Work"))
    board_col_todo.addData(Todo(QColor('lightgreen'), "Clean"))

    board_col_towork.addData(Todo(QColor('lightgreen'), "Fix"))
    board_col_towork.addData(Todo(QColor('steelblue'), "Poo"))

    board_col_done.addData(Todo(QColor('steelblue'), "Swim"))

    root_context = engine.rootContext()
    root_context.setContextProperty('board_col_todo', board_col_todo)
    root_context.setContextProperty('board_col_towork', board_col_towork)
    root_context.setContextProperty('board_col_done', board_col_done)

    engine.load("PyTodo.qml")


    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
