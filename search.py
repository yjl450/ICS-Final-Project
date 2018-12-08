# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import botton_click as click
import time

class Ui_SearchHistory(object):
    def __init__(self, user):
        self.user = user

    def setupUi(self, SearchHistory):
        SearchHistory.setObjectName("SearchHistory")
        SearchHistory.resize(382, 613)
        self.keyword = QtWidgets.QLineEdit(SearchHistory)
        self.keyword.setGeometry(QtCore.QRect(29, 80, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.keyword.setFont(font)
        self.keyword.setText("")
        self.keyword.setObjectName("keyword")
        self.search = QtWidgets.QPushButton(SearchHistory)
        self.search.setGeometry(QtCore.QRect(239, 80, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.search.setFont(font)
        self.search.setObjectName("search")
        self.search.clicked.connect(lambda: self.search_bnt_click())
        self.info = QtWidgets.QLabel(SearchHistory)
        self.info.setGeometry(QtCore.QRect(30, 20, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.info.setFont(font)
        self.info.setObjectName("info")
        self.result = QtWidgets.QTextBrowser(SearchHistory)
        self.result.setGeometry(QtCore.QRect(30, 140, 321, 441))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.result.setFont(font)
        self.result.setObjectName("result")

        self.retranslateUi(SearchHistory)
        QtCore.QMetaObject.connectSlotsByName(SearchHistory)

    def retranslateUi(self, SearchHistory):
        _translate = QtCore.QCoreApplication.translate
        SearchHistory.setWindowTitle(_translate("SearchHistory", "Form"))
        self.search.setText(_translate("SearchHistory", "Search"))
        self.info.setText(_translate("SearchHistory", "Input the keyword to search in history."))

    def search_bnt_click(self):
        self.result.clear()
        keyw = self.keyword.text()
        click.send_button(self.user, '$$$? ' + keyw)
        time.sleep(0.1)
        result = self.user.sm.search
        if result:
            self.result.append(result)
        else:
            reply = QMessageBox.question(None, 'Search', 'Cannot find anything in chat history.',
                                         QMessageBox.OK, QMessageBox.OK)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_SearchHistory()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()