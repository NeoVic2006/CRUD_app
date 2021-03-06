from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)

        self.pushButonChangPass = QtWidgets.QPushButton(Dialog)
        self.pushButonChangPass.setGeometry(QtCore.QRect(80, 160, 111, 23))
        self.pushButonChangPass.setObjectName("pushButonChangPass")

        #------------
        self.pushButonChangPass.clicked.connect(self.Email_send_button)
        #------------ 
        

        self.pushButtonCancel = QtWidgets.QPushButton(Dialog)
        self.pushButtonCancel.setGeometry(QtCore.QRect(230, 160, 75, 23))
        self.pushButtonCancel.setObjectName("pushButtonCancel")

        #------------
        self.pushButtonCancel.clicked.connect(Dialog.close)
        #------------ 

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(80, 90, 221, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButonChangPass.setText(_translate("Dialog", "Change password"))
        self.pushButtonCancel.setText(_translate("Dialog", "Cancel"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Enter your email"))


    def Email_send_button(self):
        msg = QMessageBox()
        msg.setText("Email with password recovery was send!")
        msg.exec_() 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
