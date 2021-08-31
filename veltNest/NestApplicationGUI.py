from PyQt5 import QtCore, QtGui, QtWidgets

from ui import test5
from veltNest import VeltNest

class NestApplicationGUI(test5.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(NestApplicationGUI, self).__init__()
        self.setupUi(self)
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.context_menu)
        self.populate()

        
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
        show = menu.addAction("Show")
        add.triggered.connect(self.add_file)
        show.triggered.connect(self.show_file_in_window)
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())

    def show_file_in_window(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        self.photo_label.setPixmap(QtGui.QPixmap(file_path))

    #tutaj wprowadzamy plik startowy
    def add_file(self):
        print("File Added")

    #zatwierdzamy input z okna liczbowego
    def add_numbers_of_selected_files(self):
        pass

    #funkcja wywołująca nesting
    def start_nest(self):
        pass

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    fb = NestApplicationGUI()
    fb.show()
    app.exec_()
