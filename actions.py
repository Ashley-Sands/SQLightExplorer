from web_querys import WebQuerys


class FakeDialog:
    """Allows objects use the actions that send a dialog window rather than values.
       it like Mock Dialog Data"""
    def __init__(self, text):
        self.text = text

class Action:

    def __init__(self, dialog_message):
        self.dialog_message = dialog_message
        self.web_query = WebQuerys()

    def request(self, data_object):
        """

        :return: request response
        """
        pass

    def run_action(self, data_object, accepted):  # should be run_action
        """ Runs the action handling serveer responces

        :param data_object:  Object that contains all data for the action
        :param accepted:     Alows binding to buttons (set to 1 if not button action)
        :return:
        """

        if accepted == 0:
            return

        response = self.request(data_object)

        if response is None: # in the case of response being none it will handle its own error messages :)
            return

        if str(response[0]) == "404":
            self.dialog_message.set_message(response[1])
            self.dialog_message.new_window()
        elif str(response[0]) == "408":
            self.dialog_message.set_message("Error: Connection Timed Out :(")
            self.dialog_message.new_window()
        elif not self.valid_response_data(response[1]):
            self.dialog_message.set_message("Error: Invalid response :(")
            self.dialog_message.new_window()
        else:
            self.action(data_object, response[1])

    def action(self, data_object, response_data):
        pass

    def valid_response_data(self, response):
        """ Checks if response is vails (needs overriding)"""
        return False;

class Action_NewDatabase(Action):

    def __init__(self, dialog_message, tree_view):
        super().__init__(dialog_message)
        self.tree_view = tree_view

    def request(self, dialog):
        return self.web_query.new_database( dialog.text )

    def action(self, dialog, response):
        print("GGGGGGGgggggg", dialog.text)
        # Add the data to the tree
        self.tree_view.add_tree_item(None, dialog.text)  # add database
        print("GGGGGGGgggggg")

    def valid_response_data(self, response):
        return True

class Action_OpenDatabase(Action_NewDatabase):

    def request(self, dialog):
        return self.web_query.open_database( dialog.text )

    def action(self, dialog, response):

        # Add the data to the tree
        super().action(dialog, response)
        for r in response:
            self.tree_view.add_tree_item(dialog.text, r)

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

        self.tree_widget.takeTopLevelItem( self.tree_widget.indexOfTopLevelItem(self.database) )
        print("Hellooooo")
        self.refresh_database_action.run_action(FakeDialog(database_name), 1)
        print(":)")

    def valid_response_data(self, response):
        return True

class Action_TableColumns(Action):

    def __init__(self, dialog_message, tab_table ):
        super().__init__(dialog_message)
        self.tab_table = tab_table

    def request(self, data_object):
        """

        :param data_object:     dict with keys 'database_name' and 'table_name'
        :return:                request results
        """
        return self.web_query.get_column_names(data_object["database_name"], data_object["table_name"])

    def action(self, data_object, response):
        """

        :param data_object:     dict with keys 'database_name' and 'table_name'
        :param response:        data from request
        :return:                None
        """

        # the data in the response contains all column data [ col_id, name, type, can_be_null, default_value, primary_key, editable] (len 7)
        # editable IS NOT a sqlite value, it needs to be added by the user on the server side and signals if the column can be edited or not.
        # if the value is not present then it is assumed that the column can be edited
        # we only need the 2nd element (col name) for the column names
        column_names = []       # list of column names
        column_params = []      # list of tuples containing column params (editable, type)
        for r in response:
            column_names.append( r[1] )
            if  len(r) == 7:
                column_params.append( (r[6], r[2] ) )
            else:
                column_params.append( (1, r[2]) )           # if the editable has not been set assume it to be editable

        self.tab_table.set_table_columns("table:"+data_object["table_name"], column_names, column_params)

    def valid_response_data(self, response):
        """Check that the data is a list of list, and that len nested list has a len of at least 6"""
        return type(response) is list and type(response[0]) is list and len(response[0]) >= 6

class Action_TableRows(Action):

    def __init__(self, dialog_message, tab_table ):
        super().__init__(dialog_message)
        self.tab_table = tab_table

    def request(self, data_object):
        """

        :param data_object:     dict with keys 'database_name' and 'table_name'
        :return:                request results
        """
        return self.web_query.get_table_rows(data_object["database_name"], data_object["table_name"])

    def action(self, data_object, response):
        """

        :param data_object:     dict with keys 'database_name' and 'table_name'
        :param response:        data from request
        :return:                None
        """

        self.tab_table.set_table_rows("table:"+data_object["table_name"], response)

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
