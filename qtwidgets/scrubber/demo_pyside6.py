from PySide6 import QtCore, QtGui, QtWidgets
from qtwidgets import PaletteGrid


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        palette = PaletteGrid('paired12')
        palette.selected.connect(self.show_selected_color)
        self.setCentralWidget(palette)

    def show_selected_color(self, c):
        print("Selected: {}".format(c))


app = QtWidgets.QApplication([])
w = Window()
w.show()
app.exec_()





