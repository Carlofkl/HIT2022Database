# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from show import *
from change import *
from create import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QTableWidgetItem, QHeaderView
from PyQt5.QtGui import QIcon
import pymysql
import sys

class MAIN(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(MAIN,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 550)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 80, 500, 60))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(300, 180, 250, 60))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(18)
        self.commandLinkButton.setIcon(QIcon(""))
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(300, 280, 250, 60))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(18)
        self.commandLinkButton_2.setFont(font)
        self.commandLinkButton_2.setIcon(QIcon(""))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")

        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(300, 380, 350, 60))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(18)
        self.commandLinkButton_3.setFont(font)
        self.commandLinkButton_3.setIcon(QIcon(""))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")

        # self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(self.centralwidget)
        # self.commandLinkButton_4.setGeometry(QtCore.QRect(300, 390, 250, 48))
        # font = QtGui.QFont()
        # font.setFamily("Segoe UI")
        # self.commandLinkButton_4.setFont(font)
        # self.commandLinkButton_4.setObjectName("commandLinkButton_4")



        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 关系
        self.commandLinkButton.clicked.connect(self.query)
        self.commandLinkButton_2.clicked.connect(self.modify)
        self.commandLinkButton_3.clicked.connect(self.index)
        # self.commandLinkButton_4.clicked.connect(self.shiwuguanli)

    def query(self):
        self.ui_1 = Show()
        self.ui_1.show()

    def modify(self):
        self.ui_2 = Modify()
        self.ui_2.show()

    def index(self):
        self.ui_3 = Index()
        self.ui_3.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "教务处系统"))
        self.commandLinkButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.commandLinkButton.setText(_translate("MainWindow", "1.查询信息"))
        self.commandLinkButton_2.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.commandLinkButton_2.setText(_translate("MainWindow", "2.修改信息"))
        self.commandLinkButton_3.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.commandLinkButton_3.setText(_translate("MainWindow", "3.建立视图或索引"))
        # self.commandLinkButton_4.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        # self.commandLinkButton_4.setText(_translate("MainWindow", "事务管理"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">教务处管理系统</span></p></body></html>"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MAIN()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())