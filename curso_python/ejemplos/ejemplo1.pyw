import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.resize(300,200)
widget.setWindowTitle("Hola Mundo")
widget.show()

app.exec_()
