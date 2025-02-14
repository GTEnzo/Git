import sys
import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        cur.execute("SELECT * FROM coffee")
        rows = cur.fetchall()
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(len(rows[0]) if rows else 0)
        for row_index, row_data in enumerate(rows):
            for column_index, item in enumerate(row_data):
                self.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(item)))
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())
