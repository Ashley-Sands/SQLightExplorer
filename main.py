import amsql_viewer_ui
import ui_helpers
from ui_tab_table import ui_tabTable
from ui_tree_view import UiTreeView

# Signal functions


if __name__ == "__main__":

    import sys
    from PyQt5 import QtCore, QtGui, QtWidgets

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


    # Finaly show the window :D
    MainWindow.show()

    sys.exit(app.exec_())
