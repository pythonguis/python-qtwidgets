from PySide2 import QtCore, QtGui, QtWidgets
from qtwidgets import Paint


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        paint = Paint(300, 300)
        paint.setPenWidth(5)
        paint.setPenColor('#EB5160')
        self.setCentralWidget(paint)


app = QtWidgets.QApplication([])
w = Window()
w.show()
app.exec_()





