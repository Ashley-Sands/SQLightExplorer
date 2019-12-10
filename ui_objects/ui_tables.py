import ui_objects.ui_helpers

class BaseTable:

    def __init__(self, table_widget, table_type):

        self.help = ui_objects.ui_helpers.UiHelpers()
        self.table_widget = table_widget
        self.table_type = table_type
        self.column_values = {}  # columns labels are keys value params (editable, input value type, default_value )

        self.setting_rows = False       # used to prevent callbacks

        self.table_widget.itemChanged.connect(self.cell_content_changed)
        self.table_widget.currentItemChanged.connect(self.cell_selected_item_changed)

    def new_table(self, parent_widget):
        """(Abstract) gets the table and returns table widget"""
        pass

    def cell_selected_item_changed(self, item, prv_item):
        """(Abstract) called when the table item selection has changed"""
        pass

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

        self.column_values = dict(zip(column_labels, params))
        self.help.set_table_columns(self.table_widget, column_labels)

        pass

    def set_rows(self, rows):
        """Sets rows of columns in table
        :param rows:    List of List [row][column]
        """

        self.setting_rows = True
        self.help.set_table_rows(self.table_widget, rows, self.column_values)   # TODO: help.set_table_rows need column params updating to dict
        self.setting_rows = False

    def get_default_values(self):
        """ gets the default values for columns

        :return:    dict of default value {col_label: default value}
        """
        default_values = { cl: self.column_values[cl]["default_value"] for cl in self.column_values }
        return default_values

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


class DbTable_Table(BaseTable):
    pass

class NewTable_Table(BaseTable):
    pass