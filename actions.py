from web_querys import WebQuerys

class Action:

    def __init__(self, dialog_message, message404="Error: Not Found"):
        self.dialog_message = dialog_message
        self.message404 = message404
        self.web_query = WebQuerys()

    def request(self, dialog):
        """

        :return: request responce
        """
        pass

    def dialog_action(self, dialog, accepted):
        if accepted == 0:
            return

        response = self.request(dialog)

        if str(response[0]) == "404":
            self.dialog_message.set_message(self.message404)
            self.dialog_message.new_window()
        elif str(response[0]) == "408":
            self.dialog_message.set_message("Error: Connection Timed Out :(")
            self.dialog_message.new_window()
        else:
            self.action(dialog, response[1])

    def action(self, dialog, response_data):
        pass


class Action_NewDatabase(Action):

    def __init__(self, dialog_message, tree_view, message404="Not Found"):
        super().__init__(dialog_message, message404)
        self.tree_view = tree_view

    def request(self, dialog):
        return self.web_query.new_database(dialog.text)

    def action(self, dialog, response):

        # Add the data to the tree
        self.tree_view.add_tree_item(None, dialog.text)  # add database


class Action_OpenDatabase(Action_NewDatabase):

    def request(self, dialog):
        return self.web_query.open_database(dialog.text)

    def action(self, dialog, response):

        # Add the data to the tree
        super().action(dialog, response)
        for r in response:
            self.tree_view.add_tree_item(dialog.text, r)




