# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_chat(object):
    def setupUi(self, chat):
        chat.setObjectName("chat")
        chat.resize(541, 384)
        self.textEdit = QtWidgets.QTextEdit(chat)
        self.textEdit.setGeometry(QtCore.QRect(30, 250, 361, 111))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(chat)
        self.pushButton.setGeometry(QtCore.QRect(410, 280, 114, 32))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(chat)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 320, 114, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(chat)
        self.textBrowser.setGeometry(QtCore.QRect(30, 20, 361, 221))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(chat)
        self.textBrowser_2.setGeometry(QtCore.QRect(410, 20, 111, 241))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(chat)
        QtCore.QMetaObject.connectSlotsByName(chat)

    def retranslateUi(self, chat):
        _translate = QtCore.QCoreApplication.translate
        chat.setWindowTitle(_translate("chat", "Chat"))
        self.pushButton.setText(_translate("chat", "send"))
        self.pushButton_2.setText(_translate("chat", "clear"))
        self.textBrowser.setHtml("\n++++ Choose one of the following commands")
        self.textBrowser.append('time: calendar time in the system')
        self.textBrowser.append('who: to find out who else are there')
        self.textBrowser.append('c _peer_: to connect to the _peer_ and chat')
        self.textBrowser.append(' ? _term_: to search your chat logs where _term_ appears')
        self.textBrowser.append('p _#_: to get number <#> sonnet')
        self.textBrowser.append('q: to leave the chat system\n')

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QDialog()
    ui = Ui_chat()
    ui.setupUi(window)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

