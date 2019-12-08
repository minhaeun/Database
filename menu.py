# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from dbmanager import DBManager
from search import SearchDialog
from register import RegisterDialog
from book_register import BookRegisterDialog
from user_inquery import UserInqueryDialog
from overdue import Ui_Dialog as OverdueDialog
class Ui_MainWindow(object):
    def __init__(self):
        self.dbmanager = DBManager()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(774, 707)
        self.MainWindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 330, 91, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 330, 91, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 560, 91, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 560, 91, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 200, 101, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 400, 131, 41))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2") 
        font = QtGui.QFont()
        font.setFamily("나눔고딕") 
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(397, 560, 91, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 200, 31, 31))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("ui/image/user2.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 250, 71, 71))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("ui/image/login.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 250, 71, 71))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("ui/image/search-user-interface-symbol.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(120, 400, 32, 32))
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("ui/image/open-book.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(140, 460, 81, 81))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("ui/image/search-of-knowledge.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(270, 460, 71, 71))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("ui/image/clipboard.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(410, 460, 81, 81))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("ui/image/out-of-time.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(230, 60, 461, 101))
        font = QtGui.QFont()
        font.setFamily("메이플스토리")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setScaledContents(False)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(130, 60, 81, 101))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("ui/image/KakaoTalk_20191206_212411819.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KU Library"))
        self.pushButton.setText(_translate("MainWindow", "회원 등록"))
        self.pushButton_2.setText(_translate("MainWindow", "회원 조회"))
        self.pushButton_3.setText(_translate("MainWindow", "서적 검색"))
        self.pushButton_4.setText(_translate("MainWindow", "서적 등록"))
        self.label.setText(_translate("MainWindow", "회원 관리"))
        self.label_2.setText(_translate("MainWindow", "서적 관리"))
        self.pushButton_6.setText(_translate("MainWindow", "연체 관리"))
        self.label_10.setText(_translate("MainWindow", "KU Library"))

        self.addBtnListener()

    def btnRegisterClicked(self):
        dialog = QtWidgets.QDialog(self.MainWindow)
        dialog_ui = RegisterDialog(self.dbmanager)
        dialog_ui.setupUi(dialog)
        dialog.setModal(True)
        dialog.show()
        pass

    def btnInqueryUserClicked(self):
        dialog = QtWidgets.QDialog(self.MainWindow)
        dialog_ui = UserInqueryDialog(self.dbmanager)
        dialog_ui.setupUi(dialog)
        dialog.setModal(True)
        dialog.show()
        
        pass

    def btnSearchClicked(self):
        dialog = QtWidgets.QDialog(self.MainWindow)
        dialog_ui = SearchDialog(self.dbmanager)
        dialog_ui.setupUi(dialog)
        dialog.setModal(True)
        dialog.show()
        pass

    def btnBookRegisterClicked(self):
        dialog = QtWidgets.QDialog(self.MainWindow)
        dialog_ui = BookRegisterDialog(self.dbmanager)
        dialog_ui.setupUi(dialog)
        dialog.setModal(True)
        dialog.show()
        pass
    def btnBookRequestClicked(self):
        pass
    
    def btnManageClicked(self):
        dialog = QtWidgets.QDialog(self.MainWindow)
        dialog_ui = OverdueDialog(self.dbmanager)
        dialog_ui.setupUi(dialog)
        dialog.setModal(True)
        dialog.show()

    def addBtnListener(self):
        self.pushButton.clicked.connect(self.btnRegisterClicked) # 회원등록
        self.pushButton_2.clicked.connect(self.btnInqueryUserClicked) # 회원조회
        self.pushButton_3.clicked.connect(self.btnSearchClicked) # 서적검색
        self.pushButton_4.clicked.connect(self.btnBookRegisterClicked) # 서적등록
        self.pushButton_6.clicked.connect(self.btnManageClicked) # 연체 관리

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
