import ui_objects.ui_helpers

class BaseTable:

    def __init__(self, status_bar, table_type, db_name, table_name):

        self.help = ui_objects.ui_helpers.UiHelpers()

        self.table_widget = None
        self.status_bar = status_bar
        self.table_type = table_type

        self.database_name = db_name
        self.table_name = table_name

        self.column_params = {}  # columns labels are keys, values tuple of params (editable, value_type, default_value)

        self.selected_cel = None
        self.selected_cel_value = ""

        self.setting_rows = False       # used to prevent callbacks

        self.cell_changed_action = []

    def add_action(self, action):
        """Add a single action"""
        self.cell_changed_action.append( action )

    def add_actions(self, actions):
        """Add a list of actions"""
        self.cell_changed_action =[ *self.cell_changed_action, *actions ]

    def new_table(self, parent_widget, tab_count):
        """(Virtual) gets the table and returns table widget"""

        self.table_widget = self.help.create_table_widget(parent_widget, "table_" + str(tab_count), (0, 15, 598, 376))

        self.table_widget.itemChanged.connect(self.cell_content_changed)
        self.table_widget.currentItemChanged.connect(self.cell_selected_item_changed)

    def cell_selected_item_changed(self, item, prv_item):
        """(Virtual) called when the table item selection has changed"""
        self.selected_cel = item
        self.selected_cel_value = item.text()

    def cell_content_changed(self, item):
        """(Abstract) called when cell content has changes in table """
        pass

    def add_column_to_end(self, column_label, params):
        """Adds a new column to the end of the row
        :param column_label:  column name
        :param params:  Dict of params (editable, value_type, default_value) Must match columns
        """
        pass

    def set_columns(self, column_labels, params):
        """Adds a new column to the end of the row
        :param column_labels:  List of column names
        :param params:  List of dict (editable, value_type, default_value) Must match columns
        """

        self.column_params = dict(zip(column_labels, params))
        self.help.set_table_columns(self.table_widget, column_labels)

        pass

    def set_rows(self, rows):
        """Sets rows of columns in table
        :param rows:    List of List [row][column]
        """

        self.setting_rows = True
        self.help.set_table_rows(self.table_widget, rows, self.column_params)   # TODO: help.set_table_rows need column params updating to dict
        self.setting_rows = False

    def get_default_values(self):
        """ gets the default values for columns

        :return:    dict of default value {col_label: default value}
        """

        default_values = {cl: self.column_params[cl][2] for cl in self.column_params}

        return default_values

    def get_value_type_for_column(self, column_id):
        """Gets the value type for column id"""

        return self.column_params[ [*self.column_params][column_id] ][1]

    def get_selected_rows(self):
        """ Gets a list of selected rows"""
        selected_items = self.table_widget.selectedItems()
        rows = []

        for i in selected_items:
            if i.row() not in rows: # skip if we have already added row
                rows.append( i.row() )

        return rows

    def get_column_name(self, column_id):
        """ get the column label for column id """
        return self.table_widget.horizontalHeaderItem(column_id).text()

    def get_column_values_for_rows(self, column_id, rows):
        """ Gets values for a single columns rows"""
        return [ self.table_widget.item(r, column_id).text() for r in rows ]

    def verify_cell_data_type(self, data, data_type):
        """ (Virtual) Verifies cells data type is correct """
        return True

class DbTable_Table(BaseTable):

    def cell_content_changed(self, item):   # TODO: Fix **crash**

        if self.setting_rows:
            return

        valid_data = self.verify_cell_data_type( item.text(), self.get_value_type_for_column( item.column() ) )

        if not valid_data:
            item.setText( self.selected_cel_value )
            self.status_bar.showMessage("Error: Invalid Data type", 20000)
            return
        else:
            self.selected_cel_value = item.text()

        action_data = {}
        action_data["database_name"] = self.database_name
        action_data["table_name"] = self.table_name
        action_data["set_columns"] = [ [*self.column_params][item.column()] ]   # TODO: i think this works
        action_data["set_data"] = [item.text()]
        action_data["where_columns"] = [ [*self.column_params][0] ]   # in this case we will only use the first column as are where
        action_data["where_data"] = [ self.table_widget.item( item.row(), 0 ).text() ]

        for act in self.cell_changed_action:
            act.run_action( action_data, 1 )

class NewTable_Table(BaseTable):
    pass