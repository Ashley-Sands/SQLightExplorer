from windows import amsql_explorer_window
from ui_objects.ui_tab_table import ui_tabTable
from ui_objects.ui_tree_view import UiTreeView
from dialogue_window import DialogueWindow_Warning, DialogueWindow_TextEnter, DialogueWindow_Config, DialogueWindow_Message

from actions import Action_OpenDatabase, Action_NewDatabase, Action_TableColumns, Action_TableRows
from actions import Action_updateTableRow, Action_DropTable, Action_RemoveRowsFromTable
from actions import Action_InsertNewRow, Action_OpenTableTabFormTreeItem, Action_OpenTableTabForNewTable

def noAction(a, b):
    pass

if __name__ == "__main__":
    import amsql_config # setup config
    import global_config
    import sys
    from PyQt5 import QtWidgets

    global_config.GlobalConfig.load_from_file()

    # start the QApp
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    main_app = amsql_explorer_window.Ui_MainWindow()
    main_app.setupUi(MainWindow)

    # Setup message dialog window
    dialog_message = DialogueWindow_Message()

    # Add the welcome tab
    main_app.welcome_tab()

    # Setup the classes to manage the UI elements :)
    ui_tab_table = ui_tabTable( main_app.tab_view, main_app.statusbar )
    ui_tree_view = UiTreeView(main_app.treeWidget, main_app.statusbar )

    # Setup actions
    open_database_action = Action_OpenDatabase(dialog_message, ui_tree_view)
    new_database_action = Action_NewDatabase(dialog_message, ui_tree_view)
    new_table_action = Action_OpenTableTabForNewTable(dialog_message, ui_tree_view, ui_tab_table)

    drop_table_action = Action_DropTable(dialog_message, ui_tree_view)
    open_table_in_tab_action = Action_OpenTableTabFormTreeItem(dialog_message, ui_tree_view, ui_tab_table)

    table_columns_action = Action_TableColumns(dialog_message, ui_tree_view, ui_tab_table)
    table_rows_action = Action_TableRows(dialog_message, ui_tree_view, ui_tab_table)
    table_item_changed_action = Action_updateTableRow(dialog_message)
    table_remove_rows_action = Action_RemoveRowsFromTable(dialog_message, ui_tab_table)
    table_insert_row_action = Action_InsertNewRow(dialog_message, ui_tab_table)

    # set actions on ui
    ui_tree_view.add_actions(open_table_in_tab_action)
    ui_tree_view.add_actions(table_columns_action)
    ui_tree_view.add_actions(table_rows_action)
    ui_tab_table.add_item_changed_action(table_item_changed_action)

    # Setup dialogue instances
    dialogs = {}

    dialogs["drop_table"] = DialogueWindow_Warning(drop_table_action.run_action)                # TODO: update table name in window
    dialogs["remove_rows"] = DialogueWindow_Warning(table_remove_rows_action.run_action)        # TODO: update table name in window
    dialogs["new_database"] = DialogueWindow_TextEnter(new_database_action.run_action, "New database name")
    dialogs["open_database"] = DialogueWindow_TextEnter(open_database_action.run_action, "Existing database name")
    dialogs["new_table"] = DialogueWindow_TextEnter(new_table_action.run_action, "New table name")

    dialogs["config"] = DialogueWindow_Config()

    # setup display values on dialog windows
    dialogs["new_database"].set_standard_buttons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
    dialogs["new_table"].set_standard_buttons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)

    # set dict of dialogues in each dialogue instance to prevent multiple windows from being opened
    dialogs["drop_table"].set_dialog_windows(dialogs)
    dialogs["remove_rows"].set_dialog_windows(dialogs)
    dialogs["new_database"].set_dialog_windows(dialogs)
    dialogs["open_database"].set_dialog_windows(dialogs)
    dialogs["new_table"].set_dialog_windows(dialogs)
    dialogs["config"].set_dialog_windows(dialogs)

    # bind buttons
    main_app.button_drop_table.clicked.connect(dialogs["drop_table"].new_window)
    main_app.button_new_database.clicked.connect(dialogs["new_database"].new_window)
    main_app.button_open_database.clicked.connect(dialogs["open_database"].new_window)
    main_app.button_remove_row.clicked.connect(dialogs["remove_rows"].new_window)
    main_app.button_add_table.clicked.connect(dialogs["new_table"].new_window)
    main_app.button_add_row.clicked.connect(table_insert_row_action.button_run_action)

    # bind 'File' context menu buttons
    main_app.actionShow_Welcome_Screen.triggered.connect(main_app.welcome_tab)
    main_app.actionSettings.triggered.connect(dialogs["config"].new_window)
    main_app.actionQuit.triggered.connect(quit)

    # add the test_db on start.
    startup_databases = global_config.GlobalConfig.get("default_db").split("\n")
    for db in startup_databases:
        if not db.isspace() and len(db) > 0:
            open_database_action.run_action( {"text": db}, 1 )

    # Finally show the window :D
    MainWindow.show()

    sys.exit(app.exec_())