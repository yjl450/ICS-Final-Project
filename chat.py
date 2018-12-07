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

class Ui_chat(object):
    def __init__(self,user):
        self.user = user
        self.thread = Rmessage(self.user)
        self.thread.start()
        self.thread.sinOut.connect(self.rec_msg)

    def setupUi(self, chat):
        chat.setObjectName("chat")
        chat.resize(541, 384)
        self.chat = chat
        self.textEdit = QtWidgets.QTextEdit(chat)
        self.textEdit.setGeometry(QtCore.QRect(30, 250, 361, 111))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(chat)
        self.pushButton.setGeometry(QtCore.QRect(410, 280, 114, 32))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:self.send_bnt_click())
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

    def send_bnt_click(self):
        text = self.textEdit.toPlainText()
        self.textEdit.clear()
        self.textBrowser.append('[me]'+text)
        self.textBrowser.append('')
        if text == 'q' and self.user.sm.state == 2:
            reply = QMessageBox.question(None, 'Bye',
                                         'See you next time!',
                                         QMessageBox.Ok, QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                self.chat.close()
                self.chat.quit()
                self.user.console_input.append(text)

                return

        #message =
        click.send_button(self.user, text)

        #if message!= '':
            #self.textBrowser.append(message)

    def rec_msg(self,msg):
        if msg!= '':
            self.textBrowser.append(msg)
            self.textBrowser.append('  ')


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

#----- test code end ------
