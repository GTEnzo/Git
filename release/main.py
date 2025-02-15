import sys
import sqlite3
from ui_main import Ui_MainWindow
from ui_addEditCoffeeForm import Ui_Form
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QDialog, QLineEdit, QPushButton


class CoffeeApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load()
        self.addButton.clicked.connect(self.add)
        self.tableWidget.itemDoubleClicked.connect(self.edit)

    def load(self):
        con = sqlite3.connect('data/coffee.sqlite')
        cur = con.cursor()
        cur.execute("SELECT * FROM coffee")
        rows = cur.fetchall()
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(len(rows[0]) if rows else 0)
        for row_index, row_data in enumerate(rows):
            for column_index, item in enumerate(row_data):
                self.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(item)))
        con.close()

    def add(self):
        dialog = AddEditCoffeeDialog(self)
        if dialog.exec() == QDialog.accepted:
            self.load_data()

    def edit(self, item):
        row = item.row()
        coffee_id_item = self.tableWidget.item(row, -1)
        name_item = self.tableWidget.item(row, 0)
        roast_level_item = self.tableWidget.item(row, 1)
        ground_item = self.tableWidget.item(row, 2)
        taste_description_item = self.tableWidget.item(row, 3)
        price_item = self.tableWidget.item(row, 4)
        package_size_item = self.tableWidget.item(row, 5)

        coffee_id = coffee_id_item.text() if coffee_id_item else ''
        name = name_item.text() if name_item else ''
        roast_level = roast_level_item.text() if roast_level_item else ''
        ground = ground_item.text() if ground_item else ''
        taste_description = taste_description_item.text() if taste_description_item else ''
        price = price_item.text() if price_item else ''
        package_size = package_size_item.text() if package_size_item else ''

        dialog = AddEditCoffeeDialog(self, coffee_id, name, roast_level, ground, taste_description, price, package_size)
        if dialog.exec() == QDialog.accepted:
            self.load()


class AddEditCoffeeDialog(QDialog, Ui_Form):
    def __init__(self, parent=None, coffee_id=None, name='', roast_level='', ground='', taste_description='', price='',
                 package_size=''):
        super().__init__(parent)
        self.setupUi(self)

        self.parent = parent
        self.coffee_id = coffee_id

        self.name_input = self.findChild(QLineEdit, 'l1')
        self.roast_level_input = self.findChild(QLineEdit, 'l2')
        self.ground_input = self.findChild(QLineEdit, 'l3')
        self.taste_description_input = self.findChild(QLineEdit, 'l4')
        self.price_input = self.findChild(QLineEdit, 'l5')
        self.package_size_input = self.findChild(QLineEdit, 'l6')

        self.save_button = self.findChild(QPushButton, 'saveButton')

        self.name_input.setText(name)
        self.roast_level_input.setText(roast_level)
        self.ground_input.setText(ground)
        self.taste_description_input.setText(taste_description)
        self.price_input.setText(price)
        self.package_size_input.setText(package_size)

        self.save_button.clicked.connect(self.save)

    def save(self):
        name = self.name_input.text()
        roast_level = self.roast_level_input.text()
        ground = self.ground_input.text()
        taste_description = self.taste_description_input.text()
        price = self.price_input.text()
        package_size = self.package_size_input.text()

        con = sqlite3.connect('data/coffee.sqlite')
        cur = con.cursor()
        if self.coffee_id:
            cur.execute(
                "UPDATE coffee SET name=?, roast_level=?, ground=?, taste_description=?, price=?, package_size=? WHERE id=?",
                (name, roast_level, ground, taste_description, price, package_size, self.coffee_id))
        else:
            cur.execute(
                "INSERT INTO coffee (name, roast_level, ground, taste_description, price, package_size) VALUES (?, ?, ?, ?, ?, ?)",
                (name, roast_level, ground, taste_description, price, package_size))
        con.commit()
        con.close()
        self.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())
