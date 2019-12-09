
class BaseTable:

    def __init__(self):
        self.table_widget = None
        self.table_type = ""
        self.column_values = {} # columns are keys value params (editable, input value type, default_value )

        self.table_widget.itemChanged.connect(self.cell_changed)
        self.table_widget.currentItemChanged.connect(self.cell_selected)

    def table(self):
        """gets the table and returns table wiget"""
        pass

    def cell_selected(self, item, prv_item):
        pass

    def cell_changed(self, item):
        """ signal/callback when cell changes in table """
        pass
