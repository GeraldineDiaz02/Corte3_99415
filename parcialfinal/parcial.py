from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import sys

class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = loadUi("untitled.ui", self)
        self.show()

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Principal()
    sys.exit(app.exec_())