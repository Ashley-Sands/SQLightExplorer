from web_querys import WebQuerys
from ui_objects.ui_tab_table import ui_tabTable
import re

# TODO: there are a bunch on new methods in tab_table that would make most actions simpler
class Action:

    ACTION_STATUS_404 = 0
    ACTION_STATUS_408 = 1
    ACTION_STATUS_INVALID_RESPONSE = 2
    ACTION_STATUS_OK = 3

    def __init__(self, dialog_message):
        self.dialog_message = dialog_message
        self.web_query = WebQuerys()
        self.status = self.ACTION_STATUS_404

    def request(self, data_object):     # TODO: by default this should return stats 404, not found.
        """

        :return: request response
        """
        pass

    def button_run_action(self):
        """ alows the action to be directly binded to a button signal
        """
        self.run_action([], 1)

    def run_action(self, data_object, accepted):  # should be run_action
        """ Runs the action handling serveer responces

        :param data_object:  Object that contains all data for the action
        :param accepted:     Alows binding to buttons (set to 1 if not button action)
        :return:            Action Status
        """

        if accepted == 0:
            return

        response = self.request(data_object)

        if response is None: # in the case of response being none it will handle its own error messages :)
            return

        if str(response[0]) == "404":
            self.dialog_message.set_message(response[1])
            self.dialog_message.new_window()
            self.action_404(data_object)
            self.status = self.ACTION_STATUS_404
        elif str(response[0]) == "408":
            self.dialog_message.set_message("Error: Connection Timed Out :(")
            self.dialog_message.new_window()
            self.action_408(data_object)
            self.status = self.ACTION_STATUS_408
        elif not self.valid_response_data(response[1]):
            self.dialog_message.set_message("Error: Invalid response :(")
            self.dialog_message.new_window()
            self.status = self.ACTION_STATUS_INVALID_RESPONSE
        else:
            self.action(data_object, response[1])
            self.status = self.ACTION_STATUS_OK

        return self.status

    def action(self, data_object, response_data):
        pass

    def action_404(self, data_object):
        pass

    def action_408(self, data_object):
        pass

    def valid_response_data(self, response):
        """ Checks if response is vails (needs overriding)"""
        return False


class Action_NewDatabase(Action):

    def __init__(self, dialog_message, tree_view):
        super().__init__(dialog_message)
        self.tree_view = tree_view

    def request(self, data_object):
        return self.web_query.new_database( data_object["text"] )

    def action(self, data_object, response):

        # remove if already exist (so it gets refreshed)
        self.tree_view.remove_root_item(data_object["text"])

        # Add parent data to the tree
        self.tree_view.add_tree_item(None, data_object["text"])  # add database

    def valid_response_data(self, response):
        return True


class Action_OpenDatabase(Action_NewDatabase):

    def request(self, data_object):
        return self.web_query.open_database( data_object["text"] )

    def action(self, data_object, response):

        # Add child data to the tree
        super().action(data_object, response)
        item = None
        for r in response:
            item = self.tree_view.add_tree_item(data_object["text"], r)

        if item is not None and item.parent() is not None:
            self.tree_view.tree_view.expandItem(item.parent())

    def valid_response_data(self, response):
        return type(response) is list


class Action_DropTable(Action):

    def __init__(self, dialog_message, tree_view):
        super().__init__(dialog_message)

        self.tree_widget = tree_view.tree_view
        self.database = None
        self.refresh_database_action = Action_OpenDatabase(dialog_message, tree_view)

    def request(self, data_object):

        table = self.tree_widget.currentItem()
        # check we have an item selected and it has a parent (not db selected)
        if table is None or table.parent() is None:
            self.dialog_message.set_message("Table not Selected")
            self.dialog_message.new_window()
            return None

        self.database = table.parent()

        return self.web_query.drop_table( self.database.text(0), table.text(0) )

    def action(self, data_object, response):

        if self.database is None:
            return

        database_name = self.database.text(0)

        self.refresh_database_action.run_action({"text": database_name}, 1)


    def valid_response_data(self, response):
        return True


class Action_OpenTableTabForNewTable(Action):

    def __init__(self, dialogue_message, tree_view, tab_table):
        super().__init__(dialogue_message)
        self.tree_view = tree_view
        self.tab_table = tab_table

    def request(self, data_object):
        """check that the table does no already exist in the selected database
        :param data_object:     Dict containing key 'Text' with the value of the new table name
        """
        regex = "[a-zA-Z]"
        if len(data_object["text"]) == 0 or data_object["text"].isspace()  :
            self.dialog_message.set_message("Error: No table name entered")
            self.dialog_message.new_window()
            return None
        elif len( re.findall(regex, data_object["text"][0]) ) == 0:
            print(data_object["text"][0], re.findall(regex, data_object["text"][0]))
            self.dialog_message.set_message("Error: Database must start with a letter")
            self.dialog_message.new_window()
            return None

        selected_database, table_name = self.tree_view.get_selected_item_and_parent_text()
        table_name = data_object["text"]
        table_name.replace(" ", "_")

        if selected_database is None:
            self.dialog_message.set_message("No database selected")
            self.dialog_message.new_window()
            return None

        return self.web_query.table_does_not_exist(selected_database, table_name)

    def action(self, data_object, response):
        print("We good :)")
        selected_database = self.tree_view.get_selected_item_and_parent_text()[0]
        table_name = data_object["text"]
        table_name.replace(" ", "_")
        self.tab_table.add_tab(ui_tabTable.TAB_TYPE_NEW_TABLE, selected_database, table_name)
        pass

    def valid_response_data(self, response):
        return True


class Action_OpenTableTabFormTreeItem(Action):

    def __init__(self, dialogue_message, tree_view, tab_table):
        super().__init__(dialogue_message)
        self.tree_view = tree_view
        self.tab_table = tab_table

    def request(self, data_object):
        """ Check database and table exist

        :param data_object:  None
        :return:             Status and response from server
        """

        db_name, table_name = self.tree_view.get_selected_item_and_parent_text()

        if db_name is None or table_name is None:
            return None

        return self.web_query.database_and_table_exist(db_name, table_name) # TODO: find out why if cant find the db and table :|

    def action(self, data_object, response_data):
        """ Opens a new tab with the selected table from database

        :param data_object:         None
        :param response_data:       None
        :return:                    None
        """

        db_name, table_name = self.tree_view.get_selected_item_and_parent_text()
        self.tab_table.add_tab( ui_tabTable.TAB_TYPE_TABLE, db_name, table_name )

    def valid_response_data(self, response):
        return True


class Action_TableColumns(Action):

    def __init__(self, dialog_message, tree_view, tab_table ):
        super().__init__(dialog_message)
        self.tree_view = tree_view
        self.tab_table = tab_table

    def request(self, data_object):
        """

        :param data_object:     None or empty {}
        :return:                request results
        """
        db_name, table_name = self.tree_view.get_selected_item_and_parent_text()
        return self.web_query.get_column_names(db_name, table_name)

    def action(self, data_object, response):
        """

        :param data_object:     None or empty {}
        :param response:        data from request
        :return:                None
        """

        # the data in the response contains all column data
        # [ col_id, name, type, can_be_null, default_value, primary_key, editable] (len 7)
        # editable IS NOT a sqlite value, it needs to be added by the user on the server side
        # and signals if the column can be edited or not.
        # if the value is not present then it is assumed that the column can be edited
        # we only need the 2nd element (col name) for the column names
        column_names = []       # list of column names
        column_params = []      # list of tuples containing column params (editable, type)
        for r in response:
            column_names.append( r[1] )
            if  len(r) == 7:
                column_params.append( (r[6], r[2], r[4] ) )
            else:
                column_params.append( (1, r[2], r[4]) )     # if the editable has not been set assume it to be editable

        db_name, table_name = self.tree_view.get_selected_item_and_parent_text()

        ui_table = self.tab_table.get_tab_ui_table(ui_tabTable.TAB_TYPE_TABLE, db_name, table_name)
        ui_table.set_columns( column_names, column_params )

    def valid_response_data(self, response):
        """Check that the data is a list of list, and that len nested list has a len of at least 6"""
        return type(response) is list and type(response[0]) is list and len(response[0]) >= 6

class Action_TableRows(Action):

    def __init__(self, dialog_message, tree_view, tab_table ):
        super().__init__(dialog_message)
        self.tab_table = tab_table
        self.tree_view = tree_view

    def request(self, data_object):
        """

        :param data_object:     None or empty {}. if tree_vew is set to not data object must contain keys 'database_name' & 'table_name'
        :return:                request results
        """
        if self.tree_view is not None:
            db_name, table_name = self.tree_view.get_selected_item_and_parent_text()
        else:
            db_name = data_object["database_name"]
            table_name = data_object["table_name"]

        return self.web_query.get_table_rows(db_name, table_name)

    def action(self, data_object, response):
        """

        :param data_object:     None or empty {}. if tree_vew is set to not data object must contain keys 'database_name' & 'table_name'
        :param response:        data from request
        :return:                None
        """

        if self.tree_view is not None:
            db_name, table_name = self.tree_view.get_selected_item_and_parent_text()
        else:
            db_name = data_object["database_name"]
            table_name = data_object["table_name"]

        ui_table = self.tab_table.get_tab_ui_table(ui_tabTable.TAB_TYPE_TABLE, db_name, table_name)
        ui_table.set_rows(response)


    def valid_response_data(self, response):
        return type(response) is list


class Action_updateTableRow(Action):

    def request(self, data_object):

        return self.web_query.edit_row(data_object["database_name"], data_object["table_name"],
                                       data_object["set_columns"], data_object["set_data"],
                                       data_object["where_columns"], data_object["where_data"])

    def action(self, data_object, response):
        """

        :param data_object:     dict with keys "database_name", "table_name",
                                               "set_columns"   , "set_data",
                                               "where_columns" , "where_data"
        :param response:        data from request
        :return:                None
        """
        pass

    def valid_response_data(self, response):
        return True


class Action_RemoveRowsFromTable(Action):

    def __init__(self, dialog_message, tab_table):
        super().__init__(dialog_message)
        self.tab_table = tab_table
        self.refresh_table_action = Action_TableRows(dialog_message, None, tab_table)

    def request(self, data_object):

        ui_table = self.tab_table.get_current_tab_table()[1]

        if ui_table is None:
            return WebQuerys.response_to_dict(404, "No database or table selected")
        elif ui_table.table_type is not ui_tabTable.TAB_TYPE_TABLE:
            return WebQuerys.response_to_dict(404, "Can not remove rows from new tables")

        rows_to_remove = ui_table.get_selected_rows()

        if len(rows_to_remove) == 0:
            return WebQuerys.response_to_dict(404, "Nothing Selected to be removed")

        where_values = ui_table.get_column_values_for_rows(0, rows_to_remove)
        where_column = ui_table.get_column_name(0)

        # TODO: fix limatation on server! hack for OR
        where_str = [" "+where_column+"=? OR"] * len(rows_to_remove)
        where_str[-1] = where_str[-1][:-5]      # remove the last 5 chars from the lsat element since the server will add =? back :)
        where_str = ''.join(where_str)          # like the todo says hacky

        return self.web_query.remove_row(ui_table.database_name, ui_table.table_name, [where_str], where_values)

    def action(self, data_object, response):
        """
                :param data_object:     None or empty
                :param response:        data from request
                :return:                None
        """
        # refresh the table.
        db_name, table_name = self.tab_table.get_database_and_table_name()
        self.refresh_table_action.run_action({"database_name": db_name, "table_name": table_name}, 1)

    def valid_response_data(self, response):
        return True


# derive for removeRows since its only the request that is different
class Action_InsertNewRow(Action_RemoveRowsFromTable):

    def request(self, data_object):

        ui_table = self.tab_table.get_current_tab_table()[1]

        if ui_table == None:
            return WebQuerys.response_to_dict(404, "No database or table selected")
        elif ui_table.table_type is not ui_tabTable.TAB_TYPE_TABLE:
            return WebQuerys.response_to_dict(404, "Can not remove rows from new tables")

        column_names, column_default_values = zip( *ui_table.get_default_values().items() )

        return self.web_query.insert_row(ui_table.database_name, ui_table.table_name, column_names, column_default_values)

class Action_AddTable(Action):

    def request(self, data_object):
        print("BBBBBBBBBBBBBBBBBBBBBIP", data_object)
        return self.web_query.new_table(data_object["database_name"], data_object["table_name"],
                                        data_object["column_names"], data_object["data_types"],
                                        data_object["data_lengths"], data_object["default_values"] )


    def action(self, data_object, response):
        print("Bip")
        pass

    def valid_response_data(self, response):
        return True