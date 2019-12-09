from global_config import GlobalConfig as Config
import http.client
import json

class WebQuerys:

    def __init__(self):
        self.connection = None

    @staticmethod
    def get_query_dict(database, table=None, sets=None, wheres=None, values=None):
        """ Creates dict to send to server

        :param database:    database name
        :param table:       table name
        :param sets:        tuple (set_columns, set_data)
        :param wheres:      tuple (where_columns, where_data)
        :param values:      tuple (value_columns, value_data)
        :return:            dict
        """
        dic = {"database": database}

        if table != None:
            dic["table"] = table

        if type(sets) is list or type(sets) is tuple:
            dic["set_columns"] = sets[0]
            dic["set_data"] = sets[1]

        if type(wheres) is list or type(wheres) is tuple:
            dic["where_columns"] = wheres[0]
            dic["where_data"] = wheres[1]

        if type(values) is list or type(values) is tuple:
            dic["value_columns"] = values[0]
            dic["value_data"] = values[1]

        return dic

    @staticmethod
    def response_to_dict(response_status, response_data):
        """ vaildates response for error handling

        :param responce_status:     servers status
        :param responce_data:       messages form server (json string)
        :return:                    correct response and data as dict
        """
        if response_status == 200 or response_status == "200":
            response = json.loads( response_data )
            response_status = response["status"]
            response_data = response["response"]

        return response_status, response_data


    def send_query(self, request_type, page, data_to_send):
        """ Sends the query to host

        :param request_type:    the type of request GET or POST
        :param page:            full page path of request
        :param data_to_send:    the data if any to send (dict to be serialized to json) (POST only)
        :return:                (status, response)
        """
        response = None
        response_data = None
        response_status = 404
        page = Config.get("remote_root") + page
        data = json.dumps(data_to_send)

        self.connection = http.client.HTTPConnection(Config.get("host"), Config.get("port"))

        try:
            # send GET request
            if request_type.upper() == "GET":
                self.connection.request("GET", page)
            # send POST request
            elif request_type.upper() == "POST":
                headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
                print(data)
                self.connection.request("POST", page, data.encode(), headers)

            else:
                response_status = 404
                response_data = "Error: their is not request type "+request_type.upper()

            print("Sending request: ", page)
            # get the response data from the request
            response = self.connection.getresponse()
            response_data = response.read().decode()
            response_status = response.status
        except:
            response_status = 408
            response_data = "Error: Connection timed out"

        self.connection.close()

        return response_status, response_data

    def open_database(self, db_name):
        """ Request to open the database to view the tables

        :param db_name: name of db
        :return:        tuple (response status, list of tables)
        """
        data = WebQuerys.get_query_dict( db_name )
        response_status, response_data = self.send_query("POST", "/open_database", data)

        return WebQuerys.response_to_dict( response_status, response_data )

    def new_database(self, db_name):
        """ Request a new database the data to view the tables

        :param db_name: name of db
        :return:        tuple (response status, list of tables)
        """
        data = WebQuerys.get_query_dict( db_name )
        response_status, response_data = self.send_query("POST", "/new_database", data)

        return WebQuerys.response_to_dict( response_status, response_data )


    def new_table(self, database_name, table_name, columns, types):
        """ sends request to server to create new table

        :param database_name:   database name
        :param table_name:      table name
        :param columns:         list of column names
        :param types:           sql column types
        :return:                None
        """
        pass

    def database_and_table_exist(self, db_name, table_name):
        """Queries if a database and table exist"""
        data = WebQuerys.get_query_dict(db_name, table_name)
        response_status, response_data = self.send_query("POST", "/table_exist", data)

        return WebQuerys.response_to_dict( response_status, response_data )

    def get_column_names(self, db_name, table_name):
        """ gets all columns from table

        :param database_name:
        :param table_name:
        :return:
        """
        data = WebQuerys.get_query_dict( db_name, table_name )
        response_status, response_data = self.send_query("POST", "/column_names", data)

        return WebQuerys.response_to_dict(response_status, response_data)

    def get_table_rows(self, db_name, table_name):
        """ gets all rows from table

            :param db_name:
            :param table_name:
            :return:
        """
        data = WebQuerys.get_query_dict(db_name, table_name)
        response_status, response_data = self.send_query("POST", "/table_rows", data)

        return WebQuerys.response_to_dict(response_status, response_data)

    def drop_table(self, db_name, table_name):

        data = WebQuerys.get_query_dict( db_name, table_name )
        response_status, response_data = self.send_query("POST", "/drop_table", data)

        return WebQuerys.response_to_dict( response_status, response_data )

    def edit_row(self, db_name, table_name, set_columns, set_values, where_columns, where_data):

        data = WebQuerys.get_query_dict(db_name, table_name, (set_columns, set_values), (where_columns, where_data))
        response_status, response_data = self.send_query("POST", "/update_row", data)

        return WebQuerys.response_to_dict(response_status, response_data)

    def insert_row(self, db_name, table_name, value_columns, value_data):

        data = WebQuerys.get_query_dict(db_name, table_name, values=(value_columns, value_data))
        response_status, response_data = self.send_query("POST", "/insert_row", data)

        return WebQuerys.response_to_dict( response_status, response_data )

    def remove_row(self, db_name, table_name, where_columns, where_data):

        data = WebQuerys.get_query_dict(db_name, table_name, wheres=(where_columns, where_data))
        response_status, response_data = self.send_query("POST", "/remove_row", data)

        return WebQuerys.response_to_dict(response_status, response_data)