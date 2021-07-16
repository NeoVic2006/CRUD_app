from sqlite3.dbapi2 import connect
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox

class Ui_Registration(object):
    def Insert_Data_In_DB(self):
        username = self.lineEditUsername.text()
        password = self.lineEdit_2.text()
        confirm_password = self.lineEdit_3.text()
        dbt = self.dateEdit.text()
        if password == confirm_password:
            connection = sqlite3.connect("login.db")
            connection.execute("INSERT INTO USERS VALUES(?, ?, ?)", (username, password, dbt))
            connection.commit()
            connection.close()
            #QMessageBox.warning(Registration, "Error", "User was created succesfully!")
            print("User was created succesfully!")
        else:
            #QMessageBox.warning(MainWindow, "Error", "The password and confirmation password do not match. Try again.")
            print("The password and confirmation password do not match. Try again.")


    def setupUi(self, Registration):
        Registration.setObjectName("Registration")
        Registration.resize(400, 300)
        self.pushButtonRegCreate = QtWidgets.QPushButton(Registration)
        self.pushButtonRegCreate.setGeometry(QtCore.QRect(110, 230, 75, 23))
        self.pushButtonRegCreate.setObjectName("pushButtonRegCreate")

        #------------
        self.pushButtonRegCreate.clicked.connect(self.Insert_Data_In_DB)
        #------------    

        self.pushButtonRegCancel = QtWidgets.QPushButton(Registration)
        self.pushButtonRegCancel.setGeometry(QtCore.QRect(200, 230, 75, 23))
        self.pushButtonRegCancel.setObjectName("pushButtonRegCancel")
        self.lineEditUsername = QtWidgets.QLineEdit(Registration)
        self.lineEditUsername.setGeometry(QtCore.QRect(70, 40, 241, 21))
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.lineEdit_2 = QtWidgets.QLineEdit(Registration)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 90, 241, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Registration)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 140, 241, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.dateEdit = QtWidgets.QDateEdit(Registration)
        self.dateEdit.setGeometry(QtCore.QRect(200, 180, 110, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(Registration)
        self.label.setGeometry(QtCore.QRect(70, 190, 121, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Registration)
        QtCore.QMetaObject.connectSlotsByName(Registration)

    def retranslateUi(self, Registration):
        _translate = QtCore.QCoreApplication.translate
        Registration.setWindowTitle(_translate("Registration", "Dialog"))
        self.pushButtonRegCreate.setText(_translate("Registration", "Create"))
        self.pushButtonRegCancel.setText(_translate("Registration", "Cancel"))
        self.lineEditUsername.setPlaceholderText(_translate("Registration", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Registration", "Password"))
        self.lineEdit_3.setPlaceholderText(_translate("Registration", "Repeat password"))
        self.label.setText(_translate("Registration", "Enter your Bitrhday:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Registration = QtWidgets.QDialog()
    ui = Ui_Registration()
    ui.setupUi(Registration)
    Registration.show()
    sys.exit(app.exec_())
