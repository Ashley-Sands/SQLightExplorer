from windows import amsql_explorer_window
from ui_objects.ui_tab_table import ui_tabTable
from ui_objects.ui_tree_view import UiTreeView
from dialogue_window import DialogueWindow_Warning, DialogueWindow_TextEnter, DialogueWindow_Config

dialogs = {}

# create our dialogue instances
dialogs["drop_table"] = DialogueWindow_Warning()
dialogs["new_database"] = DialogueWindow_TextEnter()
dialogs["open_database"] = DialogueWindow_TextEnter()
dialogs["config"] = DialogueWindow_Config();

# set dict of dialogues in each dialogue instance to prevent multiple windows from being opened
dialogs["drop_table"].set_dialog_windows(dialogs)
dialogs["new_database"].set_dialog_windows(dialogs)
dialogs["open_database"].set_dialog_windows(dialogs)
dialogs["config"].set_dialog_windows(dialogs)

if __name__ == "__main__":
    import sys
    from PyQt5 import QtWidgets

    # start the QApp
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    main_app = amsql_explorer_window.Ui_MainWindow()
    main_app.setupUi(MainWindow)

    # Add the welcome tab
    main_app.welcome_tab()

    # Setup the classes to manage the UI elements :)
    ui_tab_table = ui_tabTable( main_app.tab_view )
    ui_tree_view = UiTreeView(main_app.treeWidget, ui_tab_table)

    # bind buttons
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