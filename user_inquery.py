# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_inquery.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from DBManager import DBManager


class Ui_MainWindow(object):
    dbmanager = DBManager()
    page_rental = 1
    page_overdue = 1
    page_size = 3

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(845, 600)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtUserid = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUserid.setGeometry(QtCore.QRect(30, 20, 151, 31))
        self.txtUserid.setText("")
        self.txtUserid.setObjectName("txtUserid")
        

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 221, 231))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 71, 16))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 71, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 71, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 71, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.lbOverdue = QtWidgets.QLabel(self.groupBox)
        self.lbOverdue.setGeometry(QtCore.QRect(100, 190, 101, 16))
        self.lbOverdue.setText("")
        self.lbOverdue.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbOverdue.setObjectName("lbOverdue")
        self.lbUserno = QtWidgets.QLabel(self.groupBox)
        self.lbUserno.setGeometry(QtCore.QRect(100, 70, 101, 16))
        self.lbUserno.setText("")
        self.lbUserno.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbUserno.setObjectName("lbUserno")
        self.lbTotal = QtWidgets.QLabel(self.groupBox)
        self.lbTotal.setGeometry(QtCore.QRect(100, 160, 101, 16))
        self.lbTotal.setText("")
        self.lbTotal.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbTotal.setObjectName("lbTotal")
        self.lbUsername = QtWidgets.QLabel(self.groupBox)
        self.lbUsername.setGeometry(QtCore.QRect(100, 40, 101, 16))
        self.lbUsername.setText("")
        self.lbUsername.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbUsername.setObjectName("lbUsername")
        self.lbEmail = QtWidgets.QLabel(self.groupBox)
        self.lbEmail.setGeometry(QtCore.QRect(100, 130, 101, 16))
        self.lbEmail.setText("")
        self.lbEmail.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbEmail.setObjectName("lbEmail")
        self.lbPhonenum = QtWidgets.QLabel(self.groupBox)
        self.lbPhonenum.setGeometry(QtCore.QRect(100, 100, 101, 16))
        self.lbPhonenum.setText("")
        self.lbPhonenum.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbPhonenum.setObjectName("lbPhonenum")
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setGeometry(QtCore.QRect(20, 130, 71, 16))
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.label_25 = QtWidgets.QLabel(self.groupBox)
        self.label_25.setGeometry(QtCore.QRect(20, 100, 71, 16))
        self.label_25.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 20, 71, 32))
        self.pushButton.setObjectName("pushButton")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(310, 17, 58, 16))
        self.label_9.setObjectName("label_9")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(260, 50, 561, 181))
        self.treeWidget.setWordWrap(True)
        self.treeWidget.setColumnCount(7)
        self.treeWidget.setObjectName("treeWidget")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/books.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.treeWidget.headerItem().setIcon(2, icon)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/note.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.treeWidget.headerItem().setIcon(6, icon1)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setDefaultSectionSize(70)
        self.treeWidget.setColumnWidth(0, 50)  # no
        self.treeWidget.setColumnWidth(1, 50)  # book unique no
        self.treeWidget.setColumnWidth(2, 120)  # title
        self.treeWidget.setColumnWidth(3, 95)  # rental date
        self.treeWidget.setColumnWidth(4, 95)  # due date
        self.treeWidget.setColumnWidth(5, 50)  # percentage
        # self.treeWidget.setColumnCount(6, 80) #note -> auto

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(270, 10, 32, 32))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("image/books.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(270, 280, 32, 32))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("image/deadline.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(310, 288, 58, 16))
        self.label_12.setObjectName("label_12")
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget_2.setGeometry(QtCore.QRect(260, 320, 561, 181))
        self.treeWidget_2.setObjectName("treeWidget_2")
        self.treeWidget_2.headerItem().setText(0, "1")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 320, 221, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 39, 112, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 110, 112, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_27 = QtWidgets.QLabel(self.groupBox_2)
        self.label_27.setGeometry(QtCore.QRect(30, 50, 32, 32))
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("image/open-book.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        self.label_28.setGeometry(QtCore.QRect(30, 120, 32, 32))
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap("image/reservation.png"))
        self.label_28.setScaledContents(True)
        self.label_28.setObjectName("label_28")
        self.pagePrev1 = QtWidgets.QLabel(self.centralwidget)
        self.pagePrev1.setGeometry(QtCore.QRect(410, 230, 50, 50))
        self.pagePrev1.setText("")
        self.pagePrev1.setPixmap(QtGui.QPixmap("image/square.png"))
        self.pagePrev1.setScaledContents(True)
        self.pagePrev1.setObjectName("pagePrev1")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(420, 240, 30, 30))
        self.label_13.setAutoFillBackground(False)
        self.label_13.setStyleSheet("background-color: rgb(252, 61, 197);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(570, 240, 30, 30))
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.pagePrev1_3 = QtWidgets.QLabel(self.centralwidget)
        self.pagePrev1_3.setGeometry(QtCore.QRect(560, 230, 50, 50))
        self.pagePrev1_3.setText("")
        self.pagePrev1_3.setPixmap(QtGui.QPixmap("image/square.png"))
        self.pagePrev1_3.setScaledContents(True)
        self.pagePrev1_3.setObjectName("pagePrev1_3")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(520, 240, 30, 30))
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.pagePrev1_4 = QtWidgets.QLabel(self.centralwidget)
        self.pagePrev1_4.setGeometry(QtCore.QRect(510, 230, 50, 50))
        self.pagePrev1_4.setText("")
        self.pagePrev1_4.setPixmap(QtGui.QPixmap("image/square.png"))
        self.pagePrev1_4.setScaledContents(True)
        self.pagePrev1_4.setObjectName("pagePrev1_4")
        self.pagePrev1_7 = QtWidgets.QLabel(self.centralwidget)
        self.pagePrev1_7.setGeometry(QtCore.QRect(460, 230, 50, 50))
        self.pagePrev1_7.setText("")
        self.pagePrev1_7.setPixmap(QtGui.QPixmap("image/square.png"))
        self.pagePrev1_7.setScaledContents(True)
        self.pagePrev1_7.setObjectName("pagePrev1_7")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(470, 240, 30, 30))
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.pagePrev1_8 = QtWidgets.QLabel(self.centralwidget)
        self.pagePrev1_8.setGeometry(QtCore.QRect(610, 230, 50, 50))
        self.pagePrev1_8.setText("")
        self.pagePrev1_8.setPixmap(QtGui.QPixmap("image/square.png"))
        self.pagePrev1_8.setScaledContents(True)
        self.pagePrev1_8.setObjectName("pagePrev1_8")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(620, 240, 30, 30))
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.pagePrev1_9 = QtWidgets.QLabel(self.centralwidget)
        self.pagePrev1_9.setGeometry(QtCore.QRect(510, 500, 50, 50))
        self.pagePrev1_9.setText("")
        self.pagePrev1_9.setPixmap(QtGui.QPixmap("image/square.png"))
        self.pagePrev1_9.setScaledContents(True)
        self.pagePrev1_9.setObjectName("pagePrev1_9")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(570, 510, 30, 30))
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(470, 510, 30, 30))
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(520, 510, 30, 30))
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.pagePrev1_11 = QtWidgets.QLabel(self.centralwidget)
        self.pagePrev1_11.setGeometry(QtCore.QRect(610, 500, 50, 50))
        self.pagePrev1_11.setText("")
        self.pagePrev1_11.setPixmap(QtGui.QPixmap("image/square.png"))
        self.pagePrev1_11.setScaledContents(True)
        self.pagePrev1_11.setObjectName("pagePrev1_11")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(420, 510, 30, 30))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.pagePrev1_2 = QtWidgets.QLabel(self.centralwidget)
        self.pagePrev1_2.setGeometry(QtCore.QRect(410, 500, 50, 50))
        self.pagePrev1_2.setText("")
        self.pagePrev1_2.setPixmap(QtGui.QPixmap("image/square.png"))
        self.pagePrev1_2.setScaledContents(True)
        self.pagePrev1_2.setObjectName("pagePrev1_2")
        self.pagePrev1_12 = QtWidgets.QLabel(self.centralwidget)
        self.pagePrev1_12.setGeometry(QtCore.QRect(460, 500, 50, 50))
        self.pagePrev1_12.setText("")
        self.pagePrev1_12.setPixmap(QtGui.QPixmap("image/square.png"))
        self.pagePrev1_12.setScaledContents(True)
        self.pagePrev1_12.setObjectName("pagePrev1_12")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(620, 510, 30, 30))
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.pagePrev1_13 = QtWidgets.QLabel(self.centralwidget)
        self.pagePrev1_13.setGeometry(QtCore.QRect(560, 500, 50, 50))
        self.pagePrev1_13.setText("")
        self.pagePrev1_13.setPixmap(QtGui.QPixmap("image/square.png"))
        self.pagePrev1_13.setScaledContents(True)
        self.pagePrev1_13.setObjectName("pagePrev1_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.txtUserid.setPlaceholderText(_translate("MainWindow", "Userid"))

        self.groupBox.setTitle(_translate("MainWindow", "사용자 정보"))
        self.label.setText(_translate("MainWindow", "이름 :"))
        self.label_2.setText(_translate("MainWindow", "사용자 번호 :"))
        self.label_3.setText(_translate("MainWindow", "연체권수 :"))
        self.label_4.setText(_translate("MainWindow", "대여권수 :"))
        self.label_21.setText(_translate("MainWindow", "이메일 :"))
        self.label_25.setText(_translate("MainWindow", "휴대폰 번호 :"))
        self.pushButton.setText(_translate("MainWindow", "조회"))
        self.pushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.label_9.setText(_translate("MainWindow", "대여현황"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "No"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "책 번호"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "제목"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "대여시작일"))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "반납예정일"))
        self.treeWidget.headerItem().setText(5, _translate("MainWindow", "연체일"))
        self.treeWidget.headerItem().setText(6, _translate("MainWindow", "메모"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(
            0, _translate("MainWindow", "1"))
        self.treeWidget.topLevelItem(0).setText(
            1, _translate("MainWindow", "1"))
        self.treeWidget.topLevelItem(0).setText(
            2, _translate("MainWindow", "물은 답을 알고 있다"))
        self.treeWidget.topLevelItem(0).setText(
            3, _translate("MainWindow", "2019-12-04"))
        self.treeWidget.topLevelItem(0).setText(
            4, _translate("MainWindow", "2019-12-07"))
        self.treeWidget.topLevelItem(0).setText(
            5, _translate("MainWindow", "0"))
        self.treeWidget.topLevelItem(0).setText(
            6, _translate("MainWindow", "상습연체자"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.label_12.setText(_translate("MainWindow", "연체현황"))
        self.groupBox_2.setTitle(_translate("MainWindow", "사서 관리"))
        self.pushButton_2.setText(_translate("MainWindow", "대출"))
        self.pushButton_3.setText(_translate("MainWindow", "예약"))
        self.label_13.setText(_translate("MainWindow", "<"))
        self.label_15.setText(_translate("MainWindow", "3"))
        self.label_16.setText(_translate("MainWindow", "2"))
        self.label_19.setText(_translate("MainWindow", "1"))
        self.label_20.setText(_translate("MainWindow", ">"))
        self.label_22.setText(_translate("MainWindow", "3"))
        self.label_23.setText(_translate("MainWindow", "1"))
        self.label_24.setText(_translate("MainWindow", "2"))
        self.label_14.setText(_translate("MainWindow", "<"))
        self.label_26.setText(_translate("MainWindow", ">"))

        self.setEvent()

    def btnInquery(self):
        self.userid = self.txtUserid.text()
        self.page_rental = 1
        self.page_overdue = 1

        self.inquery_info()
        self.inquery_rental()
        self.inquery_overdue()

    def inquery_info(self):
        userid = self.userid
        info = self.dbmanager.inquery_info(userid)
        
        self.lbUsername.setText(info['user_name'])
        self.lbUserno.setText(str(info['user_no']))
        self.lbPhonenum.setText(info['phonenum'])
        self.lbEmail.setText(info['email'])
        self.lbTotal.setText(str(info['total']))
        self.lbOverdue.setText(str(info['overdue']))
        
        pass

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
            progress = QtWidgets.QProgressBar()
            percent = round(float(row['percent']))
            if(percent > 100):
                percent = 100
            progress.setValue()
            tw.setItemWidget(item, 5, progress)
            # item.setText(5, str(row['percent']))
            item.setText(
                6, str(row['note'] if row['note'] is not None else ''))

    def inquery_overdue(self):
        pass

    def setEvent(self):
        self.pushButton.clicked.connect(self.btnInquery)  # 조회
        # self.pushButton_2.clicked.connect() # 대출
        # self.pushButton_3.clicked.connect() # 예약

    def addItem(self, tree):
        item = QtWidgets.QTreeWidgetItem(tree)
        return item


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
