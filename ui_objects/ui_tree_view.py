from PyQt5 import QtWidgets
from ui_objects.ui_helpers import UiHelpers
import web_querys

class UiTreeView:

    def __init__(self, tree_view, tab_table):

        self.tree_view = tree_view
        self.tab_table = tab_table
        self.parent_items = {}  # key: display names
        self.help = UiHelpers()

        self.open_table_action = [] # callback sig, actionData, 1

        self.tree_view.itemDoubleClicked.connect( self.open_tree_item_in_tab )

    def add_actions(self, open_table_action):
        self.open_table_action.append(open_table_action)

    def open_tree_item_in_tab(self, tree_item, column_id):

        if tree_item.parent() == None :
            return;

        action_data = {}

        # get the data required for the action
        action_data["database_name"] = tree_item.parent().text(column_id)
        action_data["table_name"] = tree_item.text(column_id)

        # add new tab and table.
        self.tab_table.add_tab( "Table:" + action_data["table_name"] )

        for action in self.open_table_action:
            action.run_action(action_data, 1)

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
