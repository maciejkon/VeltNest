
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 430, 191, 61))
        self.pushButton.setObjectName("pushButton")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(420, 360, 61, 31))
        self.textEdit.setObjectName("textEdit")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 360, 101, 31))
        self.label.setObjectName("label")

        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(70, 160, 411, 192))
        self.treeView.setObjectName("treeView")
        self.treeView.header().setVisible(True)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 60, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(29)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 130, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.photo_label = QtWidgets.QLabel(self.centralwidget)
        self.photo_label.setGeometry(QtCore.QRect(500, 160, 231, 191))
        self.photo_label.setFrameShape(QtWidgets.QFrame.Box)
        self.photo_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.photo_label.setText("")
        self.confim_button = QtWidgets.QPushButton(self.centralwidget)
        self.confim_button.setGeometry(QtCore.QRect(500, 360, 175, 31))
        self.confim_button.setObjectName("confim_button")
        #self.photo_label.setPixmap(QtGui.QPixmap("../b????d 1.png"))
        self.photo_label.setScaledContents(True)
        self.photo_label.setObjectName("photo_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.pushButton.setText(_translate("MainWindow", "Nest!"))
        self.label.setText(_translate("MainWindow", "Ilo???? element??w:"))
        self.label_2.setText(_translate("MainWindow", "VeltNest!"))
        self.label_3.setText(_translate("MainWindow", "Wybierz plik startowy:"))
        self.confim_button.setText(_translate("MainWindow", "Number of elements"))




