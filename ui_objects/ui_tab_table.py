from PyQt5 import QtCore, QtWidgets
from ui_objects.ui_helpers import UiHelpers

class ui_tabTable:

    def __init__(self, tab_widget, status_bar):
        """ Stores tab widget and manages tabs

        :param tab_widget:  the widget that contains tabs.
        """
        self.translate = QtCore.QCoreApplication.translate
        self.tab_widget = tab_widget
        self.tab_widget.tabCloseRequested.connect( self.close_tab )

        self.selected_cel_value = ""    # used to restore value if invalid value is inputed
        self.item_changed_action = []

        self.tabs = {}      # key tab names tuple(tab, table)
        self.table_column_parmas = {}   # key tab name. (editable, input value# )
        self.tab_count = 0;

        self.setting_table_data = False

        self.status_bar = status_bar
        self.help = UiHelpers()

    def add_item_changed_action(self, action):
        self.item_changed_action.append(action)

    def get_tab_data(self, tab_name):

        if tab_name not in self.tabs:
            return None

        return self.tabs[tab_name]

    def add_tab(self, name):
        """ Adds new tab to table widget

        :param name:            name to display on tab
        :return:                the new tab, None if already exist
        """

        if name.lower() in self.tabs:
            return None

        tab = QtWidgets.QWidget()
        tab.setObjectName( "tab_"+str(self.tab_count) )

        self.tab_widget.addTab(tab, "")
        self.tab_widget.setTabText(self.tab_widget.indexOf(tab), self.translate("MainWindow", name))

        # create table view
        table = self.help.create_table_widget(tab, "table_" + str(self.tab_count), (0, 15, 600, 371))
        table.itemChanged.connect(self.cell_changed)
        table.itemPressed.connect(self.cell_selected)

        # set active!
        self.tab_widget.setCurrentIndex(self.tab_widget.indexOf(tab))

        self.tabs[name.lower()] = tab, table
        self.tab_count += 1

        return tab, table

    def set_table_columns(self, tab_name, column_names, column_params):
        """ Sets column names for tab with tab_name

        :param tab_name:        name of tab
        :param column_names:    List of column names
        :param column_params:   List of tuples of colum params [( editable, type ), ...]
        :return:                None
        """

        if tab_name.lower() not in self.tabs:
            return

        self.help.set_table_columns(self.tabs[tab_name][1], column_names)
        self.table_column_parmas[tab_name.lower()] = column_params

    def set_table_rows(self, tab_name, rows):
        """

        :param tab_name:    name of tab to set rows in
        :param rows:        List of rows (List of List)
        :return:            None
        """

        self.setting_table_data = True

        if tab_name.lower() not in self.tabs:
            return

        self.help.set_table_rows(self.tabs[tab_name][1], rows, self.table_column_parmas[tab_name.lower()])

        self.setting_table_data = False

    def get_tab_table_from_table_item(self, item):
        """Gets the tabs tuple from table item. None if not found"""
        for k in self.tabs:
            if self.tabs[k][1] == item.tableWidget():
                return self.tabs[k]

        return None, None

    def cell_selected(self, item):
        self.selected_cel_value = item.text()

    def cell_changed(self, item):
        """ signal/callback when cell changes in table """

        if self.setting_table_data is True:
            return

        tab, table = self.get_tab_table_from_table_item(item)

        if tab is None:
            self.status_bar.showMessage("Error: tab not found. can not change cell", 20000)
            return

        tab_name = self.tab_widget.tabText( self.tab_widget.indexOf(tab) )
        table_name = tab_name.split(":")[1]   # (table:table_name)
        valid_data = self.verify_value(item.text(), self.table_column_parmas[tab_name.lower()][item.column()][1])

        if not valid_data:
            item.setText(self.selected_cel_value)
            self.status_bar.showMessage("Error: Invalid data type", 20000)
            return
        else:
            self.selected_cel_value = item.text()   # updated the selected value if valid

        # get the rowid value
        rowid_value = table.item(item.row(), 0)                 # TODO: this will only use the first column for the WHERE when updateing cells
        where_column_name = table.horizontalHeaderItem(0)       # Altho, we still get the name of the column

        print(item.text(), item.row(), item.column(), where_column_name.text(), "=", rowid_value.text())

        #for act in self.item_changed_action:
            #act.run_action() # TODO

    def verify_value(self, value, value_type):
        """Verifies that the values matches the column value type"""

        verified = True

        # TODO: Varchar length
        try:
            if value_type.lower() == "int":
                int(value)
            elif value_type.lower() == "float":
                float(value)
        except:
            verified = False

        print("Value Type:", value_type, "Vaild:", verified)

        return verified

    def close_tab(self, tab_index):
        # delete tab data
        if  self.tab_widget.tabText(tab_index) in self.tabs:
            del self.tabs[self.tab_widget.tabText(tab_index)]

        # delete table column data.
        if  self.tab_widget.tabText(tab_index) in self.table_column_parmas:
            del self.table_column_parmas[ self.tab_widget.tabText(tab_index) ]

        # bye bye, tab :)
        self.tab_widget.removeTab(tab_index)

