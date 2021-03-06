# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QTableWidgetItem, QHeaderView
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import pymysql
import sys
from table import *
from query import *

class Show(QtWidgets.QMainWindow):
    def __init__(self):
        super(Show,self).__init__()
        self.commandLinkButton = None
        self.commandLinkButton_2 = None
        self.commandLinkButton_3 = None
        self.commandLinkButton_4 = None
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(694, 526)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 80, 181, 321))
        self.widget.setObjectName("widget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.widget)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.verticalLayout.addWidget(self.commandLinkButton)

        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.widget)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.verticalLayout.addWidget(self.commandLinkButton_2)

        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.widget)
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.verticalLayout.addWidget(self.commandLinkButton_3)

        # self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(self.widget)
        # self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        # self.verticalLayout.addWidget(self.commandLinkButton_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        self.commandLinkButton.clicked.connect(self.get_student_list)
        self.commandLinkButton_2.clicked.connect(self.get_teacher_list)
        self.commandLinkButton_3.clicked.connect(self.query)
        # self.commandLinkButton_4.clicked.connect(self.get_course_list)



    def get_student_list(self):
        con = pymysql.connect(host='localhost', port=3306, user='root', password='fkl001206', charset='utf8',
                              database='lab1')  # ???????????????
        cur = con.cursor()  # ??????sql???????????????
        sql = "SELECT * FROM student"
        cur.execute(sql)
        result = cur.fetchall()
        self.ui_1 = Table()
        if result:
            self.ui_1.tableWidget.setRowCount(len(result))  # ????????????
            self.ui_1.tableWidget.setColumnCount(len(result[0]))  # ??????0???
            self.ui_1.tableWidget.setHorizontalHeaderLabels(['??????', '??????', '????????????', '??????', '?????????'])
            print(len(result))
            print(len(result[0]))
            for row, form in enumerate(result):
                for column, item in enumerate(form):
                    self.ui_1.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))  # ??????????????????
                    column += 1
                row_postition = self.ui_1.tableWidget.rowCount()
                self.ui_1.tableWidget.insertRow(row_postition)
            self.ui_1.show()
        cur.close()
        con.close()


    def get_teacher_list(self):
        con = pymysql.connect(host='localhost', port=3306, user='root', password='fkl001206', charset='utf8',
                              database='lab1')  # ???????????????
        cur = con.cursor()  # ??????sql???????????????
        sql = "SELECT * FROM teacher"
        cur.execute(sql)
        result = cur.fetchall()
        self.ui_1 = Table()
        if result:
            self.ui_1.tableWidget.setRowCount(len(result))  # ????????????
            self.ui_1.tableWidget.setColumnCount(len(result[0]))  # ??????0???
            self.ui_1.tableWidget.setHorizontalHeaderLabels(['?????????', '??????', '????????????'])
            for row, form in enumerate(result):
                for column, item in enumerate(form):
                    self.ui_1.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))  # ??????????????????
                    column += 1
                row_postition = self.ui_1.tableWidget.rowCount()
                self.ui_1.tableWidget.insertRow(row_postition)
            self.ui_1.show()
        cur.close()
        con.close()

    def get_course_list(self):
        con = pymysql.connect(host='localhost', port=3306, user='root', password='fkl001206', charset='utf8',
                              database='lab1')  # ???????????????
        cur = con.cursor()  # ??????sql???????????????
        sql = "SELECT * FROM sc"
        cur.execute(sql)
        result = cur.fetchall()
        self.ui_1 = Table()
        if result:
            self.ui_1.tableWidget.setRowCount(len(result))  # ????????????
            self.ui_1.tableWidget.setColumnCount(len(result[0]))  # ??????o???
            self.ui_1.tableWidget.setHorizontalHeaderLabels(['?????????', '??????', '??????'])
            for row, form in enumerate(result):
                for column, item in enumerate(form):
                    self.ui_1.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))  # ??????????????????
                    column += 1
                row_postition = self.ui_1.tableWidget.rowCount()
                self.ui_1.tableWidget.insertRow(row_postition)
            self.ui_1.show()
        cur.close()
        con.close()


    def query(self):
        self.ui_2 = Query()
        self.ui_2.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "????????????"))
        self.commandLinkButton.setText(_translate("MainWindow", "????????????"))
        self.commandLinkButton_2.setText(_translate("MainWindow", "????????????"))
        self.commandLinkButton_3.setText(_translate("MainWindow", "????????????"))
        # self.commandLinkButton_4.setText(_translate("MainWindow", "??????????????????"))








