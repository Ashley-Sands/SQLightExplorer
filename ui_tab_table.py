from PyQt5 import QtCore, QtGui, QtWidgets
from ui_helpers import UiHelpers

class ui_tabTable:

    def __init__(self, tab_widget ):
        """ Stores tab widget and manages tabs

        :param tab_widget:  the widget that contains tabs.
        """
        self.translate = QtCore.QCoreApplication.translate
        self.tab_widget = tab_widget
        self.tab_widget.tabCloseRequested.connect( self.close_tab );
        self.tab_count = 0;

        self.help = UiHelpers()

    def add_tab(self, name):
        """ Adds new tab to table widget

        :param object_name:     name of the object (should be unique to app)
        :param name:            name to display on tab
        :param table_widget:    table to add tab to
        :return:                the new tab
        """

        tab = QtWidgets.QWidget()
        tab.setObjectName( "tab_"+str(self.tab_count) )

        self.tab_widget.addTab(tab, "")
        self.tab_widget.setTabText(self.tab_widget.indexOf(tab), self.translate("MainWindow", name))

        # create table view
        table = self.help.create_table_widget(tab, "table_" + str(self.tab_count), (0, 15, 600, 371))
        self.help.set_table_columns(table, ["a", "b", "c", "d", "e"])

        # set active!
        self.tab_widget.setCurrentIndex(self.tab_widget.indexOf(tab))

        self.tab_count += 1

        return tab

    def close_tab(self, tab_index):
        self.tab_widget.removeTab(tab_index)
