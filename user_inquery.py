# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_inquery.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class UserInqueryDialog(object):
    dbmanager = None
    page_rental = 1
    page_size = 10
    userid = None
    userno = None

    def __init__(self, dbmanager):
        self.dbmanager = dbmanager

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(845, 600)
        self.Dialog = Dialog
        self.txtUserid = QtWidgets.QLineEdit(Dialog)
        self.txtUserid.setGeometry(QtCore.QRect(30, 20, 151, 31))
        self.txtUserid.setText("")
        self.txtUserid.setObjectName("txtUserid")

        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 221, 231))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 71, 16))
        self.label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 71, 16))
        self.label_2.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 71, 16))
        self.label_3.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 71, 16))
        self.label_4.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.lbOverdue = QtWidgets.QLabel(self.groupBox)
        self.lbOverdue.setGeometry(QtCore.QRect(100, 190, 101, 16))
        self.lbOverdue.setText("")
        self.lbOverdue.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lbOverdue.setObjectName("lbOverdue")
        self.lbUserno = QtWidgets.QLabel(self.groupBox)
        self.lbUserno.setGeometry(QtCore.QRect(100, 70, 101, 16))
        self.lbUserno.setText("")
        self.lbUserno.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lbUserno.setObjectName("lbUserno")
        self.lbTotal = QtWidgets.QLabel(self.groupBox)
        self.lbTotal.setGeometry(QtCore.QRect(100, 160, 101, 16))
        self.lbTotal.setText("")
        self.lbTotal.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lbTotal.setObjectName("lbTotal")
        self.lbUsername = QtWidgets.QLabel(self.groupBox)
        self.lbUsername.setGeometry(QtCore.QRect(100, 40, 101, 16))
        self.lbUsername.setText("")
        self.lbUsername.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lbUsername.setObjectName("lbUsername")
        self.lbEmail = QtWidgets.QLabel(self.groupBox)
        self.lbEmail.setGeometry(QtCore.QRect(100, 130, 101, 16))
        self.lbEmail.setText("")
        self.lbEmail.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lbEmail.setObjectName("lbEmail")
        self.lbPhonenum = QtWidgets.QLabel(self.groupBox)
        self.lbPhonenum.setGeometry(QtCore.QRect(100, 100, 101, 16))
        self.lbPhonenum.setText("")
        self.lbPhonenum.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lbPhonenum.setObjectName("lbPhonenum")
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setGeometry(QtCore.QRect(20, 130, 71, 16))
        self.label_21.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.label_25 = QtWidgets.QLabel(self.groupBox)
        self.label_25.setGeometry(QtCore.QRect(20, 100, 71, 16))
        self.label_25.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 20, 71, 32))
        self.pushButton.setObjectName("pushButton")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(310, 17, 58, 16))
        self.label_9.setObjectName("label_9")
        self.treeWidget = QtWidgets.QTreeWidget(Dialog)
        self.treeWidget.setGeometry(QtCore.QRect(260, 50, 561, 201))
        self.treeWidget.setWordWrap(True)
        self.treeWidget.setColumnCount(6) # 메모추가하면 7개
        self.treeWidget.setObjectName("treeWidget")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/books.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.treeWidget.headerItem().setIcon(2, icon)
        # icon1 = QtGui.QIcon()
        # icon1.addPixmap(QtGui.QPixmap("image/note.png"),
        #                 QtGui.QIcon.Normal, QtGui.QIcon.On)
        # self.treeWidget.headerItem().setIcon(6, icon1)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setDefaultSectionSize(70)
        self.treeWidget.setColumnWidth(0, 50)  # no
        self.treeWidget.setColumnWidth(1, 50)  # book unique no
        self.treeWidget.setColumnWidth(2, 200)  # title
        self.treeWidget.setColumnWidth(3, 95)  # rental date
        self.treeWidget.setColumnWidth(4, 95)  # due date
        self.treeWidget.setColumnWidth(5, 50)  # percentage
        # self.treeWidget.setColumnCount(6, 80) #note -> auto

        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(270, 10, 32, 32))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("image/books.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(270, 280, 32, 32))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("image/reserved.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(310, 288, 58, 16))
        self.label_12.setObjectName("label_12")
        self.treeWidget_2 = QtWidgets.QTreeWidget(Dialog)
        self.treeWidget_2.setGeometry(QtCore.QRect(260, 320, 561, 201))
        self.treeWidget_2.setObjectName("treeWidget_2")
        self.treeWidget_2.headerItem().setText(0, "1")

        self.treeWidget_2.setColumnCount(7)
        self.treeWidget_2.header().setDefaultSectionSize(70)
        self.treeWidget_2.setColumnWidth(0, 50)  # no
        self.treeWidget_2.setColumnWidth(1, 50)  # book no
        self.treeWidget_2.setColumnWidth(2, 120)  # title
        self.treeWidget_2.setColumnWidth(3, 100)  # author
        self.treeWidget_2.setColumnWidth(4, 95)  # reserv date
        self.treeWidget_2.setColumnWidth(5, 70)  # state

        self.treeWidget_2.headerItem().setIcon(2, icon)

        # self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        # self.groupBox_2.setGeometry(QtCore.QRect(20, 320, 221, 181))
        # self.groupBox_2.setObjectName("groupBox_2")
        # self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        # self.pushButton_2.setGeometry(QtCore.QRect(80, 39, 112, 51))
        # self.pushButton_2.setObjectName("pushButton_2")
        # self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        # self.pushButton_3.setGeometry(QtCore.QRect(80, 110, 112, 51))
        # self.pushButton_3.setObjectName("pushButton_3")
        # self.label_27 = QtWidgets.QLabel(self.groupBox_2)
        # self.label_27.setGeometry(QtCore.QRect(30, 50, 32, 32))
        # self.label_27.setText("")
        # self.label_27.setPixmap(QtGui.QPixmap("image/open-book.png"))
        # self.label_27.setScaledContents(True)
        # self.label_27.setObjectName("label_27")
        # self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        # self.label_28.setGeometry(QtCore.QRect(30, 120, 32, 32))
        # self.label_28.setText("")
        # self.label_28.setPixmap(QtGui.QPixmap("image/reservation.png"))
        # self.label_28.setScaledContents(True)
        # self.label_28.setObjectName("label_28")
        self.menubar = QtWidgets.QMenuBar(Dialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 22))
        self.menubar.setObjectName("menubar")
        self.btnReturn = QtWidgets.QPushButton(Dialog)
        self.btnReturn.setGeometry(QtCore.QRect(761, 10, 61, 32))
        self.btnReturn.setObjectName("btnReturn")

        self.btnExtend = QtWidgets.QPushButton(Dialog)
        self.btnExtend.setGeometry(QtCore.QRect(700, 10, 61, 32))
        self.btnExtend.setObjectName("btnExtend")


        self.btnRental = QtWidgets.QPushButton(Dialog)
        self.btnRental.setGeometry(QtCore.QRect(761, 281, 61, 32))
        self.btnRental.setObjectName("btnRental")

        # self.label_17 = QtWidgets.QLabel(Dialog)
        # self.label_17.setGeometry(QtCore.QRect(734, 12, 24, 24))
        # self.label_17.setText("")
        # self.label_17.setPixmap(QtGui.QPixmap("image/return.png"))
        # self.label_17.setScaledContents(True)
        # self.label_17.setObjectName("label_17")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.txtUserid.setPlaceholderText(_translate("Dialog", "Userid"))

        self.groupBox.setTitle(_translate("Dialog", "사용자 정보"))
        self.label.setText(_translate("Dialog", "이름 :"))
        self.label_2.setText(_translate("Dialog", "사용자 번호 :"))
        self.label_3.setText(_translate("Dialog", "연체권수 :"))
        self.label_4.setText(_translate("Dialog", "대여권수 :"))
        self.label_21.setText(_translate("Dialog", "이메일 :"))
        self.label_25.setText(_translate("Dialog", "휴대폰 번호 :"))
        self.pushButton.setText(_translate("Dialog", "조회"))
        self.pushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.label_9.setText(_translate("Dialog", "대여현황"))
        self.treeWidget.headerItem().setText(0, _translate("Dialog", "No"))
        self.treeWidget.headerItem().setText(1, _translate("Dialog", "책 번호"))
        self.treeWidget.headerItem().setText(2, _translate("Dialog", "제목"))
        self.treeWidget.headerItem().setText(3, _translate("Dialog", "대여시작일"))
        self.treeWidget.headerItem().setText(4, _translate("Dialog", "반납예정일"))
        self.treeWidget.headerItem().setText(5, _translate("Dialog", "반납까지"))
        # self.treeWidget.headerItem().setText(6, _translate("Dialog", "메모"))
        # __sortingEnabled = self.treeWidget.isSortingEnabled()
        # self.treeWidget.setSortingEnabled(False)
        # self.treeWidget.topLevelItem(0).setText(
        #     0, _translate("Dialog", "1"))
        # self.treeWidget.topLevelItem(0).setText(
        #     1, _translate("Dialog", "1"))
        # self.treeWidget.topLevelItem(0).setText(
        #     2, _translate("Dialog", "물은 답을 알고 있다"))
        # self.treeWidget.topLevelItem(0).setText(
        #     3, _translate("Dialog", "2019-12-04"))
        # self.treeWidget.topLevelItem(0).setText(
        #     4, _translate("Dialog", "2019-12-07"))
        # self.treeWidget.topLevelItem(0).setText(
        #     5, _translate("Dialog", "0"))
        # self.treeWidget.topLevelItem(0).setText(
        #     6, _translate("Dialog", "자"))
        # self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.treeWidget_2.headerItem().setText(0, _translate("Dialog", "No"))
        self.treeWidget_2.headerItem().setText(1, _translate("Dialog", "책 번호"))
        self.treeWidget_2.headerItem().setText(2, _translate("Dialog", "제목"))
        self.treeWidget_2.headerItem().setText(3, _translate("Dialog", "저자"))
        self.treeWidget_2.headerItem().setText(4, _translate("Dialog", "예약일자"))
        self.treeWidget_2.headerItem().setText(5, _translate("Dialog", "예약상태"))
        self.treeWidget_2.headerItem().setText(6, _translate("Dialog", "대여가능 수"))

        self.label_12.setText(_translate("Dialog", "예약현황"))
        
        # self.groupBox_2.setTitle(_translate("Dialog", "리 관리"))
        # self.pushButton_2.setText(_translate("Dialog", "대출"))
        # self.pushButton_3.setText(_translate("Dialog", "예약"))
        
        self.btnReturn.setText(_translate("Dialog", "반납"))
        self.btnExtend.setText(_translate("Dialog", "연장"))
        self.btnRental.setText(_translate("Dialog", "대여"))

        self.setEvent()

    def btnInqueryClicked(self):
        # try:
        self.page_rental = 1
        self.page_overdue = 1

        self.inquery_info()
        self.inquery_rental()
        self.inquery_reservation()
        # except Exception:
        #     print(Exception)
        #     pass
        # QtWidgets.QMessageBox().about(self, "title", "message")

    def inquery_info(self):
        userid = self.txtUserid.text()
        info = self.dbmanager.inquery_info(userid)
        if(info is not None):
            self.userid = userid
            self.userno = str(info['user_no'])
            self.lbUsername.setText(info['user_name'])
            self.lbUserno.setText(str(info['user_no']))
            self.lbPhonenum.setText(info['phonenum'])
            self.lbEmail.setText(info['email'])
            self.lbTotal.setText(str(info['total']))
            self.lbOverdue.setText(str(info['overdue']))
        else:
            self.show_alert("사용자 조회", "조회 결과가 없습니다")
        pass

    def show_alert(self, title, message):
        msgbox = QtWidgets.QMessageBox(self.Dialog)
        msgbox.setIcon(QtWidgets.QMessageBox.Warning)
        msgbox.setText(title)
        msgbox.setInformativeText(message)
        msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        return msgbox.exec()

    def inquery_rental(self, page=1):
        userid = self.userid
        size = self.page_size
        tw = self.treeWidget
        tw.clear()
        rows = self.dbmanager.inquery_rental(userid, size, page)
        for row in rows:
            item = self.addItem(tw)
            item.setText(0, str(row['rental_no']))
            item.setText(1, str(row['book_unique_no']))
            item.setText(2, str(row['title']))
            item.setText(3, str(row['rental_date']))
            item.setText(4, str(row['due_date']))

            percent = int(float(row['percent']))
            progress = QtWidgets.QProgressBar()
            prog_palette = '''
                QProgressBar {
                    border-radius: 5px;
                    text-align: center;
                    height:13px;
                    margin-top:2px;
                    margin-bottom:2px;
                    font-size:12px;
                }

                QProgressBar::chunk {
                    background-color: %s;
                    border-radius:4px;
                }
            '''
            if(row['overdue'] <= 0):
                progress.setValue(percent)
                prog_palette = prog_palette % ("#549ff0")
            else:
                progress.setValue(100)
                prog_palette = prog_palette % ("#f06654")
            progress.setStyleSheet(prog_palette)
            tw.setItemWidget(item, 5, progress)
            # item.setText(
            #     6, str(row['note'] if row['note'] is not None else ''))

    def inquery_reservation(self, page=1):
        userid = self.userid
        size = self.page_size
        tw = self.treeWidget_2
        tw.clear()
        rows = self.dbmanager.inquery_reservation(userid)
        for row in rows:
            item = self.addItem(tw)
            item.setText(0, str(row['reservation_no']))
            item.setText(1, str(row['book_no']))
            item.setText(2, str(row['title']))
            item.setText(3, str(row['author']))
            item.setText(4, str(row['reservation_date']))
            item.setText(5, str(row['state']))
            item.setText(6, str(row['possible_count']))

    def btnRentalClicked(self):
        userid = self.userid
        if(userid is not None):
            userno = self.userno
            items = self.treeWidget_2.selectedItems()
            if(items):
                reservation_no = items[0].text(0)
                book_no = items[0].text(1)
                title = items[0].text(2)

                messagebox = QtWidgets.QMessageBox(self.Dialog)
                messagebox.setText("도서 대여")
                messagebox.setInformativeText("'%s'\n\n대여처리 하시겠습니까?" % title)
                messagebox.setStandardButtons(
                    QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.No)
                messagebox.setDefaultButton(QtWidgets.QMessageBox.Ok)
                messagebox.setIcon(QtWidgets.QMessageBox.Question)
                ret = messagebox.exec()
                if(ret == QtWidgets.QMessageBox.Ok):
                    result = self.dbmanager.rental_book(reservation_no, userno, book_no)
                    if(result == -1):
                        self.show_alert("도서대여", "대여 가능한 책이 없습니다.")
                    self.inquery_info()
                    self.inquery_rental()
                    self.inquery_reservation()

    def btnReturnClicked(self):
        userid = self.userid
        if(userid is not None):
            userno = self.userno
            items = self.treeWidget.selectedItems()
            if(items):
                rental_no = items[0].text(0)
                book_unique_no = items[0].text(1)
                title = items[0].text(2)

                messagebox = QtWidgets.QMessageBox(self.Dialog)
                messagebox.setText("도서 반납")
                messagebox.setInformativeText("'%s'\n\n반납처리 하시겠습니까?" % title)
                messagebox.setStandardButtons(
                    QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.No)
                messagebox.setDefaultButton(QtWidgets.QMessageBox.Ok)
                messagebox.setIcon(QtWidgets.QMessageBox.Question)
                ret = messagebox.exec()
                if(ret == QtWidgets.QMessageBox.Ok):
                    self.dbmanager.return_book(rental_no, book_unique_no)
                    self.inquery_info()
                    self.inquery_rental()

    def btnExtendClicked(self):
        userid = self.userid
        if(userid is not None):
            userno = self.userno
            items = self.treeWidget.selectedItems()
            if(items):
                title = items[0].text(2)
                rental_no = items[0].text(0)
                messagebox = QtWidgets.QMessageBox(self.Dialog)
                messagebox.setText("도서 연장")
                messagebox.setInformativeText("'%s'\n\n연장처리 하시겠습니까?" % title)
                messagebox.setStandardButtons(
                    QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.No)
                messagebox.setDefaultButton(QtWidgets.QMessageBox.Ok)
                messagebox.setIcon(QtWidgets.QMessageBox.Question)
                ret = messagebox.exec()
                if(ret == QtWidgets.QMessageBox.Ok):
                    self.dbmanager.extend_book(rental_no)
                    self.inquery_rental()


    def setEvent(self):
        self.pushButton.clicked.connect(lambda: self.btnInqueryClicked())  # 조회
        # self.pushButton_3.clicked.connect() # 예약
        self.btnReturn.clicked.connect(lambda: self.btnReturnClicked())
        self.btnExtend.clicked.connect(lambda: self.btnExtendClicked())
        self.btnRental.clicked.connect(lambda: self.btnRentalClicked())  # 대출

    def addItem(self, tree):
        item = QtWidgets.QTreeWidgetItem(tree)
        return item


if __name__ == "__main__":
    import sys
    import dbmanager
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UserInqueryDialog(dbmanager.DBManager())
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
