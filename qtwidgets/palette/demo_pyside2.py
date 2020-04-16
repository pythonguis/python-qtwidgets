from PySide2 import QtCore, QtGui, QtWidgets
from qtwidgets import PaletteGrid, PaletteHorizontal, PaletteVertical


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        palette = PaletteGrid('17undertones') # or PaletteHorizontal, or PaletteVertical
        palette.selected.connect(self.show_selected_color)
        self.setCentralWidget(palette)

    def show_selected_color(self, c):
        print("Selected: {}".format(c))


app = QtWidgets.QApplication([])
w = Window()
w.show()
app.exec_()





