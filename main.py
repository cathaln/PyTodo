#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import mysql.connector
from PySide2.QtGui import QGuiApplication, QColor, QIcon
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import Qt, QAbstractListModel, QModelIndex, Slot

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
        self.mydb = SQLDatabase.get_db_instance()
        self.cursor = self.mydb.cursor()

    def get_color(self):
        return self._color

    def get_name(self):
        return self._name

    def get_description(self):

        if self._description == '':
            self.cursor.execute("SELECT description FROM todotasks WHERE name = '" + self._name + "'")
            self._description = self.cursor.fetchall()[0][0]
        return self._description



class BoardColumn(QAbstractListModel):

    '''
    Class for the board of todo's. Contains interaction with each Todo object created.
    '''

    ColorRole = Qt.UserRole + 1
    NameRole = Qt.UserRole + 2
    DescRole = Qt.UserRole + 3

    # allows QAbstractListModel to know which functions to call to
    # access issue attributes
    _roles = {ColorRole: b"get_color", NameRole: b"get_name", DescRole: b"get_description"}

    def __init__(self, parent=None):

        '''
        Initialisation of board. Creates todo list as well as populates it.
        '''

        QAbstractListModel.__init__(self, parent)

        self.mydb = SQLDatabase.get_db_instance()
        self.cursor = self.mydb.cursor()

        self._todos = []
        self.refresh_todos_list()

    def refresh_todos_list(self):

        '''
        Refreshes the list of todos on the board. Called whenever a todo is updated, added, or deleted,
        '''

        self.clearData()
        self.cursor.execute("SELECT name FROM todotasks")
        todo_names = self.cursor.fetchall()
        for todo in todo_names:
            self.addData(Todo(QColor('#607D8B'), str(todo[0])))

    def addData(self, todo):

        '''
        Adding a todo to the board.
        '''

        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._todos.append(todo)
        self.endInsertRows()

    @Slot(str)
    def removeData(self, todo):

        '''
        Delete a selected todo from the todo board.
        '''
        self.cursor.execute("DELETE FROM todotasks WHERE name = '" + todo + "'")
        self.mydb.commit()
        self.refresh_todos_list()


    def clearData(self):

        '''
        Clears the list containing the todos. Used as oart of the refresh.
        '''

        self.beginRemoveRows(QModelIndex(), 0, self.rowCount())
        self._todos.clear()
        self.endRemoveRows()

    def rowCount(self, parent=QModelIndex()):

        '''
        A getter for the list length.
        '''

        return len(self._todos)

    def data(self, index, role=Qt.DisplayRole):

        '''
        Used to allow QAbstractListModel to identify data.
        '''

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

        '''
        Getter for role names
        '''

        return self._roles

    @Slot(str, str)
    def update_todo(self, head_txt, body_txt):

        '''
        A slot method for updating an existing todo, adds new if not existing.
        '''
        self.cursor.execute("SELECT EXISTS(SELECT name FROM todotasks WHERE name = '" + head_txt + "')")
        pre_existing_entry = self.cursor.fetchall()[0][0]
        if pre_existing_entry < 1:
            self.cursor.execute("INSERT INTO todotasks (name, description) VALUES (%s, %s)", (head_txt, body_txt))
            self.mydb.commit()
        else:
            self.cursor.execute("UPDATE todotasks SET description = '" + body_txt + "' WHERE name = '" + head_txt + "'")
            self.mydb.commit()

        self.refresh_todos_list()


class SQLDatabase():

    @staticmethod
    def get_db_instance():

        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="todopass",
          database="PyTodo"
        )
        return mydb


if __name__ == '__main__':
    sys.argv += ['--style', 'material']
    app = QGuiApplication(sys.argv)
    app.setWindowIcon(QIcon('bluetick.png'))
    engine = QQmlApplicationEngine()

    board_todo = BoardColumn()

    root_context = engine.rootContext()
    root_context.setContextProperty('board_todo', board_todo)

    engine.load("QML/PyTodo.qml")


    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
