import amsql_viewer_ui
import ui_helpers




if __name__ == "__main__":

    import sys
    from PyQt5 import QtCore, QtGui, QtWidgets

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    main_app = amsql_viewer_ui.Ui_MainWindow()
    main_app.setupUi(MainWindow)
    main_app.welcome_tab()

    MainWindow.show()

    sys.exit(app.exec_())
