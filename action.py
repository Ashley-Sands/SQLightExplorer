from web_querys import WebQuerys

class Action:

    def __init__(self, dialog_message, tree_view):
        self.dialog_message = dialog_message
        self.tree_view = tree_view

    def dialog_action(self, dialog, accepted):

        if accepted == 0:
            return

        web_query = WebQuerys()

        response = web_query.open_database(dialog.text)

        if str(response[0]) == "404":
            self.dialog_message.set_message("Error: Database Not Found")
            self.dialog_message.new_window()
        elif str(response[0]) == "408":
            self.dialog_message.set_message("Error: Connection Timed Out :(")
            self.dialog_message.new_window()
        else:
            # Add the data to the tree
            self.tree_view.add_tree_item(None, dialog.text)  # add database
            for r in response[1]:
                self.tree_view.add_tree_item(dialog.text, r)



