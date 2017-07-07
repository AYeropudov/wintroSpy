#!/usr/bin/python3.5
# -*- coding utf-8 -*-
from PyQt5 import QtCore

from PyQt5.QtWidgets import QWidget, QApplication
from slots import MainWindowSlots
from threadSpy import MyThread
import sys


class SpyderWintro(MainWindowSlots):
    
    def __init__(self, form):
        self.setupUi(form)
        self.my_thread = MyThread()
        self.connect_slots()

    def connect_slots(self):
        self.timeButton.clicked.connect(self.set_time)
        self.threedBtn.clicked.connect(self.start_th)
        self.stopTransaction.clicked.connect(self.stop_th)
        self.my_thread.started.connect(self.on_started)
        self.my_thread.finished.connect(self.on_finished)
        self.my_thread.mysinal.connect(self.on_change, QtCore.Qt.QueuedConnection)
        return None

    def stop_th(self):
        self.my_thread.running = False
        self.threedLabel.setText("Aborted by user")

    def start_th(self):
        self.my_thread.start()
        self.threedBtn.setDisabled(True)

    def on_started(self):
        self.threedLabel.setText("Started thead")

    def on_finished(self):
        self.threedBtn.setDisabled(False)

    def on_change(self, s):
        self.threedLabel.setText(s)

    def closeEvent(self, event):
        self.hide()
        self.my_thread.running= False
        self.my_thread.wait(5000)
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    ui = SpyderWintro(window)
    window.show()
    sys.exit(app.exec_())
