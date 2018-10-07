# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstMainWin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(726, 592)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 110, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.CB01 = QtWidgets.QCheckBox(self.centralwidget)
        self.CB01.setGeometry(QtCore.QRect(160, 130, 71, 16))
        self.CB01.setObjectName("CB01")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 260, 54, 12))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 240, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.CB02 = QtWidgets.QCheckBox(self.centralwidget)
        self.CB02.setGeometry(QtCore.QRect(310, 70, 71, 16))
        self.CB02.setObjectName("CB02")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 726, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "按钮"))
        self.CB01.setText(_translate("MainWindow", "CheckBox"))
        self.label.setText(_translate("MainWindow", "显示"))
        self.lineEdit.setText(_translate("MainWindow", "ABC"))
        self.CB02.setText(_translate("MainWindow", "CheckBox"))

