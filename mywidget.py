from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication
import sys

class MainWidget(QWidget):
    btnNo = 0
    def __init__(self, MainWindow):
        QWidget.__init__(self, flags=Qt.Widget)
        MainWindow.resize(500,600)
        self.MainWindow = MainWindow
        self.setupUi()
        self.mywidgets = []

    def createWidget(self):
        widget = QtWidgets.QLabel(self)
        widget.setText("created %d" % self.btnNo)
        widget.setGeometry(QtCore.QRect(0, len(self.mywidgets)*30, 40, 30))
        self.mywidgets.append(widget)
        print(widget)
        # mywidget = MyWidget(self)
        # mywidget.setGeometry(QtCore.QRect(10,len(self.mywidgets)*80, 300,80))
        # self.mywidgets.append(mywidget)
        # self.repaint()
        # print(self.mywidgets)

    def setupUi(self):

        self.button = QtWidgets.QPushButton(self);
        self.button.setGeometry(QtCore.QRect(0,0,50,30))
        self.button.setText("버튼")
        self.button.clicked.connect(self.createWidget)
        # self.layout.addWidget(self.button)
        pass
    
class MyWidget(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent=parent, flags=Qt.Widget)
        # self.setLayout(None)
        # self.resize(300,500)

        self.setStyleSheet("Background-color:#fff")
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("dktlqkf")
        self.label1.setGeometry(QtCore.QRect(0, 0, 300, 50))
        self.label1.setObjectName("Label1")
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setObjectName("Label2")
        self.label2.setText("dpd?")
        self.label2.setGeometry(QtCore.QRect(0, 90, 300, 40))
        self.label2.setStyleSheet("color:#ff0000")
        

class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.resize(600,500)

        self.mywidget = MyWidget(self)
        self.mywidget.setStyleSheet("background-color:#abcdab;border:1px solid red;")
        self.mywidget.setObjectName("mywidget")
        self.mywidget.setGeometry(QtCore.QRect(10,90, 300,900))
        # self.widget.setGeometry(QtCore.QRect(40, 40, 171, 111))
        # self.widget.setObjectName("widget")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QtWidgets.QMainWindow()
    form.setCentralWidget(MainWidget(form))
    form.show()
    exit(app.exec_())