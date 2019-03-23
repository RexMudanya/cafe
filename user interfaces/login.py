'''
window for client login to system
email + password login
'''
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import sys

class LoginWindow(QMainWindow):
    """docstring for Window"""
    def __init__(self):
        super().__init__()
        
        self.title = "Client Login"
        self.top = 400
        self.left= 200
        self.width= 500
        self.height=500
        #self.setWindowIcon(QtGui.QIcon("icon.jpg"))

        name_label =  QLabel("Username: ", self)
        #name_label.move(200,200)       
        name_label.setGeometry(80,50,101,31)

        pwd_label = QLabel("Password: ", self)
        pwd_label.setGeometry(80,110,101,31)

        login_btn = QPushButton("Login", self)
        login_btn.setGeometry(300, 210, 89, 25)

        self.InitUI()

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

App = QApplication(sys.argv)
window = LoginWindow()
sys.exit(App.exec())