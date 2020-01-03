from PyQt5 import QtCore, QtWidgets
import ui_objects.ui_helpers
from global_config import GlobalConfig


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

        if self.selected_cel is None:
            self.selected_cel = ""
        else:
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
        """ Gets a list of selected row id"""
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

    def get_row_values_for_cols(self, row_id, cols):
        """ Gets values for a single columns rows"""
        return [ self.table_widget.item(row_id, c).text() for c in cols ]

    def get_row_widget_values_for_cols(self, row_id, cols):
        """ Gets values for a single columns rows"""
        return [ self.table_widget.cellWidget(row_id, c).currentText() for c in cols ]

    def verify_cell_data_type(self, value, value_type):
        """ (Virtual) Verifies cells data type is correct """
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

    combo_box_count = 0     # static

    def __init__(self, status_bar, table_type, db_name, table_name, tab):
        super().__init__(status_bar, table_type, db_name, table_name)
        self.tab = tab
        self.save_button = None
        self.add_column_button = None
        self.save_table_actions = []

    def add_save_table_actions(self, actions):
        self.save_table_actions = [*self.save_table_actions, *actions]

    def new_table(self, parent_widget, tab_count):
        super().new_table( parent_widget, tab_count )

        table_geometry = self.table_widget.geometry()

        table_height = table_geometry.height()
        row_height = 30

        table_geometry.setHeight(table_height)
        self.table_widget.setGeometry(table_geometry)

        column_values = []# * (self.table_widget.columnCount())

        # add rows for our values
        self.help.add_table_row(self.table_widget, column_values, label="Column Name", row_height=row_height)
        self.help.add_table_row(self.table_widget, column_values, label="Value Type", row_height=row_height)
        self.help.add_table_row(self.table_widget, column_values, label="Value Length", row_height=row_height)
        self.help.add_table_row(self.table_widget, column_values, label="Default Value", row_height=row_height)
        self.help.add_table_row(self.table_widget, column_values, label="", row_height=row_height)

        # add our first column
        self.add_column_to_end("Column ", (1, "ANY", None))
        self.add_column_to_end("Column ", (1, "ANY", None))

        self.save_button = self.help.create_button("Save Table", "save_table"+str(NewTable_Table.combo_box_count), (360, 440, 100, 50), pressed_signal=self.save_table_button_action)
        self.add_column_button = self.help.create_button("Add Column", "add_column_table"+str(NewTable_Table.combo_box_count), (360, 440, 100, 50), pressed_signal=self.add_column_button_action)

        self.table_widget.setCellWidget(4, 0, self.save_button)
        self.table_widget.setCellWidget(4, 1, self.add_column_button)

    def add_column_to_end(self, column_label, params):

        col_id = self.table_widget.columnCount()
        self.help.add_table_column(self.table_widget, col_id, column_label+str(col_id), [""]*5)

        combo_box_values = GlobalConfig.get("value_types").split("\n")
        combo_box = self.help.create_combo_box(combo_box_values, NewTable_Table.combo_box_count)
        NewTable_Table.combo_box_count += 1

        self.table_widget.setCellWidget(1, col_id, combo_box)

        # move the add column button to the end col of the table
        self.table_widget.setCellWidget(4, col_id, self.add_column_button)
        # prevent the button row being edited, by setting the cell that add column button was in to not editable
        last_col_item = self.table_widget.item(4, col_id-1)

        if last_col_item is not None:
            last_col_item.setFlags( self.help.get_cell_flags(0) )

    def add_column_button_action(self):
        self.add_column_to_end("Column ", (1, "ANY", None))

    def save_table_button_action(self):
        """ triggers save table action"""

        columns = [i for i in range(self.table_widget.columnCount())]

        act_data = {}
        act_data["database_name"] = self.database_name
        act_data["table_name"] = self.table_name
        act_data["column_names"] = self.get_row_values_for_cols(0, columns)
        act_data["data_types"] = self.get_row_widget_values_for_cols(1, columns)
        act_data["data_lengths"] = self.get_row_values_for_cols(2, columns)
        act_data["default_values"] = self.get_row_values_for_cols(3, columns)


        # clear out any columns with no names and replace spaces with '_'
        for i, v in enumerate(act_data["column_names"]):
            if v.isspace() or v == "":
                for k in act_data:
                    if k != "table_name" and k != "database_name":
                        act_data[k].pop(i)
            else:
                act_data["column_names"][i].replace(" ", "_")

        for act in self.save_table_actions:
            act.run_action(act_data, 1)


    def cell_content_changed(self, item):

        if item is None:
            return

        # length cells must be INT
        # default value must be TYPE cell
        row = item.row()
        value = item.text()
        valid_data = True

        if row == 2:    # length row
            valid_data =  self.verify_cell_data_type( value, "int" )
        elif row == 3:  # default value
            column = item.column()
            type_value = self.table_widget.cellWidget(1, column)

            if type_value is None:
                return

            type_value = type_value.currentText().lower()
            valid_data =  self.verify_cell_data_type( value, type_value )

        if not valid_data:
            item.setText( self.selected_cel_value )
            self.status_bar.showMessage("Error: Invalid Data type", 20000)
            return
        else:
            self.selected_cel_value = item.text()


