# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/register.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(332, 370)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 140, 80, 80))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ui/image/user.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(142, 230, 151, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(142, 190, 151, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(142, 110, 151, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(142, 150, 151, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(161, 290, 121, 41))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 291, 81))
        font = QtGui.QFont()
        font.setFamily("메이플스토리")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "Phone Number"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Email"))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog", "Userid"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Username"))
        self.pushButton.setText(_translate("Dialog", "Submit"))
        self.label_2.setText(_translate("Dialog", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
