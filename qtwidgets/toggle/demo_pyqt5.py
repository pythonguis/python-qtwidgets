import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from toggle import Toggle, AnimatedToggle


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        toggle_1 = Toggle()
        toggle_2 = AnimatedToggle(
            checked_color="#FFB000",
            pulse_checked_color="#44FFB000"
        )

        container = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toggle_1)
        layout.addWidget(toggle_2)
        container.setLayout(layout)

        self.setCentralWidget(container)


app = QtWidgets.QApplication([])
w = Window()
w.show()
app.exec_()




