from global_config import GlobalConfig as Config
import http.client
import json

class WebQuerys:

    def __init__(self):
        self.connection = None

    @staticmethod
    def get_query_dict(database, table=None):
        """Creates dict to send to server"""
        dic = {"database": database}

        if table != None:
            dic["table"] = table

        return dic

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

            print("Sending", response_data, "request: ", page)
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
        response_status, response_data = self.send_query("POST", "/open_database", db_name)

        if response_status == 200 or response_status == "200":
            response = json.loads( response_data )
            response_status = response["status"]
            response_data = response["response"]

        return response_status, response_data

    def new_database(self, db_name):
        """ Request a new database the data to view the tables

        :param db_name: name of db
        :return:        tuple (response status, list of tables)
        """
        response_status, response_data = self.send_query("POST", "/new_database", db_name)

        if response_status == 200 or response_status == "200":
            response = json.loads( response_data )
            response_status = response["status"]
            response_data = response["response"]

        return response_status, response_data

    def new_table(self, table_name, columns, types):
        """ sends request to server to create new table

        :param table_name:  table name
        :param columns:     list of column names
        :param types:       sql column types
        :return:            None
        """
        pass

    def get_column_names(self, table_name):
        pass

    def get_table_rows(self, table_name):
        pass

    def drop_table(self, table_name):
        pass

    def edit_value(self, table_name):
        pass

    def new_row(self, table_name):
        pass
