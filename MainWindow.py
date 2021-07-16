from PasswordRecovery import Ui_Dialog
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from AdminWindow import Ui_AdminWindow
from PyQt5.QtWidgets import QMessageBox
from Usercreation import Ui_Registration


class Ui_MainWindow(object):
    def open_admin_window(self):
        """
        After succesfull login to system this function will close Login Window and open Admin Window
        """
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()


    def sign_Up_window(self):
        """
        After pressing "Registery" button this function is opening UserRegister Window
        """
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Registration()
        self.ui.setupUi(self.window)
        self.window.show()


    def login_Check(self):
        """
        Function to check with DB and see is user can login succesfully  
        """
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        connection = sqlite3.connect("login.db")
        result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?", (username, password))
        if (len(result.fetchall()) >  0 ):               # If User is found in DB
            print("User found!")
            self.open_admin_window()
        else: 
            print("User Not Found!")
            QMessageBox.warning(MainWindow, "Error", "Invalid Username or Password")


    def signUpcheck(self):
        pass


    def setupUi(self, MainWindow):
        """
        Creating Main window with log in screen
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 549)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.ButtonEnter = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonEnter.setGeometry(QtCore.QRect(210, 250, 141, 51))
        self.ButtonEnter.setObjectName("ButtonEnter")

        #------------
        self.ButtonEnter.clicked.connect(self.login_Check)
        #------------       

        self.ButtonRegistery = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonRegistery.setGeometry(QtCore.QRect(370, 250, 141, 51))
        self.ButtonRegistery.setObjectName("ButtonRegistery")

        #------------
        self.ButtonRegistery.clicked.connect(self.sign_Up_window)
        #------------

        self.ButtonCancel = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonCancel.setGeometry(QtCore.QRect(530, 250, 141, 51))
        self.ButtonCancel.setObjectName("ButtonCancel")

        self.checkBox_Rem_my_Username = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Rem_my_Username.setGeometry(QtCore.QRect(290, 330, 311, 17))
        self.checkBox_Rem_my_Username.setObjectName("checkBox_Rem_my_Username")

        self.checkBox_Show_pass = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Show_pass.setGeometry(QtCore.QRect(290, 360, 311, 17))
        self.checkBox_Show_pass.setObjectName("checkBox_Show_pass")

        self.Button_Forgot_pass = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Forgot_pass.setGeometry(QtCore.QRect(290, 390, 171, 21))
        self.Button_Forgot_pass.setObjectName("Button_Forgot_pass")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 140, 461, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 190, 461, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")


        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 21))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")


        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ButtonEnter.setText(_translate("MainWindow", "Enter"))
        self.ButtonRegistery.setText(_translate("MainWindow", "Registery"))
        self.ButtonCancel.setText(_translate("MainWindow", "Cancel"))
        self.checkBox_Rem_my_Username.setText(_translate("MainWindow", "Remeber my Username"))
        self.checkBox_Show_pass.setText(_translate("MainWindow", "Show password "))
        self.Button_Forgot_pass.setText(_translate("MainWindow", "Forgot password?"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create a new file"))
        self.actionSave.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
