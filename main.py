#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from PySide2.QtGui import QGuiApplication, QColor
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import Qt, QAbstractListModel, QModelIndex

'''
Class for each issue raised in the board
'''
class Todo():

    '''
    Class for each Todo created.
    '''

    def __init__(self, color=QColor('#607D8B'), name="Default"):
        self._color = color
        self._name = name
        self._description = ''

    def get_color(self):
        return self._color

    def get_name(self):
        return self._name

    # needs work
    def get_description(self):
        if self._description == '':
            with open('./ToDoTasks/' + self._name) as filename:
                self._description = filename.read()
        return self._description



class BoardColumn(QAbstractListModel):

    '''
    Class for the board of todo's.
    '''

    ColorRole = Qt.UserRole + 1
    NameRole = Qt.UserRole + 2
    DescRole = Qt.UserRole + 3

    # allows QAbstractListModel to know which functions to call to
    # access issue attributes
    _roles = {ColorRole: b"get_color", NameRole: b"get_name", DescRole: b"get_description"}

    def __init__(self, parent=None):
        QAbstractListModel.__init__(self, parent)
        self._todos = []
        for todo in os.listdir(os.getcwd() + '/ToDoTasks'):
            self.addData(Todo(QColor('#607D8B'), todo))

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
        if role == self.NameRole:
            return data.get_name()
        if role == self.DescRole:
            return data.get_description()

        return QVariant()

    def roleNames(self):
        return self._roles



if __name__ == '__main__':
    sys.argv += ['--style', 'material']
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    board_todo = BoardColumn()

    root_context = engine.rootContext()
    root_context.setContextProperty('board_todo', board_todo)

    engine.load("QML/PyTodo.qml")


    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
