import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QColor


class Program(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.click)
        self.flag = False

    def click(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.flag = False

    def draw(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        num = random.randint(10, 250)
        qp.drawEllipse(250 - num // 2, 250 - num // 2, num, num)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = Program()
    program.show()
    sys.exit(app.exec())
