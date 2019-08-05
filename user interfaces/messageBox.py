import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import *

error = 1

def window(error):
	app = QApplication(sys.argv)
	w = QWidget()
	b = QPushButton(w)
	b.setText("Show message")
	eMsg = error

	b.move(50, 50)
	b.clicked.connect(showdialog)
	w.setWindowTitle("Dialog")
	w.show()
	sys.exit(app.exec_())

def showdialog(eMsg):
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Warning)
	# todo: implement password policy in error message
	error_msg = ['null data', 'fill empty fields',
	             'invalid email', 'enter a valid email account',
	             'invalid password', 'try again/ reset password',
	             'invalid phone number', 'enter valid phone number']

	msg.setText(error_msg[eMsg])
	# msg.setInformativeText("Additional Information")
	msg.setWindowTitle("Error message")
	msg.setDetailedText(error_msg[eMsg+1])
	msg.setStandardButtons(QMessageBox.Ok)
	msg.buttonClicked.connect(msgbtn)
	retval = msg.exec_()

def msgbtn(i):
	print(i.text())

if __name__ == '__main__':
	window(error)
