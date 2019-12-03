from windows import amsql_explorer_window
from ui_objects.ui_tab_table import ui_tabTable
from ui_objects.ui_tree_view import UiTreeView
from dialogue_window import DialogueWindow_Warning, DialogueWindow_TextEnter, DialogueWindow_Config, DialogueWindow_Message
from actions import Action_OpenDatabase, Action_NewDatabase

def dialogue_callback( dialog_name, accepted ):
    pass
'''
    if accepted == 0:
        return

    web_query = WebQuerys()

    if dialog_name == "open_database":
        response = web_query.open_database( dialogs["open_database"].text )
        if str( response[0] ) == "404":
            dialog_message.set_message("Error: Database Not Found")
            dialog_message.new_window()
        elif str( response[0] ) == "408":
            dialog_message.set_message("Error: Connection Timed Out :(")
            dialog_message.new_window()
        else:
            # Add the data to the tree
            pass

    print("data:", response[0], response[1])
'''

if __name__ == "__main__":
    import amsql_config # setup config
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

    # Setup message dialog window
    dialog_message = DialogueWindow_Message("message")

    # Setup actions
    open_database_action = Action_OpenDatabase(dialog_message, ui_tree_view, message404="Error: Database Not Found")
    new_database_action = Action_NewDatabase(dialog_message, ui_tree_view, message404="Error: Database Already Exist")

    # Setup dialogue instances
    dialogs = {}

    dialogs["drop_table"] = DialogueWindow_Warning("drop_table", dialogue_callback)  #TODO: Remove name from class / __init__ as the callback now sets it self insted of its name :)
    dialogs["new_database"] = DialogueWindow_TextEnter("new_database", new_database_action.dialog_action)
    dialogs["open_database"] = DialogueWindow_TextEnter("open_database", open_database_action.dialog_action)
    dialogs["config"] = DialogueWindow_Config("config")

    # set dict of dialogues in each dialogue instance to prevent multiple windows from being opened
    dialogs["drop_table"].set_dialog_windows(dialogs)
    dialogs["new_database"].set_dialog_windows(dialogs)
    dialogs["open_database"].set_dialog_windows(dialogs)
    dialogs["config"].set_dialog_windows(dialogs)

    # bind buttons
    main_app.button_drop_table.clicked.connect(dialogs["drop_table"].new_window)
    main_app.button_new_database.clicked.connect(dialogs["new_database"].new_window)
    main_app.button_open_database.clicked.connect(dialogs["open_database"].new_window)

    # bind 'File' context menu buttons
    main_app.actionShow_Welcome_Screen.triggered.connect(main_app.welcome_tab)
    main_app.actionSettings.triggered.connect(dialogs["config"].new_window)
    main_app.actionQuit.triggered.connect(quit)

    # Finally show the window :D
    MainWindow.show()

    sys.exit(app.exec_())