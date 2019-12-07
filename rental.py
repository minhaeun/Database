# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/rental.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(613, 538)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 80, 241, 61))
        font = QtGui.QFont()
        font.setFamily("메이플스토리")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.label_27 = QtWidgets.QLabel(Form)
        self.label_27.setGeometry(QtCore.QRect(160, 90, 41, 41))
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("image/open-book.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(260, 330, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(240, 160, 191, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_userID = QtWidgets.QLabel(Form)
        self.label_userID.setGeometry(QtCore.QRect(150, 170, 81, 16))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.label_userID.setFont(font)
        self.label_userID.setObjectName("label_userID")
        self.label_rentalDate = QtWidgets.QLabel(Form)
        self.label_rentalDate.setGeometry(QtCore.QRect(150, 210, 81, 16))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.label_rentalDate.setFont(font)
        self.label_rentalDate.setObjectName("label_rentalDate")
        self.label_dueDate_2 = QtWidgets.QLabel(Form)
        self.label_dueDate_2.setGeometry(QtCore.QRect(150, 250, 81, 16))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.label_dueDate_2.setFont(font)
        self.label_dueDate_2.setObjectName("label_dueDate_2")
        self.label_memo = QtWidgets.QLabel(Form)
        self.label_memo.setGeometry(QtCore.QRect(150, 290, 81, 16))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.label_memo.setFont(font)
        self.label_memo.setObjectName("label_memo")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(240, 280, 191, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.dateEdit_today = QtWidgets.QDateEdit(Form)
        self.dateEdit_today.setGeometry(QtCore.QRect(240, 201, 191, 31))
        self.dateEdit_today.setObjectName("dateEdit_today")
        self.dateEdit_duedate = QtWidgets.QDateEdit(Form)
        self.dateEdit_duedate.setGeometry(QtCore.QRect(240, 241, 191, 31))
        self.dateEdit_duedate.setObjectName("dateEdit_duedate")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)






    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "도서 대출"))
        self.pushButton.setText(_translate("Form", "대출"))
        self.label_userID.setText(_translate("Form", "회원 아이디"))
        self.label_rentalDate.setText(_translate("Form", "대여 날짜"))
        self.label_dueDate_2.setText(_translate("Form", "반납예정일"))
        self.label_memo.setText(_translate("Form", "메모"))
        self.btnConnect()

    def btnConnect(self):
        self.pushButton.clicked.connect(self.btnPushButtonClicked)

    def btnPushButtonClicked(self):
        dbmanager = DBManager()
       

        result = dbmanager.inquery_rental()
        print(result)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
