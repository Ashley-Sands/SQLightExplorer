# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sqllite.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

# This code has been changed by Ashley Sands

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(823, 512)
        MainWindow.setMinimumSize(QtCore.QSize(823, 512))
        MainWindow.setMaximumSize(QtCore.QSize(823, 512))
        MainWindow.setDocumentMode(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 181, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.button_new_database = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_new_database.setObjectName("button_new_database")
        self.horizontalLayout.addWidget(self.button_new_database)

        self.button_open_database = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_open_database.setObjectName("button_open_database")
        self.horizontalLayout.addWidget(self.button_open_database)

        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 50, 181, 371))
        self.treeWidget.setObjectName("treeWidget")

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 430, 181, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.button_add_table = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.button_add_table.setObjectName("button_add_table")
        self.horizontalLayout_2.addWidget(self.button_add_table)

        self.button_drop_table = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.button_drop_table.setObjectName("button_drop_table")
        self.horizontalLayout_2.addWidget(self.button_drop_table)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(190, 10, 20, 451))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(220, 430, 181, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_2")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.button_add_row = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.button_add_row.setObjectName("add_row")
        self.horizontalLayout_3.addWidget(self.button_add_row)

        self.button_remove_row = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.button_remove_row.setObjectName("button_remove_row")
        self.horizontalLayout_3.addWidget(self.button_remove_row)

        self.tab_view = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_view.setEnabled(True)
        self.tab_view.setGeometry(QtCore.QRect(210, 10, 600, 414))
        self.tab_view.setAutoFillBackground(False)
        self.tab_view.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab_view.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_view.setElideMode(QtCore.Qt.ElideNone)
        self.tab_view.setDocumentMode(False)
        self.tab_view.setTabsClosable(True)
        self.tab_view.setMovable(True)
        self.tab_view.setTabBarAutoHide(False)
        self.tab_view.setObjectName("tab_view")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 823, 21))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")

        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")

        self.actionShow_Welcome_Screen = QtWidgets.QAction(MainWindow)
        self.actionShow_Welcome_Screen.setObjectName("actionShow_Welcome_Screen")
        #self.actionShow_Welcome_Screen.triggered.connect(self.add_new_welcome_tab)

        self.menuFile.addAction(self.actionShow_Welcome_Screen)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)

        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tab_view.setCurrentIndex(0)

        # self.treeWidget.doubleClicked['QModelIndex'].connect(self.treeWidget.collapseAll)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setTabOrder(self.button_new_database, self.button_open_database)
        MainWindow.setTabOrder(self.button_open_database, self.treeWidget)
        MainWindow.setTabOrder(self.treeWidget, self.tab_view)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AMSql - Viewer"))
        self.button_new_database.setText(_translate("MainWindow", "New Database"))
        self.button_open_database.setText(_translate("MainWindow", "Open Database"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Table Name"))

        self.button_add_table.setText(_translate("MainWindow", "Add Table"))
        self.button_drop_table.setText(_translate("MainWindow", "Drop Table"))

        self.button_add_row.setText(_translate("MainWindow", "Add New Row"))
        self.button_remove_row.setText(_translate("MainWindow", "Remove Rows"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionShow_Welcome_Screen.setText(_translate("MainWindow", "Show Welcome Screen"))

    def add_new_welcome_tab(self, checked):
        self.welcome_tab()

    def welcome_tab(self):
        _translate = QtCore.QCoreApplication.translate

        self.tab_welcome = QtWidgets.QWidget()
        self.tab_welcome.setObjectName("tab_welcome")

        self.label = QtWidgets.QLabel(self.tab_welcome)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(6, 10, 571, 371))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())

        self.label.setSizePolicy(sizePolicy)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.tab_view.addTab(self.tab_welcome, "")

        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">AMSql </span><span style=\" font-size:14pt; vertical-align:super;\">v0.2</span></p><p align=\"center\"><span style=\" font-size:12pt;\">AMSql is simple tool to view and edit sql lite databases over http/https</span></p><p><br/></p><p><span style=\" font-size:10pt;\">Once you have added a database, double click on a table nested in the database to view in a new tab :)</span></p><p><br/></p><p><span style=\" font-size:10pt;\">Featchers...</span></p></body></html>"))
        self.tab_view.setTabText(self.tab_view.indexOf(self.tab_welcome), _translate("MainWindow", "Welcome"))
        self.tab_view.setCurrentIndex(self.tab_view.indexOf(self.tab_welcome))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.tab_view.currentWidget()
    MainWindow.show()
    sys.exit(app.exec_())
