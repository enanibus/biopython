#!/usr/bin/python
# -*- coding: utf-8  -*-

import sys
from PyQt4 import QtCore, QtGui

class MainWindow(QtGui.QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)		

		self.resize(500, 300)
		self.crearAcciones()
		self.crearMenuBar()
		self.crearToolBar()

		cajaDeTexto = QtGui.QTextEdit()
		self.setCentralWidget(cajaDeTexto)

		self.statusBar().showMessage("Hola! soy la barra de estado")		

	def crearAcciones(self):
		icono = QtGui.QIcon("acm.png")
		self.salir = QtGui.QAction(icono,"Salir", self)
		self.salir.setShortcut('Ctrl+Q')
		self.connect(self.salir, QtCore.SIGNAL("triggered()"), QtCore.SLOT("close()"))

	def crearMenuBar(self):
		menubar = self.menuBar()
		file = menubar.addMenu("&Archivo")
		file.addAction(self.salir)
		aaa = menubar.addMenu("Help")
		aaa.addAction("nada")
	
	def crearToolBar(self):
		self.toolbar = self.addToolBar('Salir')
		self.toolbar.addAction(self.salir)
		self.toolbar.setMovable(False)

app = QtGui.QApplication(sys.argv)

main = MainWindow()
main.show()

app.exec_()
