import sys
import sqlite3
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6 import uic


class Program(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.click)
        self.num = 0

    def click(self):
        if self.num < 5:
            self.num += 1
        else:
            self.num = 1
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        res = cur.execute(f'''SELECT * FROM coffees WHERE id == {self.num}''').fetchall()
        self.textBrowser.setText(
            f'<b>{res[0][0]}: {res[0][1]}, {res[0][2]}, {res[0][3]}, {res[0][4]}, {res[0][5]}, {res[0][6]}<b>')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = Program()
    program.show()
    sys.exit(app.exec())
