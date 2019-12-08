# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\search_detail.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import math
from rental import RentalDialog


class SearchDetailDialog(object):
    no = 0

    def __init__(self, dbmanager, book_no):
        self.dbmanager = dbmanager
        self.book_no = book_no

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 650)
        self.Dialog = Dialog
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 600, 51))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 600, 61))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 600, 16))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 150, 600, 16))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(40, 220, 600, 400))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setMidLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 600, 400))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 190, 110, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "KU Library"))
        self.label.setText(_translate("Dialog", "정리하는 뇌"))
        self.label_2.setText(_translate(
            "Dialog", "Levitin, Daniel J .: 김성훈 / 출판사"))
        self.label_3.setText(_translate("Dialog", "책번호 :"))
        self.label_4.setText(_translate("Dialog", "대출여부 :"))
        self.pushButton.setText(_translate("Dialog", "책 추가 등록"))
        self.pushButton.clicked.connect(lambda:self.btnPushClicked())

        self.scrollLayout = QtWidgets.QGridLayout()
        self.scrollLayout.setSizeConstraint(QtWidgets.QGridLayout.SetFixedSize)
        self.scrollAreaWidgetContents.setLayout(self.scrollLayout)

        self.getBookInfo()
        self.addBookList()

    def getBookInfo(self):
        info = self.dbmanager.book_detail(self.book_no)
        self.title = info['title']
        self.label.setText(self.title)
        self.label_2.setText("%s | %s | %s" % (
            info['author'], info['publisher'], info['published_date']))
        self.label_3.setText("책 구분 번호 : %s" % info['book_no'])
        self.label_4.setText("대여 가능 여부 : %s" %
                             ("가능" if info['count'] > 0 else "불가능"))

    def addBookList(self):
        title = self.title
        # clear 기능
        while(self.scrollLayout.count() != 0):
            item = self.scrollLayout.itemAt(0)
            if(item):
                self.scrollLayout.removeItem(item)
                item.widget().deleteLater() 
        #
        rows = self.dbmanager.book_list(self.book_no)
        no = 0
        for row in rows:
            book_unique_no = row['book_unique_no']
            condition = row['condition']
            enabled = True if condition == '대여가능' else False
            item = BookInfo(title, book_unique_no,
                            condition, enabled, self)
            item.setFixedSize(270, 80)
            self.scrollLayout.addWidget(item, math.floor(no / 2), no % 2)
            no += 1

    def btnPushClicked(self): 
        title = self.title
        messagebox = QtWidgets.QMessageBox(self.Dialog)
        messagebox.setWindowTitle("추가등록")
        messagebox.setText("'%s'\n\n책을 추가등록 하시겠습니까?" % title)
        messagebox.setStandardButtons(
            QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.No)
        messagebox.setDefaultButton(QtWidgets.QMessageBox.Ok)
        messagebox.setIcon(QtWidgets.QMessageBox.Question)
        ret = messagebox.exec()
        if(ret == QtWidgets.QMessageBox.Ok):
            self.dbmanager.add_book(self.book_no)
            self.addBookList() # refresh 

    def remove_book(self, book_unique_no):
        self.dbmanager.remove_book(book_unique_no)
        self.addBookList() # refresh
        pass

    def rental_book(self, book_unique_no):  
        Dialog = QtWidgets.QDialog(self.Dialog)
        ui = RentalDialog(self.dbmanager, book_unique_no)
        ui.setupUi(Dialog)
        Dialog.setModal(True)
        Dialog.show() 

    def reservation_book(self, book_unique_no):
        self.show_alert("도서예약","만들어야합니다")
        pass

    def show_alert(self, title, message):
        msgbox = QtWidgets.QMessageBox(self.Dialog)
        msgbox.setIcon(QtWidgets.QMessageBox.Warning)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        return msgbox.exec()


class BookInfo(QtWidgets.QWidget):
    def __init__(self, title, book_unique_no, state, enabled, Dialog, parent=None):
        super(BookInfo, self).__init__(parent)  
        self.Dialog = Dialog
        self.title = title
        self.book_unique_no = book_unique_no
        self.state = state
        self.enabled = enabled

        layout = QtWidgets.QFormLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        lbUniqueText = QtWidgets.QLabel("등록번호")
        lbUniqueText.setMinimumSize(QtCore.QSize(80, 0))
        lbUniqueNo = QtWidgets.QLabel(str(book_unique_no))

        layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, lbUniqueText)
        layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, lbUniqueNo)

        lbStateText = QtWidgets.QLabel("상태")
        lbStateText.setMinimumSize(QtCore.QSize(80, 0))
        lbState = QtWidgets.QLabel(str(state))

        layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, lbStateText)
        layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, lbState) 

        form = QtWidgets.QWidget()
        form.setMinimumSize(QtCore.QSize(0, 40))
        horizontalLayout = QtWidgets.QHBoxLayout()
        horizontalLayout.setObjectName("horizontalLayout")
        btnRental = QtWidgets.QPushButton("대여")
        btnRental.setObjectName("btnRental")
        horizontalLayout.addWidget(btnRental)
        btnRemove = QtWidgets.QPushButton("삭제")
        btnRemove.setObjectName("btnRemove")
        horizontalLayout.addWidget(btnRemove)
        btnReservation = QtWidgets.QPushButton("예약")
        btnReservation.setObjectName("btnRemove")
        horizontalLayout.addWidget(btnReservation)
        form.setLayout(horizontalLayout)
        layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, form)
        btnRental.setEnabled(enabled)  # 대여상태 아닐때만 대여 가능
        btnRemove.setEnabled(enabled)  # 대여상태 아닐때만 삭제 가능
        btnReservation.setEnabled(not enabled)

        btnRental.clicked.connect(self.btnRentalClicked)
        btnRemove.clicked.connect(self.btnRemoveClicked)
        btnReservation.clicked.connect(self.btnReservationClicked)

        self.setLayout(layout)
        # self.setStyleSheet("background-color:#ff0000")

    def btnRentalClicked(self):
        book_unique_no = self.book_unique_no
        messagebox = QtWidgets.QMessageBox(self)
        messagebox.setWindowTitle("도서 대여")
        messagebox.setText("%s번 도서\n\n대여처리 하시겠습니까?" % book_unique_no)
        messagebox.setStandardButtons(
            QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.No)
        messagebox.setDefaultButton(QtWidgets.QMessageBox.Ok)
        messagebox.setIcon(QtWidgets.QMessageBox.Question)
        ret = messagebox.exec()
        if(ret == QtWidgets.QMessageBox.Ok):
            self.Dialog.rental_book(self.book_unique_no)

    def btnRemoveClicked(self):
        book_unique_no = self.book_unique_no
        messagebox = QtWidgets.QMessageBox(self)
        messagebox.setWindowTitle("도서 삭제")
        messagebox.setText("%s번 도서\n\n삭제처리 하시겠습니까?" % book_unique_no)
        messagebox.setStandardButtons(
            QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.No)
        messagebox.setDefaultButton(QtWidgets.QMessageBox.Ok)
        messagebox.setIcon(QtWidgets.QMessageBox.Question)
        ret = messagebox.exec()
        if(ret == QtWidgets.QMessageBox.Ok):
            self.Dialog.remove_book(book_unique_no)

    def btnReservationClicked(self):
        book_unique_no = self.book_unique_no
        messagebox = QtWidgets.QMessageBox(self)
        messagebox.setWindowTitle("도서 대여")
        messagebox.setText("%s번 도서\n\n예약처리 하시겠습니까?" % book_unique_no)
        messagebox.setStandardButtons(
            QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.No)
        messagebox.setDefaultButton(QtWidgets.QMessageBox.Ok)
        messagebox.setIcon(QtWidgets.QMessageBox.Question)
        ret = messagebox.exec()
        if(ret == QtWidgets.QMessageBox.Ok):
            self.Dialog.reservation_book(self.book_unique_no)
        pass