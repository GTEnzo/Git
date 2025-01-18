import sys
import random
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(500, 500)
        self.btn = QtWidgets.QPushButton(parent=Form)
        self.btn.setGeometry(QtCore.QRect(10, 10, 481, 28))
        self.btn.setObjectName("btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn.setText(_translate("Form", "Push me"))


class Program(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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
        num = random.randint(10, 400)
        qp.setBrush(QColor(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
        qp.drawEllipse(250 - num // 2, 250 - num // 2, num, num)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = Program()
    program.show()
    sys.exit(app.exec())
