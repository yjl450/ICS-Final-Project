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
        chat.setWindowTitle(_translate("chat", "Dialog"))
        self.pushButton.setText(_translate("chat", "send"))
        self.pushButton_2.setText(_translate("chat", "clear"))
        self.textBrowser.setHtml(_translate("chat", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QDialog()
    ui = Ui_chat()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

