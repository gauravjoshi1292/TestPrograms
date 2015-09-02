__author__ = 'gjoshi'

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class NumberFormatDialog(QDialog):
    def __init__(self, format, parent=None):
        super(NumberFormatDialog, self).__init__(parent)

        thousands_label = QLabel("&Thousands separator")
        self.thousand_edit = QLineEdit(format["thousands_separator"])
        thousands_label.setBuddy(self.thousand_edit)

        decimal_marker_label = QLabel("Decimal &marker")
        self.decimal_marker_edit = QLineEdit(format["decimal_marker"])
        decimal_marker_label.setBuddy(self.decimal_marker_edit)

        decimal_places_label = QLabel("&Decimal places")
        self.decimal_places_spinBox = QSpinBox()
        decimal_places_label.setBuddy(self.decimal_places_spinBox)
        self.decimal_places_spinBox.setRange(0, 6)
        self.decimal_places_spinBox.setValue(format["decimal_places"])

        self.red_negatives_checkbox = QCheckBox("&Red negative numbers")
        self.red_negatives_checkbox.setChecked(format["red_negatives"])

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        self.format = format.copy()

        grid = QGridLayout()
        grid.addWidget(thousands_label, 0, 0)
        grid.addWidget(self.thousand_edit, 0, 1)
        grid.addWidget(decimal_marker_label, 1, 0)
        grid.addWidget(self.decimal_marker_edit, 1, 1)
        grid.addWidget(decimal_places_label, 2, 0)
        grid.addWidget(self.decimal_places_spinBox, 2, 1)
        grid.addWidget(self.red_negatives_checkbox, 3, 0, 1, 2)
        grid.addWidget(button_box, 4, 0, 1, 2)
        self.setLayout(grid)

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        self.setWindowTitle("Set Number Format (Modal)")

    def number_format(self):
        return self.format

    def accept(self):
        class ThousandsError(Exception):
            pass

        class DecimalError(Exception):
            pass

        punctuation = frozenset(",;:.")

        thousands = unicode(self.thousand_edit.text())
        decimal = unicode(self.decimal_marker_edit.text())

        try:
            if len(decimal) == 0:
                raise DecimalError, "The decimal marker may not be empty."
            if len(thousands) > 1:
                raise ThousandsError, ("The thousands separator may only be empty or one"
                                       " character.")
            if len(decimal) > 1:
                raise DecimalError, "The decimal marker must be one character."
            if thousands == decimal:
                raise ThousandsError, ("The thousands separator and the decimal marker"
                                       " must be different.")
            if thousands and thousands not in punctuation:
                raise ThousandsError, ("The thousands separator must be a punctuation"
                                       " symbol.")
            if decimal not in punctuation:
                raise DecimalError, "The decimal marker must be a punctuation symbol."

        except ThousandsError, e:
            QMessageBox.warning(self, "Thousands Separator Error", unicode(e))
            self.thousand_edit.selectAll()
            self.thousand_edit.setFocus()
            return

        except DecimalError, e:
            QMessageBox.warning(self, "Decimal Marker Error", unicode(e))
            self.decimal_marker_edit.selectAll()
            self.decimal_marker_edit.setFocus()
            return

        self.format["thousands_separator"] = thousands
        self.format["decimal_marker"] = decimal
        self.format["decimal_places"] = self.decimal_places_spinBox.value()
        self.format["red_negatives"] = self.red_negatives_checkbox.isChecked()
        QDialog.accept(self)


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.format = dict(thousands_separator=",", decimal_marker=".", decimal_places=2,
                           red_negatives=False)
        self.set_number_format()

    def set_number_format(self):
        dialog = NumberFormatDialog(self.format, self)
        if dialog.exec_():
            self.format = dialog.number_format()
            print self.format

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
