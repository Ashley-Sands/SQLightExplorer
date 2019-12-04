from web_querys import WebQuerys

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

        # Add the data to the tree
        self.tree_view.add_tree_item(None, dialog.text)  # add database

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

        # the data in the response contains all column data (ie, id, name, type, ...)
        # we only need the 2nd element (col name) for the column names
        column_names = []
        for r in response:
            column_names.append(r[1])

        self.tab_table.set_table_columns("table:"+data_object["table_name"], column_names)

    def valid_response_data(self, response):
        return type(response) is list and type(response[0]) is list
