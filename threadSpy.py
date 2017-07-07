# -*- coding: utf-8 -*-
from datetime  import datetime
from PyQt5 import QtCore


class MyThread(QtCore.QThread):

    mysinal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            self.sleep(1)
            self.mysinal.emit("i= %s" % self.set_time())

    def set_time(self):
        return datetime.now().strftime('%H:%M:%S')
