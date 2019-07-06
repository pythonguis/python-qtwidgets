from PySide2 import QtCore, QtGui, QtWidgets
from gradient import Gradient


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        gradient = Gradient()
        gradient.setGradient([(0, 'black'), (1, 'green'), (0.5, 'red')])
        self.setCentralWidget(gradient)


app = QtWidgets.QApplication([])
w = Window()
w.show()
app.exec_()





