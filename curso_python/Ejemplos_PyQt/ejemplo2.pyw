# -*- coding: utf-8  -*-

import sys
from PyQt4 import QtGui, QtCore

class Main(QtGui.QWidget):
	def __init__(self, parent=None):
		super(Main, self).__init__(parent)		

		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Ejemplo 2')
		self.setWindowIcon(QtGui.QIcon('acm.png'))

		boton = QtGui.QPushButton("Cerrar", self)
		boton.setGeometry(10, 10, 70, 35)
		self.connect(boton, QtCore.SIGNAL("clicked()"),
			 QtCore.SLOT("close()")) 

	def closeEvent(self, event):	
		aviso = QtGui.QMessageBox.question(self, "Salir",
			"Esta seguro de que quiere salir?",
			 QtGui.QMessageBox.Yes, QtGui.QMessageBox.No )
		if aviso == QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()
		
app = QtGui.QApplication(sys.argv)
main = Main()
main.show()
sys.exit(app.exec_())
