import sys
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6 import uic


class Program(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.click)

    def click(self):
        print('ok')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = Program()
    program.show()
    sys.exit(app.exec())
