# File responsible for processing the output json file.
import os
import json
import config
import generator
import default

def process_value_recursive(value, names_list, names_2_list, last_names_list, adresses_list, cities_list):

    config_data = config.load_config()

    if isinstance(value, str):
        if value == "HASH":
            return generator.generate_random_hash()
        if value == "NATURAL":
            return generator.generate_random_natural()
        if value == "INTEGER":
            return generator.generate_random_integer()
        if value == "DATE":
            return generator.generate_random_date()
        if value == "DATETIME":
            return generator.generate_random_datetime()
        if value == "FIRST_NAME_1":
            return generator.generate_random_name(names_list)
        if value == "FIRST_NAME_2":
            return generator.generate_random_name_2(names_2_list)
        if value == "LAST_NAME":
            last_names = generator.generate_random_last_names(last_names_list)
            return " ".join(last_names)
        if value == "ADRESSES":
            return generator.generate_random_adresses(adresses_list)
        if value == "CITY":
            return generator.generate_random_cities(cities_list)
        if value == "COLLECTION_NATURAL":
            natural_collection = config.get_nested_value(config_data, "range.natural_collection", default.RANGE)
            return [generator.generate_random_natural() for _ in range(natural_collection)]
        if value == "COLLECTION_INTEGER":
            integer_collection = config.get_nested_value(config_data, "range.integer_collection", default.RANGE)
            return [generator.generate_random_integer() for _ in range(integer_collection)]
        if value == "COLLECTION_DATE":
            return generator.generate_random_date_list()
        if value == "COLLECTION_DATETIME":
            return generator.generate_random_datetime_list()
        if value == "COLLECTION_FIRST_NAME_1":
            first_name_1_collection = config.get_nested_value(config_data, "range.first_name_1_collection", default.RANGE)
            return [generator.generate_random_name(names_list) for _ in range(first_name_1_collection)]
        if value == "COLLECTION_FIRST_NAME_2":
            first_name_2_collection = config.get_nested_value(config_data, "range.first_name_2_collection", default.RANGE)
            return [generator.generate_random_name_2(names_2_list) for _ in range(first_name_2_collection)]
        if value == "COLLECTION_LAST_NAME":
            last_name_collection = config.get_nested_value(config_data, "range.last_name_collection", default.RANGE)
            return [' '.join(last_names) for last_names in ([last_name1, last_name2] for last_name1, last_name2 in (generator.generate_random_last_names(last_names_list) for _ in range(last_name_collection)))]
    elif isinstance(value, dict):
        return process_data_recursive(value, names_list, names_2_list, last_names_list, adresses_list, cities_list)
    elif isinstance(value, list):
        return [process_value_recursive(item, names_list, names_2_list, last_names_list, adresses_list, cities_list) for item in value]
    return value

def process_data_recursive(data, names_list, names_2_list, last_names_list, adresses_list, cities_list):
    processed_data = {}
    for key, value in data.items():
        processed_data[key] = process_value_recursive(value, names_list, names_2_list, last_names_list, adresses_list, cities_list)
    return processed_data

def read_and_process_json(file_path, names_list, names_2_list, adresses_list, last_names_list, cities_list):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        
        out_filename = os.path.basename(file_path)
        out_path = os.path.join("out", out_filename)
        
        processed_data = process_data_recursive(data, names_list, names_2_list, adresses_list, last_names_list, cities_list)
        
        with open(out_path, 'w', encoding='utf-8') as out_file:
            json.dump(processed_data, out_file, indent=4, ensure_ascii=False)

def process_array_objects_recursive(data, names_list, names_2_list, last_names_list, adresses_list, cities_list):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, list):
                if isinstance(value[0], dict):
                    array_size = default.ARRAY_OBJECT
                    data[key] = [process_value_recursive(value[0], names_list, names_2_list, last_names_list, adresses_list, cities_list) for _ in range(array_size)]
            elif isinstance(value, dict):
                process_array_objects_recursive(value, names_list, names_2_list, last_names_list, adresses_list, cities_list)
    elif isinstance(data, list):
        for item in data:
            process_array_objects_recursive(item, names_list, names_2_list, last_names_list, adresses_list, cities_list)