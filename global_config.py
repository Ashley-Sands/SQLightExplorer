import json
import os

class GlobalConfig:

    FILE_NAME = "config.amsql"
    __CONFIG__ = {}

    @staticmethod
    def get(config_name):
        """Gets the config data for name"""
        if config_name.lower() in GlobalConfig.__CONFIG__:
            return GlobalConfig.__CONFIG__[config_name.lower()]
        else:
            print("Error: Config not found", config_name)
            return " ";

    @staticmethod
    def set(config_name, data):
        """Sets or adds (if not exist) to the global config"""
        GlobalConfig.__CONFIG__[config_name.lower()] = data

    @staticmethod
    def is_set(config_name):
        return config_name.lower() in GlobalConfig.__CONFIG__

    @staticmethod
    def save_to_file():

        file_str = json.dumps(GlobalConfig.__CONFIG__, indent=2)

        with open(GlobalConfig.FILE_NAME, "w") as file:
            file.write(file_str)


    @staticmethod
    def load_from_file():

        file_str = ""
        if os.path.exists(GlobalConfig.FILE_NAME):
            with open(GlobalConfig.FILE_NAME, "r") as file:
                file_str = file.read()

            GlobalConfig.__CONFIG__ = json.loads(file_str)

        else:
            print("No Config to load!")

