from configparser import ConfigParser

def get_config(category,key):
    config=ConfigParser()
    # config.read("./config.ini")
    config.read("config_ini/config.ini")
    return config.get(category,key)
