# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_course.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Modify_course(QtWidgets.QMainWindow):

    def __init__(self):
        super(Modify_course, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 480, 90, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 480, 90, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(230, 100, 340, 280))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.verticalLayout.addWidget(self.line)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)

        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)

        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.insert_course)
        self.pushButton_2.clicked.connect(self.delete_course)




    def insert_course(self):
        cid, cname, tid = self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text()
        if not cid or not cname or not tid:
            QMessageBox.warning(self, '警告', '请输入课程号、课程名和任课教师号')
        elif len(cid) != 3 or len(tid) != 3:
            QMessageBox.warning(self, '警告', '课程号为3位数字，教师号为3位数字')
        else:
            con = pymysql.connect(host='localhost', port=3306, user='root', password='fkl001206', charset='utf8',
                                  database='lab1')  # 连接数据库
            cur = con.cursor()  # 执行sql语句的游标
            query = 'select * from course where cid=%s'
            if cur.execute(query, [cid]):
                QMessageBox.warning(self, '插入异常', '该课程号已存在，请重新输入')
            elif not cur.execute('select * from teacher where tid = %s', [tid]):
                QMessageBox.warning(self, '插入异常', '该教师号在教师表中不存在，请尝试插入对应条目')
            else:
                QMessageBox.information(self, '成功', '成功插入一条课程数据')
                query = 'insert into course(cid,cname,tid) values (%s,%s,%s)'
                cur.execute(query, [cid, cname, tid])
                con.commit()

    def delete_course(self):  # 删除学生信息
        cid = self.lineEdit.text()
        if not cid:
            QMessageBox.warning(self, '警告', '课程号为空')
        elif len(cid) != 3:
            QMessageBox.warning(self, '警告', '课程号只可为3位数字')
        else:
            con = pymysql.connect(host='localhost', port=3306, user='root', password='fkl001206', charset='utf8',
                                  database='lab1')  # 连接数据库
            cur = con.cursor()  # 执行sql语句的游标
            query = 'select * from course where cid=%s'
            if not cur.execute(query, [cid]):
                QMessageBox.warning(self, "删除异常", "该课程号不存在，请重新输入")
            else:
                if cur.execute('select * from grade where cid=%s', [cid]):
                    QMessageBox.information(self, '提示', '该课程号正被选课表作为外键引用，触发器已默认删除对应条目数据')
                    query = 'delete from grade where cid=%s'
                    cur.execute(query, [cid])
                QMessageBox.information(self, '成功', '成功删除一条课程数据')
                query = 'delete from course where cid=%s'
                cur.execute(query, [cid])
                con.commit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "插入"))
        self.pushButton_2.setText(_translate("MainWindow", "删除"))
        self.label.setText(_translate("MainWindow", "课程号"))
        self.label_2.setText(_translate("MainWindow", "课程名"))
        self.label_3.setText(_translate("MainWindow", "教师教工号"))
