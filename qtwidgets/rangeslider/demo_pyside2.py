from PySide2 import QtCore, QtGui, QtWidgets
from qtwidgets import RangeSlider


app = QtWidgets.QApplication([])

slider = RangeSlider()
slider.show()

app.exec_()
