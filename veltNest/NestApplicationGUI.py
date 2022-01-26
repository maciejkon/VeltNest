from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ui import test5
from veltNest import VeltNest


class NestApplicationGUI(test5.Ui_MainWindow, QtWidgets.QMainWindow, VeltNest.NestingApp):

    def __init__(self):
        super(NestApplicationGUI, self).__init__()
        self.setupUi(self)
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.context_menu)
        self.model = QtWidgets.QFileSystemModel()
        self.populate()

        self.treeView.clicked.connect(self.show_file_in_window)
        self.treeView.doubleClicked.connect(self.add_file)
        self.confim_button.clicked.connect(self.add_numbers_of_selected_files)
        self.pushButton.clicked.connect(self.start_nest)

    def populate(self):
        path = "C:/Users/macie/PycharmProjects/VeltNest/start"
        self.model.setRootPath((QtCore.QDir.rootPath()))
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(path))
        self.treeView.setSortingEnabled(True)

    def context_menu(self):
        menu = QtWidgets.QMenu()
        add = menu.addAction("Add")
        add.triggered.connect(self.add_file)
        add = menu.addAction("Show")
        add.triggered.connect(self.show_file_in_window)
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())

    def show_file_in_window(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        self.photo_label.setPixmap(QtGui.QPixmap(file_path))

    def add_file(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        if self.check_file_format(file_path):
            self.get_and_parse(file_path)
            QMessageBox.about(self, "Dodanie pliku startowego", "Plik został wybrany")
        else:
            QMessageBox.about(self,"Zły format pliku","Plik musi posiadac rozszerzenie .SVG")

    def add_numbers_of_selected_files(self):
        number = self.textEdit.toPlainText()
        if self.set_number_of_elements(number):
            QMessageBox.about(self, "Dodanie liczby elementów", "Określono liczbę elementów")
        else:
            QMessageBox.about(self, "Zły typ danych", "Musisz wpisać liczbę!")

    def start_nest(self):
        if not self.get_points():
            QMessageBox.about(self, "Wybierz plik startowy", "Nie wybrałeś pliku startowego!")
            return False
        if not self.get_number_of_elements():
            QMessageBox.about(self, "Wybierz Liczbę", "Nie wybrałeś liczby!")
            return False
        else:
            points = self.get_points()
            numberOfElements = self.get_number_of_elements()
            if self.start_app(points, numberOfElements):
                QMessageBox.about(self, "Gotowe!", "Plik znajduje się w folderze end")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    fb = NestApplicationGUI()
    fb.show()
    app.exec_()
