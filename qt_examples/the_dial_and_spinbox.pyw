__author__ = 'gjoshi'

import sys
from PyQt4.QtGui import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        dial = QDial()
        dial.setNotchesVisible(True)
        spinbox = QSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        self.setLayout(layout)

        dial.valueChanged.connect(spinbox.setValue)
        spinbox.valueChanged.connect(dial.setValue)

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
