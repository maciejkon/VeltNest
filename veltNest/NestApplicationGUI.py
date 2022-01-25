from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QMessageBox

from ui import test5
from veltNest import VeltNest


class NestApplicationGUI(test5.Ui_MainWindow, QtWidgets.QMainWindow, VeltNest.NestingApp):

    def __init__(self):
        super(NestApplicationGUI, self).__init__()
        self.setupUi(self)
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.context_menu)
        self.populate()

        self.treeView.clicked.connect(self.show_file_in_window)
        self.treeView.doubleClicked.connect(self.add_file)
        self.confim_button.clicked.connect(self.add_numbers_of_selected_files)
        self.pushButton.clicked.connect(self.start_nest)


    def populate(self):
        path = "C:/Users/macie/PycharmProjects/VeltNest/start"
        self.model = QtWidgets.QFileSystemModel()
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
        self.get_and_parse(file_path)
        QMessageBox.about(self, "Dodanie pliku startowego", "Plik został wybrany")

    def add_numbers_of_selected_files(self):
        number = self.textEdit.toPlainText()
        self.add_number_of_elements_to_Database(number)
        QMessageBox.about(self, "Dodanie liczby elementów", "Określono liczbę elementów")

    def start_nest(self):
        self.start_app(self.get_points_from_database(), self.get_numberOfElements_from_database())
        QMessageBox.about(self, "Gotowe!", "Plik znajduje się w folderze end")

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    fb = NestApplicationGUI()
    fb.show()
    app.exec_()
