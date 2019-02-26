import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(600,300)
		
		self.label_name = QtWidgets.QLabel(Dialog)
		self.label_name.setGeometry(QtCore.QRect(53,50,91,16))
		self.label_name.setObjectName("Name_label")

		self.label_pwd = QtWidgets.QLabel(Dialog)
		self.label_pwd.setGeometry(QtCore.QRect(60,80,71,16))
		self.label_pwd.setObjectName("Password_label")

		self.loginButton = QtWidgets.QPushButton(Dialog)
		self.loginButton.setGeometry(QtCore.QRect(150, 240, 81, 23))
		self.loginButton.setObjectName("loginButton")

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

		def retranslateUi(self,Dialog):
			_translate = QtCore>QCoreApplication.translate
			Dialog.setWindowTitle(_translate("Dialog","Login Screen"))


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	Dialog = QtWidgets.QDialog()
	ui = ui_Dialog()
	ui.setupUi(Dialog)
	Dialog.show()
	sys.exit(app.exec_())