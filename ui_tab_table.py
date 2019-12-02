from PyQt5 import QtCore, QtGui, QtWidgets

class ui_tabTable:

    def __init__(self, tab_widget ):
        """ Stores tab widget and manages tabs

        :param tab_widget:  the widget that contains tabs.
        """
        self.translate = QtCore.QCoreApplication.translate
        self.tab_widget = tab_widget
        self.tab_widget.tabCloseRequested.connect( self.close_tab );

    def add_tab(self, object_name, name):
        """ Adds new tab to table widget

        :param object_name:     name of the object (should be unique to app)
        :param name:            name to display on tab
        :param table_widget:    table to add tab to
        :return:                the new tab
        """


        tab = QtWidgets.QWidget()
        tab.setObjectName( object_name )
        self.tab_widget.addTab(tab, "")
        self.tab_widget.setTabText(self.tab_widget.indexOf(tab), self.translate("MainWindow", name))
        # set active!
        self.tab_widget.setCurrentIndex(self.tab_widget.indexOf(tab))

        return tab

    def close_tab(self, tab_index):
        self.tab_widget.removeTab(tab_index)
