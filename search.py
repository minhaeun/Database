# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setUserid(self, userid):
        self.userid = userid
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(635, 343)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 10, 191, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_22 = QtWidgets.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(350, 300, 30, 30))
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(320, 10, 71, 32))
        self.pushButton.setObjectName("pushButton")
        self.pagePrev1_13 = QtWidgets.QLabel(Dialog)
        self.pagePrev1_13.setGeometry(QtCore.QRect(340, 290, 50, 50))
        self.pagePrev1_13.setText("")
        self.pagePrev1_13.setPixmap(QtGui.QPixmap("image/square.png"))
        self.pagePrev1_13.setScaledContents(True)
        self.pagePrev1_13.setObjectName("pagePrev1_13")
        self.label_23 = QtWidgets.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(250, 300, 30, 30))
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.pagePrev1_9 = QtWidgets.QLabel(Dialog)
        self.pagePrev1_9.setGeometry(QtCore.QRect(290, 290, 50, 50))
        self.pagePrev1_9.setText("")
        self.pagePrev1_9.setPixmap(QtGui.QPixmap("image/square.png"))
        self.pagePrev1_9.setScaledContents(True)
        self.pagePrev1_9.setObjectName("pagePrev1_9")
        self.label_24 = QtWidgets.QLabel(Dialog)
        self.label_24.setGeometry(QtCore.QRect(300, 300, 30, 30))
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.label_26 = QtWidgets.QLabel(Dialog)
        self.label_26.setGeometry(QtCore.QRect(400, 300, 30, 30))
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(200, 300, 30, 30))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 20, 58, 16))
        self.label.setObjectName("label")
        self.pagePrev1_2 = QtWidgets.QLabel(Dialog)
        self.pagePrev1_2.setGeometry(QtCore.QRect(190, 290, 50, 50))
        self.pagePrev1_2.setText("")
        self.pagePrev1_2.setPixmap(QtGui.QPixmap("image/square.png"))
        self.pagePrev1_2.setScaledContents(True)
        self.pagePrev1_2.setObjectName("pagePrev1_2")
        self.label_27 = QtWidgets.QLabel(Dialog)
        self.label_27.setGeometry(QtCore.QRect(20, 10, 32, 32))
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("image/open-book.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.treeWidget = QtWidgets.QTreeWidget(Dialog)
        self.treeWidget.setGeometry(QtCore.QRect(20, 60, 601, 221))
        self.treeWidget.setObjectName("treeWidget")
        self.pagePrev1_12 = QtWidgets.QLabel(Dialog)
        self.pagePrev1_12.setGeometry(QtCore.QRect(240, 290, 50, 50))
        self.pagePrev1_12.setText("")
        self.pagePrev1_12.setPixmap(QtGui.QPixmap("image/square.png"))
        self.pagePrev1_12.setScaledContents(True)
        self.pagePrev1_12.setObjectName("pagePrev1_12")
        self.pagePrev1_11 = QtWidgets.QLabel(Dialog)
        self.pagePrev1_11.setGeometry(QtCore.QRect(390, 290, 50, 50))
        self.pagePrev1_11.setText("")
        self.pagePrev1_11.setPixmap(QtGui.QPixmap("image/square.png"))
        self.pagePrev1_11.setScaledContents(True)
        self.pagePrev1_11.setObjectName("pagePrev1_11")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_22.setText(_translate("Dialog", "3"))
        self.pushButton.setText(_translate("Dialog", "조회"))
        self.label_23.setText(_translate("Dialog", "1"))
        self.label_24.setText(_translate("Dialog", "2"))
        self.label_26.setText(_translate("Dialog", ">"))
        self.label_14.setText(_translate("Dialog", "<"))
        self.label.setText(_translate("Dialog", "서적이름"))
        self.treeWidget.headerItem().setText(0, _translate("Dialog", "No"))
        self.treeWidget.headerItem().setText(1, _translate("Dialog", "제목"))
        self.treeWidget.headerItem().setText(2, _translate("Dialog", "저자"))
        self.treeWidget.headerItem().setText(3, _translate("Dialog", "출판사"))
        self.treeWidget.headerItem().setText(4, _translate("Dialog", "대출가능 수"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
