# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainframe_mr.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MassRequests(object):
    def setupUi(self, MassRequests):
        MassRequests.setObjectName("MassRequests")
        MassRequests.setEnabled(True)
        MassRequests.resize(764, 411)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MassRequests.sizePolicy().hasHeightForWidth())
        MassRequests.setSizePolicy(sizePolicy)
        MassRequests.setMinimumSize(QtCore.QSize(764, 411))
        MassRequests.setMaximumSize(QtCore.QSize(764, 411))
        MassRequests.setStyleSheet("background-color: rgb(213, 213, 213);")
        MassRequests.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MassRequests)
        self.centralwidget.setObjectName("centralwidget")
        self.label_path_to_xl = QtWidgets.QLabel(self.centralwidget)
        self.label_path_to_xl.setGeometry(QtCore.QRect(50, 140, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_path_to_xl.setFont(font)
        self.label_path_to_xl.setObjectName("label_path_to_xl")
        self.text_path_to_fit = QtWidgets.QTextEdit(self.centralwidget)
        self.text_path_to_fit.setGeometry(QtCore.QRect(30, 180, 591, 31))
        self.text_path_to_fit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.text_path_to_fit.setObjectName("text_path_to_fit")
        self.btn_find_xl = QtWidgets.QPushButton(self.centralwidget)
        self.btn_find_xl.setGeometry(QtCore.QRect(660, 180, 75, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_find_xl.setFont(font)
        self.btn_find_xl.setStyleSheet("background-color: rgba(0, 149, 255, 253);")
        self.btn_find_xl.setObjectName("btn_find_xl")
        self.btn_go = QtWidgets.QPushButton(self.centralwidget)
        self.btn_go.setGeometry(QtCore.QRect(340, 330, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_go.setFont(font)
        self.btn_go.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.btn_go.setObjectName("btn_go")
        MassRequests.setCentralWidget(self.centralwidget)

        self.retranslateUi(MassRequests)
        QtCore.QMetaObject.connectSlotsByName(MassRequests)

    def retranslateUi(self, MassRequests):
        _translate = QtCore.QCoreApplication.translate
        MassRequests.setWindowTitle(_translate("MassRequests", "Создание массовых заявкок в СУИД"))
        self.label_path_to_xl.setText(_translate("MassRequests", "Укажите путь к файлу"))
        self.btn_find_xl.setText(_translate("MassRequests", "Загрузить"))
        self.btn_go.setText(_translate("MassRequests", "GO"))
