__author__ = 'gjoshi'

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class PenPropertiesDlg(QDialog):
    def __init__(self, parent=None):
        super(PenPropertiesDlg, self).__init__(parent)

        width_label = QLabel("&Width:")
        self.width_spin_box = QSpinBox()
        width_label.setBuddy(self.width_spin_box)
        self.width_spin_box.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.width_spin_box.setRange(0, 24)

        self.beveled_check_box = QCheckBox("&Beveled edges")

        style_label = QLabel("&Style:")
        self.style_combo_box = QComboBox()
        style_label.setBuddy(self.style_combo_box)
        self.style_combo_box.addItems(["Solid", "Dashed", "Dotted", "DashDotted",
                                       "DashDotDotted"])

        ok_button = QPushButton("&OK")
        cancel_button = QPushButton("&Cancel")

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)

        layout = QGridLayout()
        layout.addWidget(width_label, 0, 0)
        layout.addWidget(self.width_spin_box, 0, 1)
        layout.addWidget(self.beveled_check_box, 0, 2)
        layout.addWidget(style_label, 1, 0)
        layout.addWidget(self.style_combo_box, 1, 1, 1, 2)
        layout.addLayout(button_layout, 2, 0, 1, 3)
        self.setLayout(layout)

        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)

        self.setWindowTitle("Pen Properties")


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.width = 0
        self.beveled = True
        self.style = "DashDotted"
        self.set_pen_properties()

    def set_pen_properties(self):
        dialog = PenPropertiesDlg(self)
        dialog.width_spin_box.setValue(self.width)
        dialog.beveled_check_box.setChecked(self.beveled)
        dialog.style_combo_box.setCurrentIndex(
            dialog.style_combo_box.findText(self.style))

        if dialog.exec_():
            self.width = dialog.width_spin_box.value()
            self.beveled = dialog.beveled_check_box.isChecked()
            self.style = unicode(dialog.style_combo_box.currentText())
            self.update_data()

    def update_data(self):
        label = QLabel("{0} {1} {2}".format(self.width, self.beveled, self.style))
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
