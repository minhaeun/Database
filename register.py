# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/register.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class RegisterDialog(object):
    def __init__(self, dbmanager):
        self.dbmanager = dbmanager

    def setupUi(self, RegisterDialog):
        RegisterDialog.setObjectName("RegisterDialog")
        RegisterDialog.resize(332, 370)
        self.Dialog = RegisterDialog
        self.label = QtWidgets.QLabel(RegisterDialog)
        self.label.setGeometry(QtCore.QRect(30, 140, 80, 80))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ui/image/user.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit0 = QtWidgets.QLineEdit(RegisterDialog)
        self.lineEdit0.setGeometry(QtCore.QRect(142, 110, 151, 31))
        self.lineEdit0.setFont(font)
        self.lineEdit0.setObjectName("lineEdit0")
        self.lineEdit1 = QtWidgets.QLineEdit(RegisterDialog)
        self.lineEdit1.setGeometry(QtCore.QRect(142, 150, 151, 31))
        self.lineEdit1.setFont(font)
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit2 = QtWidgets.QLineEdit(RegisterDialog)
        self.lineEdit2.setGeometry(QtCore.QRect(142, 190, 151, 31))
        self.lineEdit2.setFont(font)
        self.lineEdit2.setObjectName("lineEdit2")
        self.lineEdit3 = QtWidgets.QLineEdit(RegisterDialog)
        self.lineEdit3.setGeometry(QtCore.QRect(142, 230, 151, 31))
        self.lineEdit3.setFont(font)
        self.lineEdit3.setObjectName("lineEdit3")
        self.pushButton = QtWidgets.QPushButton(RegisterDialog)
        self.pushButton.setGeometry(QtCore.QRect(161, 290, 121, 41))
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.label_2 = QtWidgets.QLabel(RegisterDialog)
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

        self.retranslateUi(RegisterDialog)
        QtCore.QMetaObject.connectSlotsByName(RegisterDialog)

    def retranslateUi(self, RegisterDialog):
        _translate = QtCore.QCoreApplication.translate
        RegisterDialog.setWindowTitle(_translate("RegisterDialog", "KU Library"))
        self.lineEdit3.setPlaceholderText(_translate("RegisterDialog", "Phone Number"))
        self.lineEdit2.setPlaceholderText(_translate("RegisterDialog", "Email"))
        self.lineEdit0.setPlaceholderText(_translate("RegisterDialog", "Userid"))
        self.lineEdit1.setPlaceholderText(_translate("RegisterDialog", "Username"))
        self.pushButton.setText(_translate("RegisterDialog", "Submit"))
        self.label_2.setText(_translate("RegisterDialog", "Register"))

        self.addBtnListener()

    def btnRegisterClicked(self):
        userid = self.lineEdit0.text()
        username = self.lineEdit1.text()
        email = self.lineEdit2.text()
        phonenum = self.lineEdit3.text()
        info = self.dbmanager.register_check(userid)
        if(info['count'] != 0):
            self.show_alert("회원등록", "이미 등록된 회원 아이디입니다.")
        else:
            if(self.dbmanager.register(userid, username, email, phonenum) == 1):
                self.show_info("회원등록", "회원등록 성공")
            else:
                self.show_alert("회원등록", "회원등록 실패")

    def addBtnListener(self):
        self.pushButton.clicked.connect(lambda: self.btnRegisterClicked())

    def show_info(self, title, message):
        msgbox = QtWidgets.QMessageBox(self.Dialog)
        msgbox.setIcon(QtWidgets.QMessageBox.Information)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        return msgbox.exec()

    def show_alert(self, title, message):
        msgbox = QtWidgets.QMessageBox(self.Dialog)
        msgbox.setIcon(QtWidgets.QMessageBox.Warning)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        return msgbox.exec()
 