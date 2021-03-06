from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox


class Ui_AddUser(object):
    def setupUi(self, AddUser):
        AddUser.setObjectName("AddUser")
        AddUser.resize(400, 300)

        self.pushButton_Create_User = QtWidgets.QPushButton(AddUser)
        self.pushButton_Create_User.setGeometry(QtCore.QRect(80, 230, 75, 23))
        self.pushButton_Create_User.setObjectName("pushButton_Create_User")

        #------------
        self.pushButton_Create_User.clicked.connect(self.Adding_User_to_Clients_DB)
        #------------   

        self.pushButton_cancel = QtWidgets.QPushButton(AddUser)
        self.pushButton_cancel.setGeometry(QtCore.QRect(220, 230, 75, 23))
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        #------------
        self.pushButton_cancel.clicked.connect(AddUser.close)    
        #------------

        self.lineEdit_Phone = QtWidgets.QLineEdit(AddUser)
        self.lineEdit_Phone.setGeometry(QtCore.QRect(60, 90, 241, 21))
        self.lineEdit_Phone.setObjectName("lineEdit_Phone")
        self.lineEditUsername = QtWidgets.QLineEdit(AddUser)
        self.lineEditUsername.setGeometry(QtCore.QRect(60, 40, 241, 20))
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.label = QtWidgets.QLabel(AddUser)
        self.label.setGeometry(QtCore.QRect(60, 150, 121, 16))
        self.label.setObjectName("label")
        self.dateEdit = QtWidgets.QDateEdit(AddUser)
        self.dateEdit.setGeometry(QtCore.QRect(190, 140, 110, 31))
        self.dateEdit.setObjectName("dateEdit")

        self.retranslateUi(AddUser)
        QtCore.QMetaObject.connectSlotsByName(AddUser)

    def retranslateUi(self, AddUser):
        _translate = QtCore.QCoreApplication.translate
        AddUser.setWindowTitle(_translate("AddUser", "Dialog"))
        self.pushButton_Create_User.setText(_translate("AddUser", "Create User"))
        self.pushButton_cancel.setText(_translate("AddUser", "Cancel"))
        self.lineEdit_Phone.setPlaceholderText(_translate("AddUser", "Phone Number"))
        self.lineEditUsername.setPlaceholderText(_translate("AddUser", "Username"))
        self.label.setText(_translate("AddUser", "Enter your Bitrhday:"))


    def Adding_User_to_Clients_DB(self):
        """
        Function adding Client to DB, also checking input data for uniqueness
        """
        username = self.lineEditUsername.text()
        phone = self.lineEdit_Phone.text()

        dbt = self.dateEdit.date().toString('yyyy-MM-dd')

        connection = sqlite3.connect("login.db")
        cursor=connection.cursor()
        cursor.execute("SELECT username FROM CLIENTS WHERE username = ? AND phone = ?", (username, phone))
        if item := cursor.fetchone():
            msg = QMessageBox()
            msg.setText("User with same username and phone already exist")
            msg.exec_()
        else:
            connection.execute("INSERT OR IGNORE INTO CLIENTS VALUES(?, ?, ?)", (username, phone, dbt))
            msg = QMessageBox()
            msg.setText("User was added to DB, to refresh users just click on another tab and back!")
            msg.exec_()
        connection.commit()
        connection.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddUser = QtWidgets.QDialog()
    ui = Ui_AddUser()
    ui.setupUi(AddUser)
    AddUser.show()
    sys.exit(app.exec_())

