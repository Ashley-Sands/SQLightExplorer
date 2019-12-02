from PyQt5 import QtCore, QtGui, QtWidgets
from ui_helpers import UiHelpers

class UiTreeView:

    def __init__(self, tree_view, tab_table):

        self.tree_view = tree_view
        self.tab_table = tab_table
        self.parent_items = {}
        self.help = UiHelpers()

        self.tree_view.itemDoubleClicked.connect( self.open_tree_item_in_tab )

    def open_tree_item_in_tab(self, tree_item, column_id):

        if tree_item.parent() != None :
            return;

        # add new tab and table.
        self.tab_table.add_tab( "Table:"+tree_item.text(column_id) )

    def add_tree_item(self, parent_name, str):
        """ add item to tree

        :param parent_name:  display name of parent tree items (None = new parent)
        :param str:          item display text
        :return:             QTreeWidgetItem or none if error
        """

        item = None

        if parent_name == None:
            item = self.parent_items[str] = QtWidgets.QTreeWidgetItem(self.tree_view, [str])
        else:
            item = QtWidgets.QTreeWidgetItem(self.parent_items[parent_name], [str])

        return item
