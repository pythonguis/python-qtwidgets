import sys

from qtpy import QtCore, QtGui, QtWidgets
from qtpy.QtCore import Qt
from qtpy.QtCore import Signal

if 'PyQt5' in sys.modules or 'PyQt6' in sys.modules:
    from . import resources_pyqt

else:
    from . import resources_pyside


class PasswordEdit(QtWidgets.QLineEdit):
    """
    Password LineEdit with icons to show/hide password entries.
    Based on this example https://kushaldas.in/posts/creating-password-input-widget-in-pyqt.html by Kushal Das.
    """

    def __init__(self, show_visibility=True, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.visibleIcon = QtGui.QIcon(":/icons/eye.svg")
        self.hiddenIcon = QtGui.QIcon(":/icons/hidden.svg")

        self.setEchoMode(QtWidgets.QLineEdit.Password)
        
        if show_visibility:
            # Add the password hide/shown toggle at the end of the edit box.
            self.togglepasswordAction = self.addAction(
                self.visibleIcon, 
                QtWidgets.QLineEdit.TrailingPosition
            )
            self.togglepasswordAction.triggered.connect(self.on_toggle_password_Action)

        self.password_shown = False

    def on_toggle_password_Action(self):
        if not self.password_shown:
            self.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.password_shown = True
            self.togglepasswordAction.setIcon(self.hiddenIcon)
        else:
            self.setEchoMode(QtWidgets.QLineEdit.Password)
            self.password_shown = False
            self.togglepasswordAction.setIcon(self.visibleIcon)




