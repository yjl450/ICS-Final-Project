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
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QCoreApplication
import chat
import chat_face_recog

class Ui_log_in(object):
    def setupUi(self, log_in):
        log_in.setObjectName("log_in")
        log_in.resize(547, 309)
        self.login = log_in
        self.centralwidget = QtWidgets.QWidget(log_in)
        self.centralwidget.setObjectName("centralwidget")
        self.newUserName = QtWidgets.QLineEdit(self.centralwidget)
        self.newUserName.setGeometry(QtCore.QRect(200, 140, 131, 21))
        self.newUserName.setObjectName("newUserName")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 30, 341, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 60, 211, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 140, 71, 20))
        self.label_3.setObjectName("label_3")
        self.log_bnt = QtWidgets.QPushButton(self.centralwidget)
        self.log_bnt.setGeometry(QtCore.QRect(210, 80, 114, 32))
        self.log_bnt.setObjectName("log_bnt")
        # 现在暂时把log in 这个button和输入user name 联系起来了 请之后自行修改
        self.log_bnt.clicked.connect(self.log_bnt_click)
        self.reg_bnt = QtWidgets.QPushButton(self.centralwidget)
        self.reg_bnt.setGeometry(QtCore.QRect(190, 170, 151, 31))
        self.reg_bnt.setObjectName("reg_bnt")
        self.reg_bnt.clicked.connect(self.reg_bnt_click)
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
        log_in.setWindowTitle(_translate("self", "Login"))
        self.label.setText(_translate("log_in", "Welcome to final chat system!"))
        self.label_2.setText(_translate("log_in", "Click login with your name!"))
        self.label_3.setText(_translate("log_in", "user name"))
        self.log_bnt.setText(_translate("log_in", "log in"))
        self.reg_bnt.setText(_translate("log_in", "register your face"))
        self.label_5.setText(_translate("log_in", "wanna secure your account?"))

    # def jump_to_chat(self):
    #     self.login.hide()
    #     form2 = QtWidgets.QDialog()
    #     ui = chat.Ui_chat()
    #     ui.setupUi(form2)
    #     form2.show()
    #     form2.exec_()
    #     self.login.show()

    def log_bnt_click(self):
        user_name = chat_face_recog.face_recog()
        if user_name != '$$$Unknown$$$' and user_name != '$$$Timeout$$$':
            a = click.log_in_botton(user_name, self.label_2)
            if a:
                reply = QMessageBox.question(None, 'welcome!',
                                             "log in successfully",
                                             QMessageBox.Ok, QMessageBox.Ok)
                if reply == QMessageBox.Ok:
                    self.login.close()
                    form2 = QtWidgets.QDialog()
                    ui = chat.Ui_chat(user)
                    ui.setupUi(form2)
                    form2.show()
                    form2.exec_()
        elif user_name != '$$$Unknown$$$':
            reply = QMessageBox.question(None, 'Unknown Face','Please register your face before login!',
                                         QMessageBox.Ok, QMessageBox.Ok)
        else:
            reply = QMessageBox.question(None, 'Timeout','Failed to detect face!',
                                         QMessageBox.Ok, QMessageBox.Ok)

    def reg_bnt_click(self):
        path, type = QFileDialog.getOpenFileName(None,
                                                 "Register your photo",
                                                 "",
                                                 "All Files (*);;Image File (*.jpg)")
        name = self.newUserName.text()
        reg_result = chat_face_recog.reg(path, name)
        if reg_result == True:
            reply = QMessageBox.question(None, 'Success', 'User' + name + ' is successfully registered!\n You can login now!',
                                         QMessageBox.Ok, QMessageBox.Ok)
        elif reg_result == 'User already exists':
            reply = QMessageBox.question(None, 'Existing User', 'User ' + name + ' already exists!',
                                         QMessageBox.Ok, QMessageBox.Ok)
        elif reg_result == 'No face Detected':
            reply = QMessageBox.question(None, 'Invalid Photo', 'No face detected in the photo!\nPlease select another photo!',
                                         QMessageBox.Ok, QMessageBox.Ok)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_log_in()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()