from PyQt5 import QtCore, QtWidgets
from windows import amsql_text_window, amsql_warning_window, amsql_config_window, amsql_message_window
from global_config import GlobalConfig as Config

class DialogueWindow:

    DIALOG_STATUS_NONE = 0
    DIALOG_STATUS_ACCEPTED = 1
    DIALOG_STATUS_REJECTED = 2

    def __init__(self, callback=None):
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

    def new_window(self):
        """ Creates new dialog window, and handles resetting status (do not override)
            Use window function to setup the dialogue window.
         """
        if not self.can_open_window():
            return

        self.reset_status()
        self.window()
        # insure that dialog windows are always on top :)
        self.dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.dialog.show()
        self.set_signals()

    def window(self):
        """ The window to be created (needs overriding) """
        # There is no need to call show(). this is handled in new window
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
            self.callback(self.callback_data_object(), status)

        print("closed status", status)

    def callback_data_object(self):
        """Data that is sent to the callback as the data_object"""
        return {}

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

    def __init__(self, callback):
        super().__init__(callback)

    def window(self):

        # create new dialogue window
        self.dialog = QtWidgets.QDialog()
        self.app = amsql_warning_window.UiWarningDialog()
        self.app.setupUi(self.dialog)


class DialogueWindow_TextEnter(DialogueWindow):

    def __init__(self, callback):
        super().__init__(callback)
        self.text = ""
        self.standard_buttons = QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Open

    def window(self):

        # create out text input window
        self.dialog = QtWidgets.QDialog()
        self.app = amsql_text_window.UiTextDialog()
        self.app.setupUi(self.dialog)
        self.app.buttons_yes.setStandardButtons( self.standard_buttons )

    def dialog_accepted(self):
        self.text = self.app.text_input.text()
        super().dialog_accepted()
        print("TEXT: ", self.text)

    def callback_data_object(self):
        # uses text for the data object
        return {"text": self.text}

    def set_standard_buttons(self, buttons):
        """ sets the standard buttons to be displayed

        :param buttons:  QtWidgets.QDialogButtonBox | (bitwise or) together
        :return:         None
        """
        self.standard_buttons = buttons


class DialogueWindow_Config( DialogueWindow ):

    def window(self):
        # create new dialogue window
        self.dialog = QtWidgets.QDialog()
        self.app = amsql_config_window.UiConfigDialog()
        self.app.setupUi(self.dialog)
        self.update_inputs()

    def dialog_accepted(self):

        host = self.app.text_host.text()
        port = self.app.text_port.text()
        databases = self.app.text_default_databases.toPlainText()
        timeout = self.app.spinBox_timeout.value()
        host_root = self.app.text_root_dir.text()

        Config.set("host", host)
        Config.set("port", port)
        Config.set("default_db", databases)
        Config.set("connection_timeout", timeout)
        Config.set("remote_root", host_root)

        Config.save_to_file()


    def update_inputs(self):

        host = Config.get("host")
        port = Config.get("port")
        databases = Config.get("default_db")
        timeout = Config.get("connection_timeout")
        host_root = Config.get("remote_root")

        self.app.text_host.setText(str(host))
        self.app.text_port.setText(str(port))
        self.app.text_default_databases.setPlainText(str(databases))
        self.app.spinBox_timeout.setValue(timeout)
        self.app.text_root_dir.setText(host_root)


class DialogueWindow_Message( DialogueWindow ):

    def __int__(self, callback):
        super().__init__(callback)
        self.message = ""

    def window(self):

        # create out text input window
        self.dialog = QtWidgets.QDialog()
        self.app = amsql_message_window.UiMessageDialog()
        self.app.setupUi(self.dialog)
        # set text
        self.app.label.setText( self.get_formatted_message() )

    def get_formatted_message(self):
        formatted_message = "<html><head/><body><p><span style=\" font-size:12pt;\">"
        formatted_message += self.message
        formatted_message += "</span></p></body></html>"

        return formatted_message

    def set_message(self, message):

        self.message = message

        if self.app is not None:
            self.app.label.setText( self.get_formatted_message() )