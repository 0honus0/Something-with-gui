# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\39772\Desktop\ui2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(614, 688)
        Dialog.setMinimumSize(QtCore.QSize(614, 688))
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(150, 150, 72, 41))
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(150, 280, 171, 41))
        self.label_11.setObjectName("label_11")
        self.cuoshi = QtWidgets.QTextBrowser(Dialog)
        self.cuoshi.setGeometry(QtCore.QRect(150, 360, 311, 171))
        self.cuoshi.setObjectName("cuoshi")
        self.ensure_button_3 = QtWidgets.QPushButton(Dialog)
        self.ensure_button_3.setGeometry(QtCore.QRect(370, 200, 93, 28))
        self.ensure_button_3.setObjectName("ensure_button_3")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(250, 240, 221, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(150, 330, 131, 31))
        self.label_13.setObjectName("label_13")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(150, 240, 72, 31))
        self.label_12.setObjectName("label_12")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(150, 200, 161, 31))
        self.label_10.setObjectName("label_10")
        self.result = QtWidgets.QTextBrowser(Dialog)
        self.result.setGeometry(QtCore.QRect(290, 160, 171, 31))
        self.result.setObjectName("result")
        self.result_2 = QtWidgets.QTextBrowser(Dialog)
        self.result_2.setGeometry(QtCore.QRect(370, 290, 91, 31))
        self.result_2.setObjectName("result_2")
        self.filename = QtWidgets.QTextBrowser(Dialog)
        self.filename.setGeometry(QtCore.QRect(300, 50, 161, 41))
        self.filename.setObjectName("filename")
        self.file_button = QtWidgets.QPushButton(Dialog)
        self.file_button.setGeometry(QtCore.QRect(150, 50, 141, 41))
        self.file_button.setObjectName("file_button")
        self.file_cancel_buttom = QtWidgets.QPushButton(Dialog)
        self.file_cancel_buttom.setGeometry(QtCore.QRect(330, 110, 93, 28))
        self.file_cancel_buttom.setObjectName("file_cancel_buttom")
        self.file_ensure_buttom = QtWidgets.QPushButton(Dialog)
        self.file_ensure_buttom.setGeometry(QtCore.QRect(180, 110, 93, 28))
        self.file_ensure_buttom.setObjectName("file_ensure_buttom")
        self.result_button = QtWidgets.QPushButton(Dialog)
        self.result_button.setGeometry(QtCore.QRect(370, 550, 93, 28))
        self.result_button.setObjectName("result_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_9.setText(_translate("Dialog", "????????????:"))
        self.label_11.setText(_translate("Dialog", "??????????????????????????????:"))
        self.ensure_button_3.setText(_translate("Dialog", "???"))
        self.label_13.setText(_translate("Dialog", "?????????????????????:"))
        self.label_12.setText(_translate("Dialog", "??????:"))
        self.label_10.setText(_translate("Dialog", "??????????????????????????????:"))
        self.file_button.setText(_translate("Dialog", "????????????????????????"))
        self.file_cancel_buttom.setText(_translate("Dialog", "??????"))
        self.file_ensure_buttom.setText(_translate("Dialog", "??????"))
        self.result_button.setText(_translate("Dialog", "????????????"))
