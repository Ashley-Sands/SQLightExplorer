
class WebQuerys:

    def __init__(self):
        pass

    def open_database(self, db_name):
        pass

    def new_database(self, db_name):
        pass

    def new_table(self, table_name, columns, types):
        """ sends request to server to create new table

        :param table_name:  table name
        :param columns:     list of column names
        :param types:       sql column types
        :return:            None
        """
        pass

    def drop_table(self, table_name):
        pass

    def edit_value(self, table_name):
        pass

    def new_row(self, table_name):
        pass
