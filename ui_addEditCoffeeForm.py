# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 300)
        self.l1 = QtWidgets.QLineEdit(parent=Form)
        self.l1.setGeometry(QtCore.QRect(130, 10, 211, 31))
        self.l1.setObjectName("l1")
        self.l2 = QtWidgets.QLineEdit(parent=Form)
        self.l2.setGeometry(QtCore.QRect(130, 50, 211, 31))
        self.l2.setObjectName("l2")
        self.l3 = QtWidgets.QLineEdit(parent=Form)
        self.l3.setGeometry(QtCore.QRect(130, 90, 211, 31))
        self.l3.setObjectName("l3")
        self.l4 = QtWidgets.QLineEdit(parent=Form)
        self.l4.setGeometry(QtCore.QRect(130, 130, 211, 31))
        self.l4.setObjectName("l4")
        self.l5 = QtWidgets.QLineEdit(parent=Form)
        self.l5.setGeometry(QtCore.QRect(130, 170, 211, 31))
        self.l5.setObjectName("l5")
        self.l6 = QtWidgets.QLineEdit(parent=Form)
        self.l6.setGeometry(QtCore.QRect(130, 210, 211, 31))
        self.l6.setObjectName("l6")
        self.saveButton = QtWidgets.QPushButton(parent=Form)
        self.saveButton.setGeometry(QtCore.QRect(10, 250, 331, 41))
        self.saveButton.setObjectName("saveButton")
        self.label_1 = QtWidgets.QLabel(parent=Form)
        self.label_1.setGeometry(QtCore.QRect(10, 10, 111, 31))
        self.label_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 111, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 111, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 111, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 111, 31))
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(10, 210, 111, 31))
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.saveButton.setText(_translate("Form", "Save"))
        self.label_1.setText(_translate("Form", "name"))
        self.label_2.setText(_translate("Form", "roast level"))
        self.label_3.setText(_translate("Form", "ground"))
        self.label_4.setText(_translate("Form", "taste description"))
        self.label_5.setText(_translate("Form", "price"))
        self.label_6.setText(_translate("Form", "package size"))
