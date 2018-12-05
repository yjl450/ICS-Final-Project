# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log_in.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5.QtWidgets import QMessageBox,QApplication

import chat_client_class as cmclass
import botton_click as click
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
import chat

class Ui_log_in(object):
    def setupUi(self, log_in):
        log_in.setObjectName("log_in")
        log_in.resize(547, 309)
        self.login = log_in
        self.centralwidget = QtWidgets.QWidget(log_in)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 140, 131, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 30, 341, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 60, 211, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 140, 71, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 80, 114, 32))
        self.pushButton.setObjectName("pushButton")
        # 现在暂时把log in 这个button和输入user name 联系起来了 请之后自行修改
        self.pushButton.clicked.connect(self.log_bnt_click)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 170, 151, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 140, 151, 16))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 110, 221, 31))
        self.label_5.setObjectName("label_5")
        log_in.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(log_in)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 547, 22))
        self.menubar.setObjectName("menubar")
        log_in.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(log_in)
        self.statusbar.setObjectName("statusbar")
        log_in.setStatusBar(self.statusbar)

        self.retranslateUi(log_in)
        QtCore.QMetaObject.connectSlotsByName(log_in)

    def retranslateUi(self, log_in):
        _translate = QtCore.QCoreApplication.translate
        log_in.setWindowTitle(_translate("log_in", "Log in"))
        self.label.setText(_translate("log_in", "Welcome to final chat system!"))
        self.label_2.setText(_translate("log_in", "Click login with your name!"))
        self.label_3.setText(_translate("log_in", "user name"))
        self.pushButton.setText(_translate("log_in", "log in"))
        self.pushButton_2.setText(_translate("log_in", "register your face"))
        self.label_5.setText(_translate("log_in", "wanna secure your account?"))

    def jump_to_chat(self):
        self.login.close()
        form2 = QtWidgets.QDialog()
        ui = chat.Ui_chat()
        ui.setupUi(form2)
        form2.show()
        form2.exec_()
        #self.login.show()

    def log_bnt_click(self):
        user_name = self.lineEdit.text()
        a = click.log_in_botton(user_name,self.label_2)
        if a:
            reply = QMessageBox.question(None,'welcome!',
                                         "log in successfully",
                                         QMessageBox.Ok,QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                self.jump_to_chat()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_log_in()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()