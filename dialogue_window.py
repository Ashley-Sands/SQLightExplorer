from PyQt5 import QtCore, QtGui, QtWidgets
import amsql_warning_window


class DialogueWindow:

    def __init__(self):
        self.dialog = None

    def new_warning_window(self):

        if self.dialog != None:
            return

        self.dialog = QtWidgets.QDialog()
        warning_app = amsql_warning_window.UiWarningDialog()
        warning_app.setupUi(self.dialog)
        self.dialog.show()
