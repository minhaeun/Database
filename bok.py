# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'books.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from mywidget import MyWidget

class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 600)
        # Form.setStyleSheet("Background-color: #ddd")
        self.widget = MyWidget(self)
        self.widget.setAutoFillBackground(True)
        self.widget.setStyleSheet("Background-color: #000")
        self.widget.setGeometry(QtCore.QRect(0, 0, 300, 111))
        self.widget.setObjectName("widget")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
