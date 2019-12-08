# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\rental.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class RentalDialog(object):
    def __init__(self, dbmanager, book_unique_no):
        self.dbmanager = dbmanager
        self.book_unique_no = book_unique_no

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(375, 300)
        self.Dialog = Dialog
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 90, 191, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.dateEdit_today = QtWidgets.QDateEdit(Dialog)
        self.dateEdit_today.setGeometry(QtCore.QRect(130, 131, 191, 31))
        self.dateEdit_today.setStyleSheet("color: rgb(0, 0, 0);")
        self.dateEdit_today.setObjectName("dateEdit_today")
        self.dateEdit_duedate = QtWidgets.QDateEdit(Dialog)
        self.dateEdit_duedate.setGeometry(QtCore.QRect(130, 171, 191, 31))
        self.dateEdit_duedate.setObjectName("dateEdit_duedate")
        self.label_rentalDate = QtWidgets.QLabel(Dialog)
        self.label_rentalDate.setGeometry(QtCore.QRect(40, 140, 81, 16))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.label_rentalDate.setFont(font)
        self.label_rentalDate.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_rentalDate.setObjectName("label_rentalDate")
        self.label_dueDate_2 = QtWidgets.QLabel(Dialog)
        self.label_dueDate_2.setGeometry(QtCore.QRect(40, 180, 81, 16))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.label_dueDate_2.setFont(font)
        self.label_dueDate_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_dueDate_2.setObjectName("label_dueDate_2")
        self.label_userID = QtWidgets.QLabel(Dialog)
        self.label_userID.setGeometry(QtCore.QRect(40, 100, 81, 16))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.label_userID.setFont(font)
        self.label_userID.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_userID.setObjectName("label_userID")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 210, 191, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 10, 241, 61))
        font = QtGui.QFont()
        font.setFamily("메이플스토리")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_27 = QtWidgets.QLabel(Dialog)
        self.label_27.setGeometry(QtCore.QRect(50, 20, 41, 41))
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap(".\\ui\\image/open-book.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.label_memo = QtWidgets.QLabel(Dialog)
        self.label_memo.setGeometry(QtCore.QRect(40, 220, 81, 16))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.label_memo.setFont(font)
        self.label_memo.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_memo.setObjectName("label_memo")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 261, 93, 28))
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "KU Library"))
        self.pushButton.setText(_translate("Dialog", "대출"))
        self.label_memo.setText(_translate("Dialog", "메모"))
        self.label_rentalDate.setText(_translate("Dialog", "대여 날짜"))
        self.label_dueDate_2.setText(_translate("Dialog", "반납예정일"))
        self.label_userID.setText(_translate("Dialog", "회원 아이디"))
        self.label.setText(_translate("Dialog", "도서 대출"))
        self.pushButton.clicked.connect(lambda: self.btnRentalClicked())

        import datetime
        self.dateEdit_today.setDate(datetime.datetime.now())
        self.dateEdit_duedate.setDate(datetime.datetime.now() + datetime.timedelta(days=5))
        self.dateEdit_duedate.setMinimumDate(self.dateEdit_today.date())
        # self.dateEdit_duedate.setEnabled(False)
    def btnRentalClicked(self):
        user_id = self.lineEdit.text()
        info = self.dbmanager.inquery_info(user_id)
        if(info is not None):
            user_no = info['user_no']
            if(self.dbmanager.rental_book(user_no, self.book_unique_no, self.dateEdit_today.date().toString("yyyy-MM-dd"), self.dateEdit_duedate.date().toString("yyyy-MM-dd"), self.lineEdit_5.text()) == True):
                self.show_message("도서 대여", "도서 대여가 완료되었습니다.")
                self.Dialog.close()
            else:
                self.show_alert("도서 대여", "도서 대여에 실패했습니다.")
        else: 
            self.show_alert("사용자 조회", "사용자 조회 결과가 없습니다")
        
    def show_alert(self, title, message):
        msgbox = QtWidgets.QMessageBox(self.Dialog)
        msgbox.setIcon(QtWidgets.QMessageBox.Warning)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        return msgbox.exec()

    def show_message(self, title, message):
        msgbox = QtWidgets.QMessageBox(self.Dialog)
        msgbox.setIcon(QtWidgets.QMessageBox.Information)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        return msgbox.exec()
