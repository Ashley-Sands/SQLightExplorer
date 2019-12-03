from PyQt5 import QtCore, QtGui, QtWidgets
import amsql_warning_window
import amsql_text_window

class DialogueWindow:

    DIALOG_STATUS_NONE = 0
    DIALOG_STATUS_ACCEPTED = 1
    DIALOG_STATUS_REJECTED = 2

    def __init__(self):
        self.dialog = None  # Dialog window
        self.app = None     # App class (access to UI elements)
        self.dialogStatus = self.DIALOG_STATUS_NONE

    def new_window(self):
        """ Creates new dialog window, and handles resetting status (do not override)
            Use window function to setup the dialogue window.
         """
        self.reset_status()
        self.window()
        self.set_signals()

    def window(self):
        """ The window to be created """
        pass

    def set_signals(self):
        """ Setup signals"""
        self.dialog.finished.connect( self.dialog_closed )
        QtCore.QMetaObject.connectSlotsByName(self.dialog)

    def reset_status(self):
        """ Resets status"""
        self.dialogStatus = self.DIALOG_STATUS_NONE

    def clear_window(self):
        self.dialog = None
        self.app = None

    def dialog_accepted(self):
        """Signal function for accepted status"""
        print("accepted")
        pass

    def dialog_rejected(self):
        """Signal function for rejected status"""
        print("rejected")
        pass

    def dialog_closed(self, status):

        if status == 0:
            self.dialog_rejected()
        else:
            self.dialog_accepted()

        self.clear_window()
        print("closed status", status)


class DialogueWindow_Warning(DialogueWindow):

    def __init__(self):
        super().__init__()

    def window(self):

        if self.dialog != None:
            return

        # create new dialogue window
        self.dialog = QtWidgets.QDialog()
        self.app = amsql_warning_window.UiWarningDialog()
        self.app.setupUi(self.dialog)
        self.dialog.show()


class DialogueWindow_TextEnter(DialogueWindow):

    def __init__(self):
        super().__init__()

    def window(self):

        if self.dialog != None:
            return

        # create out text input window
        self.dialog = QtWidgets.QDialog()
        self.app = amsql_text_window.UiTextDialog()
        self.app.setupUi(self.dialog)
        self.dialog.show()