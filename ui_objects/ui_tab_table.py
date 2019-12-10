from PyQt5 import QtCore, QtWidgets
from ui_objects.ui_helpers import UiHelpers
from ui_objects.ui_tables import DbTable_Table, NewTable_Table

class ui_tabTable:

    TAB_TYPE_TABLE = "Table"
    TAB_TYPE_NEW_TABLE = "New_Table"

    def __init__(self, tab_widget, status_bar):
        """ Stores tab widget and manages tabs

        :param tab_widget:  the widget that contains tabs.
        """
        self.translate = QtCore.QCoreApplication.translate
        self.tab_widget = tab_widget
        self.tab_widget.tabCloseRequested.connect( self.close_tab )

        self.selected_cel = None
        self.selected_cel_value = ""    # used to restore value if invalid value is inputed

        self.tabs = {}      # key tab names, tuple(tab, table)
        self.tab_data = {}  # key tab names, dict{type, db_name, table_name}
        self.tab_count = 0

        self.table_cell_changed_actions = []  # need to be stored in here so we can bind them when we create the table

        self.status_bar = status_bar
        self.help = UiHelpers()

    def add_action(self, action):
        self.table_cell_changed_actions.append( action )

    @staticmethod
    def get_tab_name(tab_type, db_name, table_name):
        return tab_type + ":" + db_name + "." + table_name

    def get_tab_data(self, tab_name):

        if tab_name not in self.tabs:
            return None

        return self.tabs[tab_name]

    def add_tab(self, tab_type, database_name, table_name):
        """ Adds new tab to table widget

        :param tab_type:        the type of tab ie. new_table, table
        :param database_name:   name of the database the tab belongs to
        :param table_name:      name of table the tab belongs to
        :return:                the new tab, None if already exist
        """

        name = ui_tabTable.get_tab_name(tab_type, database_name, table_name)

        if name.lower() in self.tabs:
            return None

        tab = QtWidgets.QWidget()
        tab.setObjectName( "tab_"+str(self.tab_count) )


        self.tab_widget.addTab(tab, "")
        self.tab_widget.setTabText(self.tab_widget.indexOf(tab), self.translate("MainWindow", name))

        # create table view
        table = DbTable_Table(self.status_bar, tab_type, database_name, table_name)
        table.new_table(tab, self.tab_count)
        table.add_actions( self.table_cell_changed_actions )

        # set active!
        self.tab_widget.setCurrentIndex(self.tab_widget.indexOf(tab))

        self.tabs[name.lower()] = tab, table
        self.tab_data[name.lower()] = {"type": tab_type, "db_name": database_name, "table_name": table_name}
        self.tab_count += 1

        return tab, table

    def get_tab_ui_table(self, tab_type, db_name, table_name):

        return self.tabs[ self.get_tab_name(tab_type, db_name, table_name).lower() ][1]

    # TODO this and get name should be done when the tab changes
    def get_current_tab_table(self):
        """ Get the current tab and table if exist in obj.
            (Some tabs are not tab table and wont be found)
        """

        for t in self.tabs:
            if self.tabs[t][0] == self.tab_widget.currentWidget():
                return self.tabs[t]

        return None, None

    def get_current_tab_name(self):

        for t in self.tabs:
            if self.tabs[t][0] == self.tab_widget.currentWidget():
                return t

    def get_tab_table_from_table_item(self, item):
        """Gets the tabs tuple from table item. None if not found"""
        for k in self.tabs:
            if self.tabs[k][1] == item.tableWidget():
                return self.tabs[k]

        return None, None

    def get_database_and_table_name(self):
        """Gets the current database and table for selected table"""
        current_tab_name = self.get_current_tab_name()
        if current_tab_name is not None:
            return self.tab_data[current_tab_name]["db_name"], self.tab_data[current_tab_name]["table_name"]
        else:
            return None, None

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
        if self.tab_widget.tabText(tab_index) in self.tabs:
            del self.tabs[self.tab_widget.tabText(tab_index)]

        # bye bye, tab :)
        self.tab_widget.removeTab(tab_index)

