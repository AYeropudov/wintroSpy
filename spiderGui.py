#!/usr/bin/python3.5
# -*- coding utf-8 -*-
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('WintroPy GUI')
window.resize(300, 300)
label = QtWidgets.QLabel("Web spy")
btnQuite = QtWidgets.QPushButton("&Закрыть окно")
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(btnQuite)
window.setLayout(vbox)
btnQuite.clicked.connect(app.quit)
window.show()
sys.exit(app.exec_())
