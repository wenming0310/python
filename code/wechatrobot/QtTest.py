# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtTest.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import wechatrobot
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(348, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_open = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open.setGeometry(QtCore.QRect(70, 210, 75, 23))
        self.pushButton_open.setObjectName("pushButton_open")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 101, 16))
        self.label.setObjectName("label")
        self.label_key = QtWidgets.QLabel(self.centralwidget)
        self.label_key.setGeometry(QtCore.QRect(20, 60, 54, 12))
        self.label_key.setObjectName("label_key")
        self.lineEdit_key = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_key.setGeometry(QtCore.QRect(70, 60, 241, 20))
        self.lineEdit_key.setObjectName("lineEdit_key")
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(200, 210, 75, 23))
        self.pushButton_close.setObjectName("pushButton_close")
        self.label_addr = QtWidgets.QLabel(self.centralwidget)
        self.label_addr.setGeometry(QtCore.QRect(20, 100, 54, 12))
        self.label_addr.setObjectName("label_addr")
        self.lineEdit_addr = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_addr.setGeometry(QtCore.QRect(70, 100, 241, 20))
        self.lineEdit_addr.setObjectName("lineEdit_addr")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(20, 140, 54, 12))
        self.label_name.setObjectName("label_name")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(70, 140, 241, 20))
        self.lineEdit_name.setObjectName("lineEdit_name")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 348, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        #self.pushButton_open.clicked.connect(self.pushButton_open.click)
        self.pushButton_open.clicked.connect(wechatrobot.startrobot)
        #self.pushButton_close.clicked.connect(MainWindow.close)
        self.pushButton_close.clicked.connect(wechatrobot.closerobot)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_open.setText(_translate("MainWindow", "打开Robot"))
        self.label.setText(_translate("MainWindow", "哇塞！竟然可以用"))
        self.label_key.setText(_translate("MainWindow", "Key"))
        self.lineEdit_key.setText(_translate("MainWindow", "b7ac5505add541918f2796561fa874f5"))
        self.pushButton_close.setText(_translate("MainWindow", "关闭Robot"))
        self.label_addr.setText(_translate("MainWindow", "地址"))
        self.lineEdit_addr.setText(_translate("MainWindow", "http://www.tuling123.com/openapi/api"))
        self.label_name.setText(_translate("MainWindow", "Name"))
        self.lineEdit_name.setText(_translate("MainWindow", "ABC"))

