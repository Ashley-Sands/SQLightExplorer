import amsql_viewer_ui
from PyQt5 import QtCore, QtGui, QtWidgets
import ui_helpers




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    main_app = amsql_viewer_ui.Ui_MainWindow()
    main_app.setupUi(MainWindow)
    main_app.welcom_tab()

    MainWindow.show()

    sys.exit(app.exec_())
