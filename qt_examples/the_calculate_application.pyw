__author__ = 'gjoshi'

import sys
from PyQt4.QtGui import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.line_edit = QLineEdit("Type an expression and press Enter")
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.line_edit)
        self.setLayout(layout)
        self.line_edit.selectAll()
        self.line_edit.setFocus()
        self.line_edit.returnPressed.connect(self.update_ui)
        self.setWindowTitle("Calculate")

    def update_ui(self):
        text = ""
        try:
            text = unicode(self.line_edit.text())
            self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
        except:
            self.browser.append("<font color=red>%s is invalid!</font>" % text)

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
