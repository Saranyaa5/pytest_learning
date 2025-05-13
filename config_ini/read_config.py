# from configparser import ConfigParser

# def get_config(category,key):
#     config=ConfigParser()
#     config.read("./config.ini")
#     return config.get(category,key)

from configparser import ConfigParser
import os

def get_config(category, key):
    config = ConfigParser()
    # Get path relative to this script's location
    config_path = os.path.join(os.path.dirname(__file__), "config.ini")
    config.read(config_path)
    return config.get(category, key)
