import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.resize(600,200)
widget.setWindowTitle("Ejsaasemplo")
widget.show()

app.exec_()
