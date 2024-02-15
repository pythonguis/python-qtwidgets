import os
import sys

from qtpy import QtCore, QtGui, QtWidgets
from qtpy.QtCore import Qt, Signal

folder = os.path.dirname(__file__)


class PasswordEdit(QtWidgets.QLineEdit):
    """
    Password LineEdit with icons to show/hide password entries.
    Based on this example https://kushaldas.in/posts/creating-password-input-widget-in-pyqt.html by Kushal Das.
    """

    def __init__(
        self,
        show_visibility=True,
        visible_icon=None,
        hidden_icon=None,
        icons_from_theme=True,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)

        if icons_from_theme:
            self.visibleIcon = QtGui.QIcon.fromTheme("view-visible")
            self.hiddenIcon = QtGui.QIcon.fromTheme("view-hidden")
        else:
            if visible_icon:
                self.visibleIcon = visible_icon
            else:
                self.visibleIcon = QtGui.QIcon(os.path.join(folder, "eye.svg"))
            if hidden_icon:
                self.hiddenIcon = hidden_icon
            else:
                self.hiddenIcon = QtGui.QIcon(
                    os.path.join(folder, "hidden.svg")
                )

        self.setEchoMode(QtWidgets.QLineEdit.Password)

        if show_visibility:
            # Add the password hide/shown toggle at the end of the edit box.
            self.togglepasswordAction = self.addAction(
                self.visibleIcon, QtWidgets.QLineEdit.TrailingPosition
            )
            self.togglepasswordAction.triggered.connect(
                self.on_toggle_password_Action
            )

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
