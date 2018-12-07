# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\github\ICS-Final-Project\connect.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Connect(object):
    def setupUi(self, Connect):
        Connect.setObjectName("Connect")
        Connect.resize(211, 237)
        Connect.setMinimumSize(QtCore.QSize(211, 237))
        Connect.setMaximumSize(QtCore.QSize(211, 237))
        self.peer = QtWidgets.QListWidget(Connect)
        self.peer.setGeometry(QtCore.QRect(20, 21, 171, 111))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.peer.setFont(font)
        self.peer.setObjectName("peer")
        item = QtWidgets.QListWidgetItem()
        self.peer.addItem(item)
        self.pushButton = QtWidgets.QPushButton(Connect)
        self.pushButton.setGeometry(QtCore.QRect(60, 192, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Connect)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 150, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.radioButton = QtWidgets.QRadioButton(Connect)
        self.radioButton.setGeometry(QtCore.QRect(0, 140, 89, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")

        self.retranslateUi(Connect)
        QtCore.QMetaObject.connectSlotsByName(Connect)

    def retranslateUi(self, Connect):
        _translate = QtCore.QCoreApplication.translate
        Connect.setWindowTitle(_translate("Connect", "Dialog"))
        __sortingEnabled = self.peer.isSortingEnabled()
        self.peer.setSortingEnabled(False)
        # item = self.peer.item(0)
        # item.setText(_translate("Connect", "qof"))
        for i in user_list:
            self.radioButton = QtWidgets.QRadioButton(Connect)
            font = QtGui.QFont()
            font.setFamily("Calibri")
            font.setPointSize(12)
            self.radioButton.setFont(font)
            self.radioButton.setObjectName(i)
            self.peer.addItem(self.radioButton)
        self.peer.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Connect", "Cancel"))
        self.pushButton_2.setText(_translate("Connect", "Connect"))
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