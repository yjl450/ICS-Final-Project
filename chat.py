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
        chat.resize(566, 467)
        self.chat = chat
        chat.setMinimumSize(QtCore.QSize(566, 467))
        chat.setMaximumSize(QtCore.QSize(566, 467))
        self.textEdit = QtWidgets.QTextEdit(chat) # Input Box
        self.textEdit.setGeometry(QtCore.QRect(30, 330, 361, 111))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(chat) # Send Button
        self.pushButton.setGeometry(QtCore.QRect(420, 330, 120, 111))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.send_bnt_click())
        self.clear = QtWidgets.QPushButton(chat) # Clear Button
        self.clear.setGeometry(QtCore.QRect(420, 240, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.clear.clicked.connect(lambda: self.clear_screen())
        self.textBrowser = QtWidgets.QTextBrowser(chat) # Message Display
        self.textBrowser.setGeometry(QtCore.QRect(30, 30, 361, 271))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowser.setObjectName("textBrowser")
        self.TransLan = QtWidgets.QComboBox(chat) # translation language
        self.TransLan.setGeometry(QtCore.QRect(420, 30, 120, 32))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.TransLan.setFont(font)
        self.TransLan.setObjectName("TransLan")
        self.TransLan.addItem("Default(Eng)")
        self.translate = QtWidgets.QPushButton(chat) # translate button
        self.translate.setGeometry(QtCore.QRect(420, 80, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.translate.setFont(font)
        self.translate.setObjectName("translate")
        self.connect = QtWidgets.QPushButton(chat) # connet button
        self.connect.setGeometry(QtCore.QRect(420, 160, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.connect.setFont(font)
        self.connect.setObjectName("connect")
        self.retranslateUi(chat)
        QtCore.QMetaObject.connectSlotsByName(chat)

    def retranslateUi(self, chat):
        _translate = QtCore.QCoreApplication.translate
        chat.setWindowTitle(_translate("chat", "Chat"))
        self.pushButton.setText(_translate("chat", "Send"))
        self.clear.setText(_translate("chat", "Clear"))
        self.translate.setText(_translate("chat", "Translate"))
        self.connect.setText(_translate("chat", "Connect"))
        for i in lang:
            self.TransLan.addItem(i)
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
        if text == 'q' and self.user.state == 2:
            reply = QMessageBox.question(None, 'Bye',
                                         'See you next time!',
                                         QMessageBox.Ok, QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                self.chat.close()
                return

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

    # def closeEvent(self, event):
    #     """Generate 'question' dialog on clicking 'X' button in title bar.
    #
    #     Reimplement the closeEvent() event handler to include a 'Question'
    #     dialog with options on how to proceed - Save, Close, Cancel buttons
    #     """
    #     reply = QMessageBox.question(
    #         self, "Message",
    #         "Are you sure you want to quit? Any unsaved work will be lost.",
    #         QMessageBox.Save | QMessageBox.Close | QMessageBox.Cancel,
    #         QMessageBox.Save)
    #
    #     if reply == QMessageBox.Close:
    #         event.accept()
    #     else:
    #         event.ignore()
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
