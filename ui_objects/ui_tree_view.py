from PyQt5 import QtWidgets
from ui_objects.ui_helpers import UiHelpers
import web_querys

class UiTreeView:

    def __init__(self, tree_view, tab_table):

        self.tree_view = tree_view  # widget
        self.tab_table = tab_table
        self.parent_items = {}  # key: display names
        self.help = UiHelpers()

        self.double_click_action = [] # callback sig, actionData, 1

        self.tree_view.itemDoubleClicked.connect( self.item_double_clicked )

    def add_actions(self, open_table_action):
        self.double_click_action.append(open_table_action)

    def item_double_clicked(self, tree_item, column_id):

        action_data = {"column_id": column_id}

        for action in self.double_click_action: # TODO: erly exit if bad status from action
            action.run_action(action_data, 1)

    def add_tree_item(self, parent_name, str):
        """ add item to tree

        :param parent_name:  display name of parent tree items (None = new parent)
        :param str:          item display text
        :return:             QTreeWidgetItem
        """

        item = None
        if parent_name == None:
            item = self.parent_items[str] = QtWidgets.QTreeWidgetItem(self.tree_view, [str])
        else:
            item = QtWidgets.QTreeWidgetItem(self.parent_items[parent_name], [str])

        return item

    def get_selected_item_and_parent_text(self):
        """ gets the selected item and its parent
            if it is the topmost item selected, selected will be None
            :return: parent, child
        """

        selected_item = self.tree_view.currentItem()
        parent = None

        if selected_item is not None and selected_item.parent() is None:
            parent = selected_item.text(0)
            selected_item = None
        elif selected_item is not None:
            parent = selected_item.parent().text(0)
            selected_item = selected_item.text(0)

        return parent, selected_item

    def remove_root_item(self, parent_name):
        if parent_name in self.parent_items:
            self.tree_view.takeTopLevelItem(self.tree_view.indexOfTopLevelItem(self.parent_items[parent_name]))