class GlobalConfig:

    __CONFIG__ = {}

    @staticmethod
    def get(config_name):
        """Gets the config data for name"""
        if config_name.lower() in GlobalConfig.__CONFIG__:
            return GlobalConfig.__CONFIG__[config_name.lower()]

    @staticmethod
    def set(config_name, data):
        """Sets or adds (if not exist) to the global config"""
        GlobalConfig.__CONFIG__[config_name.lower()] = data
