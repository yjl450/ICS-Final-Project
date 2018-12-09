# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Ui_Connect(object):
    def __init__(self, list,user):
        self.list = list
        self.radio = {}
        self.user = user

    def setupUi(self, Connect):
        self.connect = Connect
        Connect.setObjectName("Connect")
        Connect.resize(230, 250)
        Connect.setMinimumSize(QtCore.QSize(230, 250))
        Connect.setMaximumSize(QtCore.QSize(230, 250))
        self.confirm = QtWidgets.QDialogButtonBox(Connect)
        self.confirm.setGeometry(QtCore.QRect(19, 195, 193, 28))
        self.confirm.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.confirm.setObjectName("confirm")
        self.confirm.accepted.connect(self.ok_button_click)
        self.confirm.rejected.connect(self.cancel_button_click)
        self.widget = QtWidgets.QWidget(Connect)
        self.widget.setGeometry(QtCore.QRect(38, 20, 154, 151))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.info = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.info.setFont(font)
        self.info.setAlignment(QtCore.Qt.AlignCenter)
        self.info.setObjectName("info")
        self.verticalLayout_2.addWidget(self.info)
        spacerItem = QtWidgets.QSpacerItem(40, 6, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.Peer = QtWidgets.QScrollArea(self.widget)
        self.Peer.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.Peer.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.Peer.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Peer.setWidgetResizable(True)
        self.Peer.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.Peer.setObjectName("Peer")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 157, 108))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")


        for i in self.list:
            self.add_radio(i)

        self.horizontalLayout.addLayout(self.verticalLayout)
        self.Peer.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.Peer)

        self.retranslateUi(Connect)
        QtCore.QMetaObject.connectSlotsByName(Connect)

    def retranslateUi(self, Connect):
        _translate = QtCore.QCoreApplication.translate
        Connect.setWindowTitle(_translate("Connect", "Connect"))
        self.info.setText(_translate("Connect", "Select a peer!"))
        for radio in self.radio.keys():
            radio.setText(_translate("Connect", self.radio[radio]))
        # self.radioButton_2.setText(_translate("Connect", "Amanda"))
        # self.radioButton_3.setText(_translate("Connect", "Coconut"))
        # self.radioButton_4.setText(_translate("Connect", "Pineapple"))

    def add_radio(self, i):
        radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        radio.setFont(font)
        radio.setObjectName(i)
        self.verticalLayout.addWidget(radio)
        self.radio[radio] = i

    def click_connect(self):
        self.show()

    def ok_button_click(self):
        button = ''
        for i in self.radio.keys():
            if i.isChecked:
                button = i
                break
        if button  == '':
            QMessageBox.question(None, 'Message', 'Please select a peer!',
                                QMessageBox.Ok | QMessageBox.Ok)
        else:
            peer = self.radio[button]
            text = '$$$c'+str(peer)
            self.user.console_input.append(text)
            self.connect.close()




    def cancel_button_click(self):
        self.connect.close()




def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_Connect({'a','b','c'})
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()