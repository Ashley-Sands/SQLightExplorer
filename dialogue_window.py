from PyQt5 import QtCore, QtWidgets
from windows import amsql_text_window, amsql_warning_window, amsql_config_window
from global_config import GlobalConfig as Config

class DialogueWindow:

    DIALOG_STATUS_NONE = 0
    DIALOG_STATUS_ACCEPTED = 1
    DIALOG_STATUS_REJECTED = 2

    def __init__(self, name, callback=None):
        self.name = name
        self.dialog = None  # Dialog window
        self.app = None     # App class (access to UI elements)
        self.dialogStatus = self.DIALOG_STATUS_NONE
        self.dialog_windows = {}
        self.callback = callback

    def set_dialog_windows(self, dialog_dict):
        """ sets dialog window classes. (will overwrite)
        :param dialog_dict:     dict of all dialogue windows (use to prevent opening multiple dialog windows)
                                (can include self)
        """
        self.dialog_windows = dialog_dict

    def set_name(self, name):
        self.name = name

    def new_window(self):
        """ Creates new dialog window, and handles resetting status (do not override)
            Use window function to setup the dialogue window.
         """
        if not self.can_open_window():
            return

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

        if self.callback is not None:
            self.callback(self.name, status)

        print("closed status", status)

    def is_open(self):
        """returns dialogue open status"""
        return self.dialog != None

    def can_open_window(self):
        """ check to see if any dialogue windows are active (including self)

        :return:
        """
        if self.is_open():
            return False

        for k in self.dialog_windows:
            if self.dialog_windows[k].is_open():
                return False

        return True


class DialogueWindow_Warning(DialogueWindow):

    def __init__(self, name, callback):
        super().__init__(name, callback)

    def window(self):

        # create new dialogue window
        self.dialog = QtWidgets.QDialog()
        self.app = amsql_warning_window.UiWarningDialog()
        self.app.setupUi(self.dialog)
        self.dialog.show()

    def dialog_accepted(self):
        super().dialog_accepted()


class DialogueWindow_TextEnter(DialogueWindow):

    def __init__(self, name, callback):
        super().__init__(name, callback)
        self.text = ""

    def window(self):

        # create out text input window
        self.dialog = QtWidgets.QDialog()
        self.app = amsql_text_window.UiTextDialog()
        self.app.setupUi(self.dialog)
        self.dialog.show()

    def dialog_accepted(self):
        self.text = self.app.text_input.text()
        super().dialog_accepted()
        print("TEXT: ", self.text)


class DialogueWindow_Config( DialogueWindow ):

    def window(self):
        # create new dialogue window
        self.dialog = QtWidgets.QDialog()
        self.app = amsql_config_window.UiConfigDialog()
        self.app.setupUi(self.dialog)
        self.update_inputs()
        self.dialog.show()

    def dialog_accepted(self):
        host = self.app.text_host.text()
        port = self.app.text_port.text()

        Config.set("host", host)
        Config.set("port", port)

    def update_inputs(self):

        host = Config.get("host")
        port = Config.get("port")

        self.app.text_host.setText(host)
        self.app.text_port.setText(port)