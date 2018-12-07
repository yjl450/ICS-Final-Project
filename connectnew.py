# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\github\ICS-Final-Project\connect.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
import sys

lang = {'Default(Eng)':'en', '简体中文':'zh', '繁體中文':'cht',\
            '日本語': 'jp', '한국어': 'kor' , 'Français': 'fra', 'Español': 'spa',\
            'لغة عربية': 'ara'}

class Ui_Connect(object):
    def setupUi(self, Connect):
        Connect.setObjectName("Connect")
        Connect.resize(211, 237)
        Connect.setMinimumSize(QtCore.QSize(211, 237))
        Connect.setMaximumSize(QtCore.QSize(211, 237))
        self.cancel = QtWidgets.QPushButton(Connect)
        self.cancel.setGeometry(QtCore.QRect(60, 192, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.con = QtWidgets.QPushButton(Connect)
        self.con.setGeometry(QtCore.QRect(60, 150, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.con.setFont(font)
        self.con.setObjectName("con")
        self.Peer = QtWidgets.QScrollArea(Connect)
        self.Peer.setGeometry(QtCore.QRect(20, 21, 171, 111))
        self.Peer.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.Peer.setWidgetResizable(False)
        self.Peer.setObjectName("Peer")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 169, 109))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        for i in lang:
            self.radioButton = QtWidgets.QRadioButton(Connect)
            font = QtGui.QFont()
            font.setFamily("Calibri")
            font.setPointSize(12)
            self.radioButton.setFont(font)
            self.radioButton.setObjectName(i)
            self.radioButton.setText(_translate("Connect", i))
            self.Peer.addScrollBarWidget()
        self.Peer.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Connect)
        QtCore.QMetaObject.connectSlotsByName(Connect)

    def retranslateUi(self, Connect):
        _translate = QtCore.QCoreApplication.translate
        Connect.setWindowTitle(_translate("self", "Peers"))

        self.cancel.setText(_translate("Connect", "Cancel"))
        self.con.setText(_translate("Connect", "Connect"))
        self.radioButton.setText(_translate("Connect", "RadioButton"))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_Connect()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()