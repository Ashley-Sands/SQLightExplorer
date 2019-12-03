import amsql_viewer_ui
import ui_helpers
import global_config
from ui_tab_table import ui_tabTable
from ui_tree_view import UiTreeView
from dialogue_window import DialogueWindow_Warning, DialogueWindow_TextEnter

dialogs = {}

# create our dialogue instances
dialogs["drop_table"] = DialogueWindow_Warning()
dialogs["new_database"] = DialogueWindow_TextEnter()
dialogs["open_database"] = DialogueWindow_TextEnter()

# set dict of dialogues in each dialogue instance to prevent multiple windows from being opened
dialogs["drop_table"].set_dialog_windows(dialogs)
dialogs["new_database"].set_dialog_windows(dialogs)
dialogs["open_database"].set_dialog_windows(dialogs)

if __name__ == "__main__":
    import amsql_config  # setups default config.
    import sys
    import amsql_config
    from PyQt5 import QtCore, QtGui, QtWidgets

    print(global_config.GlobalConfig.get("port"))

    # start the QApp
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    main_app = amsql_viewer_ui.Ui_MainWindow()
    main_app.setupUi(MainWindow)

    # Add the welcome tab
    main_app.welcome_tab()

    # Setup the classes to manage the UI elements :)
    ui_tab_table = ui_tabTable( main_app.tab_view )
    ui_tree_view = UiTreeView(main_app.treeWidget, ui_tab_table)

    main_app.button_drop_table.clicked.connect(dialogs["drop_table"].new_window)
    main_app.button_new_database.clicked.connect(dialogs["new_database"].new_window)
    main_app.button_open_database.clicked.connect(dialogs["open_database"].new_window)

    # bind 'File' context menu buttons
    main_app.actionShow_Welcome_Screen.triggered.connect(main_app.welcome_tab)
    main_app.actionSettings.triggered.connect(dialogs["config"].new_window)
    main_app.actionQuit.triggered.connect(quit)

    # Finaly show the window :D
    MainWindow.show()

    sys.exit(app.exec_())
