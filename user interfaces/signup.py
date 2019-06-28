# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Signup(object):
    def setupUi(self, Signup):
        Signup.setObjectName("Signup")
        Signup.resize(420, 343)
        
        self.emailLineEdit = QtWidgets.QLineEdit(Signup)
        self.emailLineEdit.setGeometry(QtCore.QRect(160, 80, 231, 21))
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.emailLineEdit.setPlaceholderText("Enter your Email address")
        
        self.emailLbl = QtWidgets.QLabel(Signup)
        self.emailLbl.setGeometry(QtCore.QRect(20, 80, 121, 21))
        self.emailLbl.setObjectName("emailLbl")
        
        self.phoneNumLbl = QtWidgets.QLabel(Signup)
        self.phoneNumLbl.setGeometry(QtCore.QRect(20, 120, 121, 21))
        self.phoneNumLbl.setObjectName("phoneNumLbl")
        
        self.phoneNumLineEdit = QtWidgets.QLineEdit(Signup)
        self.phoneNumLineEdit.setGeometry(QtCore.QRect(160, 120, 231, 21))
        self.phoneNumLineEdit.setObjectName("phoneNumLineEdit")
        self.phoneNumLineEdit.setPlaceholderText("Enter your phone number")
        
        self.confirmPwdLbl = QtWidgets.QLabel(Signup)
        self.confirmPwdLbl.setGeometry(QtCore.QRect(20, 230, 131, 21))
        self.confirmPwdLbl.setObjectName("confirmPwdLbl")
        
        self.pwdInputlineEdit = QtWidgets.QLineEdit(Signup)
        self.pwdInputlineEdit.setGeometry(QtCore.QRect(160, 180, 231, 21))
        self.pwdInputlineEdit.setObjectName("pwdInputlineEdit")
        self.pwdInputlineEdit.setPlaceholderText("Enter your password")
        
        self.confirmPwdLineEdit = QtWidgets.QLineEdit(Signup)
        self.confirmPwdLineEdit.setGeometry(QtCore.QRect(160, 230, 231, 21))
        self.confirmPwdLineEdit.setObjectName("confirmPwdLineEdit")
        self.confirmPwdLineEdit.setPlaceholderText("Confirm your password")
        
        self.passwordLbl = QtWidgets.QLabel(Signup)
        self.passwordLbl.setGeometry(QtCore.QRect(20, 180, 121, 21))
        self.passwordLbl.setObjectName("passwordLbl")
        
        self.usernameLbl = QtWidgets.QLabel(Signup)
        self.usernameLbl.setGeometry(QtCore.QRect(20, 40, 121, 21))
        self.usernameLbl.setObjectName("usernameLbl")
        
        self.usernameLnEdit = QtWidgets.QLineEdit(Signup)
        self.usernameLnEdit.setGeometry(QtCore.QRect(160, 40, 231, 21))
        self.usernameLnEdit.setObjectName("usernameLnEdit")
        self.usernameLnEdit.setPlaceholderText("Enter your username")
        
        self.registerBtn = QtWidgets.QPushButton(Signup)
        self.registerBtn.setGeometry(QtCore.QRect(260, 280, 89, 25))
        self.registerBtn.setObjectName("registerBtn")
        
        self.cancelBtn = QtWidgets.QPushButton(Signup)
        self.cancelBtn.setGeometry(QtCore.QRect(150, 280, 89, 25))
        self.cancelBtn.setObjectName("cancelBtn")

        self.retranslateUi(Signup)
        QtCore.QMetaObject.connectSlotsByName(Signup)

    def retranslateUi(self, Signup):
        _translate = QtCore.QCoreApplication.translate
        Signup.setWindowTitle(_translate("Signup", "Dialog"))
        self.emailLbl.setText(_translate("Signup", "Email :"))
        self.phoneNumLbl.setText(_translate("Signup", "Phone number :"))
        self.confirmPwdLbl.setText(_translate("Signup", "Confirm Password :"))
        self.passwordLbl.setText(_translate("Signup", "Password :"))
        self.usernameLbl.setText(_translate("Signup", "Username :"))
        self.registerBtn.setText(_translate("Signup", "Submit"))
        self.cancelBtn.setText(_translate("Signup", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Signup = QtWidgets.QDialog()
    ui = Ui_Signup()
    ui.setupUi(Signup)
    Signup.show()
    sys.exit(app.exec_())

