from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_BirthdayWindow(object):
    def setupUi(self, BirthdayWindow):
        BirthdayWindow.setObjectName("BirthdayWindow")
        BirthdayWindow.resize(454, 482)

        self.tableWidgetBirthDays = QtWidgets.QTableWidget(BirthdayWindow)
        self.tableWidgetBirthDays.setGeometry(QtCore.QRect(60, 60, 331, 331))
        self.tableWidgetBirthDays.setRowCount(10)
        self.tableWidgetBirthDays.setColumnCount(2)
        self.tableWidgetBirthDays.setObjectName("tableWidgetBirthDays")

        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBirthDays.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBirthDays.setHorizontalHeaderItem(1, item)
        self.tableWidgetBirthDays.horizontalHeader().setVisible(True)
        self.tableWidgetBirthDays.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidgetBirthDays.horizontalHeader().setMinimumSectionSize(45)
        self.labelBirthday = QtWidgets.QLabel(BirthdayWindow)
        self.labelBirthday.setGeometry(QtCore.QRect(70, 20, 301, 21))
        self.labelBirthday.setObjectName("labelBirthday")
        self.pushButton = QtWidgets.QPushButton(BirthdayWindow)
        self.pushButton.setGeometry(QtCore.QRect(170, 420, 121, 41))
        self.pushButton.setObjectName("pushButton")


        connection = sqlite3.connect("login.db")
        result = connection.execute("SELECT username, date('now') - Date_of_birth FROM CLIENTS")

        # solution for MySQL === ("SELECT username, Date_of_birth From CLIENTS WHERE DATEDIFF(DAY, Date_of_birth, SysDateTime())%365 < 7")
        self.tableWidgetBirthDays.setRowCount(0)
        for row_number, roww_data in enumerate(result):
            self.tableWidgetBirthDays.insertRow(row_number)
            for column_number, data in enumerate(roww_data):
                self.tableWidgetBirthDays.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.close()


        self.retranslateUi(BirthdayWindow)
        QtCore.QMetaObject.connectSlotsByName(BirthdayWindow)

        
    def retranslateUi(self, BirthdayWindow):
        _translate = QtCore.QCoreApplication.translate
        BirthdayWindow.setWindowTitle(_translate("BirthdayWindow", "Dialog"))
        item = self.tableWidgetBirthDays.horizontalHeaderItem(0)
        item.setText(_translate("BirthdayWindow", "Name"))
        item = self.tableWidgetBirthDays.horizontalHeaderItem(1)
        item.setText(_translate("BirthdayWindow", "Date of Birth"))
        self.labelBirthday.setText(_translate("BirthdayWindow", "On this week those Users have birthdays:"))
        self.pushButton.setText(_translate("BirthdayWindow", "Okay"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BirthdayWindow = QtWidgets.QDialog()
    ui = Ui_BirthdayWindow()
    ui.setupUi(BirthdayWindow)
    BirthdayWindow.show()
    sys.exit(app.exec_())
