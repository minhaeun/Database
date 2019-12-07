# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1643, 834)
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
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(280, 310, 91, 22))
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setTickInterval(1000)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(300, 330, 58, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

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
        self.label_2.setText(_translate("Dialog", "1 / 1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
