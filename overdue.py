# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/overdue.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from dbmanager import DBManager

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.dbmanager = DBManager()
        Dialog.setObjectName("Dialog")
        Dialog.resize(975, 692)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 60, 81, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image/out-of-time (1).png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.treeWidget = QtWidgets.QTreeWidget(Dialog)
        self.treeWidget.setGeometry(QtCore.QRect(50, 170, 391, 461))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setBold(True)
        font.setWeight(75)
        self.treeWidget.setFont(font)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget_2 = QtWidgets.QTreeWidget(Dialog)
        self.treeWidget_2.setGeometry(QtCore.QRect(485, 171, 451, 461))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setBold(True)
        font.setWeight(75)
        self.treeWidget_2.setFont(font)
        self.treeWidget_2.setObjectName("treeWidget_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 70, 321, 51))
        font = QtGui.QFont()
        font.setFamily("메이플스토리")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.treeWidget.headerItem().setText(0, _translate("Dialog", "No"))
        self.treeWidget.headerItem().setText(1, _translate("Dialog", "회원 이름"))
        self.treeWidget.headerItem().setText(2, _translate("Dialog", "연체 권수"))
        self.treeWidget_2.headerItem().setText(0, _translate("Dialog", "No"))
        self.treeWidget_2.headerItem().setText(1, _translate("Dialog", "등록 번호"))
        self.treeWidget_2.headerItem().setText(2, _translate("Dialog", "도서 이름"))
        self.treeWidget_2.headerItem().setText(3, _translate("Dialog", "대출 날짜"))
        self.treeWidget_2.headerItem().setText(4, _translate("Dialog", "연체 일수"))
        self.label_2.setText(_translate("Dialog", "회원 별 연체 목록"))

        self.show_user()
        self.show_detail(1)
    def show_user(self):
        result = self.dbmanager.overdue()
        for row in result:
            item = QtWidgets.QTreeWidgetItem(self.treeWidget) 
            item.setText(0, "%s" %row["user_no"])
            item.setText(1,row["user_name"])
            item.setText(2, "%s 권" %row["count"])

    def show_detail(self,user_no):
        result = self.dbmanager.overdue_detail(user_no)
        print(result)
        for row in result:
            item = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
            item.setText(0,str(row["rental_no"]))
            item.setText(1,str(row["book_unique_no"]))
            item.setText(2,row["title"])
            item.setText(3,str(row["rental_date"]))
            item.setText(4,str(row["overdue"]))
            
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
