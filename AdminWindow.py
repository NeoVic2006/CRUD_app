from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from AddUserWindow import Ui_AddUser

class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        AdminWindow.setObjectName("AdminWindow")
        AdminWindow.resize(586, 686)
        self.centralwidget = QtWidgets.QWidget(AdminWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(40, 40, 41, 491))
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
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 530, 121, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 0, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 0, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(80, 40, 481, 441))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(6)
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

        self.label_Comments = QtWidgets.QLabel(self.centralwidget)
        self.label_Comments.setGeometry(QtCore.QRect(80, 610, 441, 31))
        self.label_Comments.setObjectName("label_Comments")

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
        self.label.setText(_translate("AdminWindow", "Logged in: "))
        self.label_2.setText(_translate("AdminWindow", "TEMP"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AdminWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AdminWindow", "Phone"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("AdminWindow", "Date of Birth"))
        self.label_Comments.setText(_translate("AdminWindow", "TextLabel"))


    def handle_tabbar_clicked(self, index):
        print(index)
        letter = ["A,B", "C,D", "E,F", "G,H,I", "J,K,L", "M,N,O", "P,Q,R", "S,T,U", "V,W,X", "Y,Z"]
        connection = sqlite3.connect("login.db")
        result = connection.execute(f"""
            with letters(l, r) as (
                select "{letter[index]}", ""
                union all
                select case when instr(l, ",") = 0 then "" else substr(l, instr(l, ",")+1, length(l) - instr(l, ",")) end, case when instr(l, ",") = 0 then l else substr(l, 1, instr(l, ",")-1) end from letters where length(l) > 0
            )
            select c.username, c.phone, c.date_of_birth from clients c where exists (
                select 1 from letters l where length(l.r) > 0 and substr(c.username, 1, length(l.r)) == l.r
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminWindow = QtWidgets.QMainWindow()
    ui = Ui_AdminWindow()
    ui.setupUi(AdminWindow)
    AdminWindow.show()
    sys.exit(app.exec_())
