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

        self.reset_status()
        self.set_signals()

    def set_signals(self):
        self.app.button_yes.accepted.connect( self.dialog_accepted() )
        self.app.button_yes.rejected.connect( self.dialog_rejected() )

    def reset_status(self):
        self.dialog = None
        self.app = None
        self.dialogStatus = self.DIALOG_STATUS_NONE

    def dialog_accepted(self):

        self.dialog = None
        pass

    def dialogu_rejected(self):

        self.dialog = None
        pass


class DialogueWindow_Warning(DialogueWindow):

    def __init__(self):
        super().__init__()
        self.text = ""

    def new_window(self):

        if self.dialog != None:
            return

        super().new_window()

        # create new dialogue window
        self.dialog = QtWidgets.QDialog()
        self.app = amsql_warning_window.UiWarningDialog()
        self.app.setupUi(self.dialog)
        self.dialog.show()

class DialogueWindow_TextEnter(DialogueWindow):

    def __init__(self):
        super().__init__()

    def new_window(self):

        if self.dialog != None:
            return

        super().new_window()

        # create out text input window
        self.dialog = QtWidgets.QDialog()
        self.app = amsql_text_window.UiTextDialog()
        self.app.setupUi(self.dialog)
        self.dialog.show()