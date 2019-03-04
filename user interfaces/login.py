from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Window(QMainWindow):
	"""docstring for Window"""
	def __init__(self):
		super().__init__()
		
		self.title = "Client Login"
		self.top = 400
		self.left= 200
		self.width= 500
		self.height=500
		#self.setWindowIcon(QtGui.QIcon("icon.jpg"))

		self.InitUI()

	def InitUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
