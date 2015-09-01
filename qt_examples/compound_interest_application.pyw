__author__ = 'gjoshi'

import sys
import itertools
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.principal_label = QLabel("Principal: ")
        self.rate_label = QLabel("Rate: ")
        self.years_label = QLabel("Years: ")
        self.amount_label = QLabel("Amount: ")
        self.amount_val_label = QLabel("$ 2215.51")
        self.principal_box = QDoubleSpinBox()
        self.rate_box = QDoubleSpinBox()
        self.years_box = QComboBox()
        self.years_box.addItems(["{0} years".format(i) for i in range(1, 10)])

        self.principal_box.setRange(0.01, 10000000.00)
        self.principal_box.setValue(2000.0)
        self.principal_box.setPrefix("$ ")
        self.rate_box.setValue(5.25)
        self.rate_box.setSuffix(" %")
        self.years_box.setCurrentIndex(1)

        layout = QGridLayout()

        layout.addWidget(self.principal_label, 0, 0)
        layout.addWidget(self.principal_box, 0, 1)
        layout.addWidget(self.rate_label, 1, 0)
        layout.addWidget(self.rate_box, 1, 1)
        layout.addWidget(self.years_label, 2, 0)
        layout.addWidget(self.years_box, 2, 1)
        layout.addWidget(self.amount_label, 3, 0)
        layout.addWidget(self.amount_val_label, 3, 1)

        self.setLayout(layout)
        self.setWindowTitle("Interest")
        self.years_box.setFocus()

        self.principal_box.valueChanged.connect(self.update_ui)
        self.rate_box.valueChanged.connect(self.update_ui)
        self.years_box.currentIndexChanged.connect(self.update_ui)

    def update_ui(self):
        principal = self.principal_box.value()
        rate = self.rate_box.value()
        years = self.years_box.currentIndex() + 1

        amount = principal * ((1 + (rate/100.0)) ** years)
        self.amount_val_label.setText("$ {0}".format(round(amount, 2)))


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
