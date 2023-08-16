# File responsible for module configuration settings.
import os
import json

# Function responsible for loading parameters from the config.json file.
def load_config():
    config_path = os.path.join("parameters", "config.json")
    with open(config_path, "r", encoding="utf-8") as config_file:
        config_data = json.load(config_file)
        return config_data

# Function responsible for loading the value of a specific attribute in a json file.
def get_nested_value(data_dict, keys, default=None):
    keys = keys.split(".")
    value = data_dict
    for key in keys:
        if isinstance(value, dict) and key in value:
            value = value[key]
        else:
            return default
    return value