from PyQt5 import QtCore, QtWidgets
from ui_objects.ui_helpers import UiHelpers

class ui_tabTable:

    def __init__(self, tab_widget):
        """ Stores tab widget and manages tabs

        :param tab_widget:  the widget that contains tabs.
        """
        self.translate = QtCore.QCoreApplication.translate
        self.tab_widget = tab_widget
        self.tab_widget.tabCloseRequested.connect( self.close_tab );

        self.tabs = {}      # key tab names tuple(tab, table)
        self.tab_count = 0;

        self.help = UiHelpers()

    def add_tab(self, name):
        """ Adds new tab to table widget

        :param name:            name to display on tab
        :return:                the new tab, None if already exist
        """

        if name in self.tabs:
            return None

        tab = QtWidgets.QWidget()
        tab.setObjectName( "tab_"+str(self.tab_count) )

        self.tab_widget.addTab(tab, "")
        self.tab_widget.setTabText(self.tab_widget.indexOf(tab), self.translate("MainWindow", name))

        # create table view
        table = self.help.create_table_widget(tab, "table_" + str(self.tab_count), (0, 15, 600, 371))

        # set active!
        self.tab_widget.setCurrentIndex(self.tab_widget.indexOf(tab))

        self.tabs[name] = tab, table
        self.tab_count += 1

        return tab

    def set_table_columns(self, tab_name, column_names):
        """ Sets column names for tab with tab_name

        :param tab_name:        name of tab
        :param column_names:    List of column names
        :return:                None
        """

        if tab_name not in self.tabs:
            return None

        self.help.set_table_columns(self.tabs[tab_name][1], column_names)

    def close_tab(self, tab_index):

        if  self.tab_widget.tabText(tab_index) in self.tabs:
            del self.tabs[self.tab_widget.tabText(tab_index)]

        self.tab_widget.removeTab(tab_index)

