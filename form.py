# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 640)
        self.timeButton = QtWidgets.QPushButton(Form)
        self.timeButton.setGeometry(QtCore.QRect(10, 40, 80, 25))
        self.timeButton.setObjectName("timeButton")
        self.threedBtn = QtWidgets.QPushButton(Form)
        self.threedBtn.setGeometry(QtCore.QRect(10, 90, 85, 27))
        self.threedBtn.setObjectName("threedBtn")
        self.threedLabel = QtWidgets.QLabel(Form)
        self.threedLabel.setGeometry(QtCore.QRect(180, 40, 131, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threedLabel.sizePolicy().hasHeightForWidth())
        self.threedLabel.setSizePolicy(sizePolicy)
        self.threedLabel.setObjectName("threedLabel")
        self.stopTransaction = QtWidgets.QPushButton(Form)
        self.stopTransaction.setGeometry(QtCore.QRect(354, 550, 111, 27))
        self.stopTransaction.setObjectName("stopTransaction")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.timeButton.setText(_translate("Form", "PushButton"))
        self.threedBtn.setText(_translate("Form", "PushButton"))
        self.threedLabel.setText(_translate("Form", "TextLabel"))
        self.stopTransaction.setText(_translate("Form", "Stop Transaction"))

