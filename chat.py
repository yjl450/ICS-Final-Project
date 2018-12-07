# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import botton_click as click
import log_in as log
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

lang = {'Default(Eng)':'en', '简体中文':'zh', '繁體中文':'cht',\
            '日本語': 'jp', '한국어': 'kor' , 'Français': 'fra', 'Español': 'spa',\
            'لغة عربية': 'ara'}

class Ui_chat(object):
    def __init__(self, user):
        self.user = user
        self.thread = Rmessage(self.user)
        self.thread.start()
        self.thread.sinOut.connect(self.rec_msg)

    def setupUi(self, chat):
        chat.setObjectName("Chat") # whole window
        chat.resize(613, 590)
        self.chat = chat
        chat.setMinimumSize(QtCore.QSize(613, 590))
        chat.setMaximumSize(QtCore.QSize(613, 590))
        self.textEdit = QtWidgets.QTextEdit(chat) # Input Box
        self.textEdit.setGeometry(QtCore.QRect(40, 410, 361, 141))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(chat) # Send Button
        self.pushButton.setGeometry(QtCore.QRect(440, 410, 141, 141))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.send_bnt_click())
        self.search = QtWidgets.QPushButton(chat) # Clear Button
        self.search.setGeometry(QtCore.QRect(440, 208, 141, 46))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.search.setFont(font)
        self.search.setObjectName("search")
        self.textBrowser = QtWidgets.QTextBrowser(chat) # Message Display
        self.textBrowser.setGeometry(QtCore.QRect(40, 30, 361, 341))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowser.setObjectName("textBrowser")
        self.TransLan = QtWidgets.QComboBox(chat) # translation language
        self.TransLan.setGeometry(QtCore.QRect(440, 30, 141, 46))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.TransLan.setFont(font)
        self.TransLan.setObjectName("TransLan")
        self.translate = QtWidgets.QPushButton(chat) # translate button
        self.translate.setGeometry(QtCore.QRect(440, 90, 141, 46))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.translate.setFont(font)
        self.translate.setObjectName("translate")
        self.translate.clicked.connect(lambda: self.LangTrans())
        self.connect = QtWidgets.QPushButton(chat) # connet button
        self.connect.setGeometry(QtCore.QRect(440, 149, 141, 46))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.connect.setFont(font)
        self.connect.setObjectName("connect")
        self.time = QtWidgets.QPushButton(chat)
        self.time.setGeometry(QtCore.QRect(440, 268, 141, 46))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.time.setFont(font)
        self.time.setObjectName("time")
        self.clear = QtWidgets.QPushButton(chat)
        self.clear.setGeometry(QtCore.QRect(440, 325, 141, 46))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.clear.clicked.connect(lambda: self.clear_screen())
        self.retranslateUi(chat)
        QtCore.QMetaObject.connectSlotsByName(chat)

    def retranslateUi(self, chat):
        _translate = QtCore.QCoreApplication.translate
        chat.setWindowTitle(_translate("chat", "Chat"))
        self.pushButton.setText(_translate("chat", "Send"))
        self.clear.setText(_translate("chat", "Clear"))
        self.search.setText(_translate("chat", "Search"))
        self.time.setText(_translate("chat", "Time"))
        self.translate.setText(_translate("chat", "Translate"))
        self.connect.setText(_translate("chat", "Connect"))
        for i in lang:
            self.TransLan.addItem(i)
        self.textBrowser.setHtml("\n++ Click \"Connect\" to chat with a friend.")
        self.textBrowser.append('++ Click \"Time\" to see current time.')
        self.textBrowser.append('++ Click \"Search\" to search chat history.')

    def send_bnt_click(self):
        text = self.textEdit.toPlainText()
        self.textEdit.clear()
        self.textBrowser.append('[me]'+text)
        self.textBrowser.append('')
        if text == 'q' and self.user.sm.state == 2:
            self.chat.close()
            return

        #message =
        click.send_button(self.user, text)

        #if message!= '':
            #self.textBrowser.append(message)

        #message =
        click.send_button(self.user, text)

        #if message!= '':
            #self.textBrowser.append(message)

    def rec_msg(self, msg):
        if msg != '':
            self.textBrowser.append(msg)
            self.textBrowser.append('  ')

    def clear_screen(self):
        self.textBrowser.clear()

    def LangTrans(self):
        toLang = self.TransLan.currentText()
        langIdx = lang[toLang]
        print(langIdx)
        self.user.sm.set_language(langIdx)3


class Chat(QtWidgets.QDialog):
    def __init__(self,user):
        super(Chat, self).__init__()
        self.user = user

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'You sure to quit?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
                self.user.sm.state = 2
                event.accept()
                self.user.console_input.append('q')
        else:
                event.ignore()


class Rmessage(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self, user, parent=None):
        super(Rmessage, self).__init__(parent)
        self.working = True
        self.user = user

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        while self.working == True:
            try:
                self.user.proc()
                message = self.user.output()
                self.sinOut.emit(message)
            except:
                pass
# ------ test code ------
# this part will not be called and is rewritten in log_in.py

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QDialog()
    ui = Ui_chat()
    # technically we need to put a parameter as user here. we do that in the login in
    ui.setupUi(window)
    window.show()
    app.exec_()





if __name__ == '__main__':
    main()

# ----- test code end ------
