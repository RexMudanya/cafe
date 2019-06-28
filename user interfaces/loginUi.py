# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_startWindow(object):
    def setupUi(self, startWindow):
        startWindow.setObjectName("startWindow")
        startWindow.resize(466, 325)
        self.centralwidget = QtWidgets.QWidget(startWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.usernameLbl = QtWidgets.QLabel(self.centralwidget)
        self.usernameLbl.setGeometry(QtCore.QRect(70, 80, 101, 31))
        self.usernameLbl.setObjectName("usernameLbl")

        self.passwordLbl = QtWidgets.QLabel(self.centralwidget)
        self.passwordLbl.setGeometry(QtCore.QRect(70, 140, 101, 31))
        self.passwordLbl.setObjectName("passwordLbl")

        self.usernameField = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameField.setGeometry(QtCore.QRect(180, 80, 211, 25))
        self.usernameField.setObjectName("usernameField")

        self.passwordField = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordField.setGeometry(QtCore.QRect(180, 140, 211, 25))
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordField.setObjectName("passwordField")

        self.loginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginBtn.setGeometry(QtCore.QRect(200, 190, 89, 25))
        self.loginBtn.setObjectName("loginBtn")

        self.signupBtn = QtWidgets.QPushButton(self.centralwidget)
        self.signupBtn.setGeometry(QtCore.QRect(200, 230, 89, 25))
        self.signupBtn.setObjectName("signupBtn")

        self.pwdRstBtn = QtWidgets.QPushButton(self.centralwidget)
        self.pwdRstBtn.setGeometry(QtCore.QRect(180, 270, 131, 25))
        self.pwdRstBtn.setObjectName("pwdRstBtn")
        
        startWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(startWindow)
        self.statusbar.setObjectName("statusbar")
        startWindow.setStatusBar(self.statusbar)

        self.retranslateUi(startWindow)
        QtCore.QMetaObject.connectSlotsByName(startWindow)

    def retranslateUi(self, startWindow):
        _translate = QtCore.QCoreApplication.translate
        startWindow.setWindowTitle(_translate("startWindow", "MainWindow"))
        self.usernameLbl.setText(_translate("startWindow", "Username :"))
        self.passwordLbl.setText(_translate("startWindow", "Password :"))
        self.loginBtn.setText(_translate("startWindow", "Login"))
        self.signupBtn.setText(_translate("startWindow", "Sign Up"))
        self.pwdRstBtn.setText(_translate("startWindow", "forgot password?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    startWindow = QtWidgets.QMainWindow()
    ui = Ui_startWindow()
    ui.setupUi(startWindow)
    startWindow.show()
    sys.exit(app.exec_())

