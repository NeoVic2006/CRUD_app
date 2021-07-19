from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from AddUserWindow import Ui_AddUser
from PyQt5.QtWidgets import QMessageBox
from BirthdayWindow import Ui_BirthdayWindow


class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        AdminWindow.setObjectName("AdminWindow")
        AdminWindow.resize(586, 790)
        self.centralwidget = QtWidgets.QWidget(AdminWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(60, 40, 20, 491))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")

        self.AB = QtWidgets.QWidget()
        self.AB.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AB.setObjectName("AB")
        self.tabWidget.addTab(self.AB, "")
        self.CD = QtWidgets.QWidget()
        self.CD.setObjectName("CD")
        self.tabWidget.addTab(self.CD, "")
        self.EF = QtWidgets.QWidget()
        self.EF.setObjectName("EF")
        self.tabWidget.addTab(self.EF, "")
        self.GHI = QtWidgets.QWidget()
        self.GHI.setObjectName("GHI")
        self.tabWidget.addTab(self.GHI, "")
        self.JKL = QtWidgets.QWidget()
        self.JKL.setObjectName("JKL")
        self.tabWidget.addTab(self.JKL, "")
        self.MNO = QtWidgets.QWidget()
        self.MNO.setObjectName("MNO")
        self.tabWidget.addTab(self.MNO, "")
        self.PQR = QtWidgets.QWidget()
        self.PQR.setObjectName("PQR")
        self.tabWidget.addTab(self.PQR, "")
        self.STU = QtWidgets.QWidget()
        self.STU.setObjectName("STU")
        self.tabWidget.addTab(self.STU, "")
        self.VWX = QtWidgets.QWidget()
        self.VWX.setObjectName("VWX")
        self.tabWidget.addTab(self.VWX, "")
        self.YZ = QtWidgets.QWidget()
        self.YZ.setObjectName("YZ")
        self.tabWidget.addTab(self.YZ, "")

        #------------
        self.tabWidget.tabBarClicked.connect(self.handle_tabbar_clicked)
        #------------

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 530, 121, 51))
        self.pushButton.setObjectName("pushButton")

        #------------
        self.pushButton.clicked.connect(self.Adding_User_to_Admin_DB)
        #------------

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 530, 121, 51))
        self.pushButton_2.setObjectName("pushButton_2")

        #------------
        self.pushButton_2.clicked.connect(self.Update_user)
        #------------
       
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 530, 121, 51))
        self.pushButton_3.setObjectName("pushButton_3")

        #------------
        self.pushButton_3.clicked.connect(self.Delete_user)
        #------------

        font = QtGui.QFont()
        font.setPointSize(11)

        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(80, 40, 481, 441))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(45)

        #------------
        self.tableWidget.itemSelectionChanged.connect(self.Get_user_data_from_table)
        #------------        

        self.label_Comments = QtWidgets.QLabel(self.centralwidget)
        self.label_Comments.setGeometry(QtCore.QRect(80, 610, 441, 31))
        self.label_Comments.setObjectName("label_Comments")

        self.UpdateUserComment = QtWidgets.QLabel(self.centralwidget)
        self.UpdateUserComment.setGeometry(QtCore.QRect(60, 590, 141, 31))
        self.UpdateUserComment.setObjectName("UpdateUserComment")

        self.UpdateUsername = QtWidgets.QLineEdit(self.centralwidget)
        self.UpdateUsername.setGeometry(QtCore.QRect(60, 620, 131, 20))
        self.UpdateUsername.setText("")
        self.UpdateUsername.setPlaceholderText("")
        self.UpdateUsername.setObjectName("UpdateUsername")

        self.UpdatePhone = QtWidgets.QLineEdit(self.centralwidget)
        self.UpdatePhone.setGeometry(QtCore.QRect(60, 650, 131, 20))
        self.UpdatePhone.setText("")
        self.UpdatePhone.setPlaceholderText("")
        self.UpdatePhone.setObjectName("UpdatePhone")

        self.dbtLabel = QtWidgets.QLabel(self.centralwidget)
        self.dbtLabel.setGeometry(QtCore.QRect(60, 690, 61, 16))
        self.dbtLabel.setObjectName("dbtLabel")

        self.dbtDate = QtWidgets.QDateEdit(self.centralwidget)
        self.dbtDate.setGeometry(QtCore.QRect(140, 680, 110, 31))
        self.dbtDate.setObjectName("dbtDate")

        self.pushButton_Done = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Done.setGeometry(QtCore.QRect(280, 680, 91, 31))
        self.pushButton_Done.setObjectName("pushButton_Done")

        #------------
        self.pushButton_Done.clicked.connect(self.done_button_to_update_DB)
        #------------     

        AdminWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 586, 21))
        self.menubar.setObjectName("menubar")
        AdminWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminWindow)
        self.statusbar.setObjectName("statusbar")
        AdminWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AdminWindow)
        self.tabWidget.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(AdminWindow)
        self.birthday_reminder()
        self.handle_tabbar_clicked(0)


    def retranslateUi(self, AdminWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminWindow.setWindowTitle(_translate("AdminWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AB), _translate("AdminWindow", "AB"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CD), _translate("AdminWindow", "CD"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.EF), _translate("AdminWindow", "EF"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.GHI), _translate("AdminWindow", "GHI"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.JKL), _translate("AdminWindow", "JKL"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MNO), _translate("AdminWindow", "MNO"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PQR), _translate("AdminWindow", "PQR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.STU), _translate("AdminWindow", "STU"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.VWX), _translate("AdminWindow", "VWX"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.YZ), _translate("AdminWindow", "YZ"))
        self.pushButton.setText(_translate("AdminWindow", "Add User"))
        self.pushButton_2.setText(_translate("AdminWindow", "Change User"))
        self.pushButton_3.setText(_translate("AdminWindow", "Delete User"))


        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AdminWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AdminWindow", "Phone"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("AdminWindow", "Date of Birth"))
        self.UpdateUserComment.setText(_translate("AdminWindow", "Update User: "))
        self.dbtLabel.setText(_translate("AdminWindow", "Date of Birth:"))
        self.pushButton_Done.setText(_translate("AdminWindow", "Done"))
        


    def handle_tabbar_clicked(self, index):
        """
        Function is making search in DB and showing results when proper TAB is chosen
        """
        letter = ["A,B", "C,D", "E,F", "G,H,I", "J,K,L", "M,N,O", "P,Q,R", "S,T,U", "V,W,X", "Y,Z"]
        connection = sqlite3.connect("login.db")
        result = connection.execute(f"""
            with letters(l, r) as (
                select "{letter[index]}", ""
                union all
                select case when instr(l, ",") = 0 then "" else substr(l, instr(l, ",")+1, length(l) - instr(l, ",")) end, case when instr(l, ",") = 0 then l else substr(l, 1, instr(l, ",")-1) end from letters where length(l) > 0
            )
            select c.username, c.phone, c.date_of_birth from clients c where exists (
                select 1 from letters l where length(l.r) > 0 and substr(lower(c.username), 1, length(l.r)) == lower(l.r)
            )
            """)
        self.tableWidget.setRowCount(0)
        for row_number, roww_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(roww_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.close()
            

    def Adding_User_to_Admin_DB(self):
        """
        Function to open "Add User to Client DB" window 
        """
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AddUser()
        self.ui.setupUi(self.window)
        self.window.show()


    def Get_user_data_from_table(self):
        """
        Function is getting userdata from Table , which we can use for Update or delete functions
        """
        if self.tableWidget.currentRow() == -1:
            msg = QMessageBox()
            msg.setText("You did not choose any User")
            msg.exec_() 
            return "Bad request"
        username = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
        phone = self.tableWidget.item(self.tableWidget.currentRow(), 1).text()
        dbt = self.tableWidget.item(self.tableWidget.currentRow(), 2).text()
        return username, phone, dbt
        
        
    def Update_user(self):
        """
        Function posting fields on the bottom for chosen User
        """
        if self.Get_user_data_from_table() != "Bad request":
            old_username, old_phone, old_dbt = self.Get_user_data_from_table()
            self.UpdateUsername.setText(old_username)
            self.UpdatePhone.setText(old_phone)
    

    def done_button_to_update_DB(self):
        """
        Function Updating DB for chosen User
        """
        old_username, old_phone, old_dbt = self.Get_user_data_from_table()
        new_username = self.UpdateUsername.text()
        new_phone = self.UpdatePhone.text()
        new_dbt = self.dbtDate.date().toString('yyyy-MM-dd')
        connection = sqlite3.connect("login.db")
        cursor=connection.cursor()
        cursor.execute("UPDATE CLIENTS SET username = ?, phone = ?, Date_of_birth = ? WHERE username = ? AND phone = ?", (new_username, new_phone, new_dbt, old_username, old_phone))
        connection.commit()
        connection.close()
        msg = QMessageBox()
        msg.setText("User was Updated! To refresh page just click on another tab and back!")
        msg.exec_() 


    def Delete_user(self):
        """
        Function cheks if User was chosen and removing user from DB. 
        """
        if self.Get_user_data_from_table() != "Bad request":
            username, phone, dbt = self.Get_user_data_from_table()
            connection = sqlite3.connect("login.db")
            cursor=connection.cursor()
            cursor.execute("DELETE FROM CLIENTS WHERE username = ? AND phone = ?", (username, phone))
            connection.commit()
            connection.close()
            msg = QMessageBox()
            msg.setText("User was Deleted! To refresh page just click on another tab and back!")
            msg.exec_() 


    def birthday_reminder(self):
        """
        Function starts reminder window
        """
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_BirthdayWindow()
        self.ui.setupUi(self.window)
        self.window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.window.show()

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminWindow = QtWidgets.QMainWindow()
    ui = Ui_AdminWindow()
    ui.setupUi(AdminWindow)
    AdminWindow.show()
    sys.exit(app.exec_())
