# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class SearchDialog(object):
    def __init__(self, dbmanager):
        self.dbmanager = dbmanager
        print("dbmanager 등록")
        print(dbmanager)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(646, 348)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(330, 30, 71, 32))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.treeWidget = QtWidgets.QTreeWidget(Dialog)
        self.treeWidget.setGeometry(QtCore.QRect(30, 80, 601, 221))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.treeWidget.setFont(font)
        self.treeWidget.setObjectName("treeWidget")
        self.label_27 = QtWidgets.QLabel(Dialog)
        self.label_27.setGeometry(QtCore.QRect(30, 30, 32, 32))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.label_27.setFont(font)
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("image/open-book.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 40, 58, 16))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 30, 191, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.txtPage = QtWidgets.QLineEdit(Dialog)
        self.txtPage.setGeometry(QtCore.QRect(280, 308, 51, 21))
        self.txtPage.setObjectName("txtPage")
        self.lbPage = QtWidgets.QLabel(Dialog)
        self.lbPage.setGeometry(QtCore.QRect(340, 310, 58, 16))
        self.lbPage.setObjectName("lbPage")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.addBtnListener()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "조회"))
        self.treeWidget.headerItem().setText(0, _translate("Dialog", "No"))
        self.treeWidget.headerItem().setText(1, _translate("Dialog", "제목"))
        self.treeWidget.headerItem().setText(2, _translate("Dialog", "저자"))
        self.treeWidget.headerItem().setText(3, _translate("Dialog", "출판사"))
        self.treeWidget.headerItem().setText(4, _translate("Dialog", "대출가능 수"))
        self.label.setText(_translate("Dialog", "서적이름"))
        self.txtPage.setText(_translate("Dialog", "1"))
        self.lbPage.setText(_translate("Dialog", "/ 10"))
    
    def btnSearchClicked(self):
        print("asdf")
        title = self.lineEdit.text()
        print("asdf")
        result = self.dbmanager.search_book(title)
        print(result)

    def addBtnListener(self):
        print("af???")
        self.pushButton.clicked.connect(self.btnSearchClicked)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = SearchDialog(None)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
