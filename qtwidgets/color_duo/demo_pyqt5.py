from qtpy import QtWidgets
from qtwidgets.color_duo.color_duo import ColorButton


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        palette = ColorButton()
        palette.colorChanged.connect(self.show_selected_color)
        self.setCentralWidget(palette)

    def show_selected_color(self, c):
        print("Selected: {}".format(c))


app = QtWidgets.QApplication([])
w = Window()
w.show()
app.exec_()





