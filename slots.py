"""
USERS SLOTS FOR WIDGETS
"""

from datetime import datetime

from form import Ui_Form


class MainWindowSlots(Ui_Form):
    def set_time(self):
        str_time = datetime.now().strftime('%H:%M:%S')
        self.timeButton.setText(str_time)
        return None

    def set_time_lbl(self):
        str_time = datetime.now().strftime('%H:%M:%S')
        self.threedLabel.setText(str_time)
        return None

