# File responsible for initializing the module.
import os
import file_loader
import json
import process

if __name__ == "__main__":

    json_directory = "in"
    
    if not os.path.exists("out"):
        os.makedirs("out")
    
    names_list = file_loader.load_names_from_csv()
    names_2_list = file_loader.load_names_2_from_csv()
    last_names_list = file_loader.load_last_names_from_csv()
    adresses_list = file_loader.load_adresses_from_csv()
    cities_list = file_loader.load_cities_from_csv()
    
    for filename in os.listdir(json_directory):
        if filename.endswith(".json"):
            
            file_path = os.path.join(json_directory, filename)
            process.read_and_process_json(file_path, names_list, names_2_list, last_names_list, adresses_list, cities_list)
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)

            process.process_array_objects_recursive(data, names_list, names_2_list, last_names_list, adresses_list, cities_list)

            out_filename = os.path.basename(file_path)
            out_path = os.path.join("out", out_filename)

            processed_data = process.process_data_recursive(data, names_list, names_2_list, last_names_list, adresses_list, cities_list)
            processed_data = {key: value if value != "COLLECTION_NATURAL" else process.process_value_recursive(value, names_list, names_2_list, last_names_list, adresses_list, cities_list) for key, value in processed_data.items()}
            processed_data = {key: value if value != "COLLECTION_INTEGER" else process.process_value_recursive(value, names_list, names_2_list, last_names_list, adresses_list, cities_list) for key, value in processed_data.items()}
            processed_data = {key: value if value != "COLLECTION_DATE" else process.process_value_recursive(value, names_list, names_2_list, last_names_list, adresses_list, cities_list) for key, value in processed_data.items()}
            processed_data = {key: value if value != "COLLECTION_DATETIME" else process.process_value_recursive(value, names_list, names_2_list, last_names_list, adresses_list, cities_list) for key, value in processed_data.items()}
            processed_data = {key: value if value != "COLLECTION_FIRST_NAME_1" else process.process_value_recursive(value, names_list, names_2_list, last_names_list, adresses_list, cities_list) for key, value in processed_data.items()}
            processed_data = {key: value if value != "COLLECTION_FIRST_NAME_2" else process.process_value_recursive(value, names_list, names_2_list, last_names_list, adresses_list, cities_list) for key, value in processed_data.items()}
            processed_data = {key: value if value != "COLLECTION_LAST_NAME" else process.process_value_recursive(value, names_list, names_2_list, last_names_list, adresses_list, cities_list) for key, value in processed_data.items()}

            with open(out_path, 'w', encoding='utf-8') as out_file:
                json.dump(processed_data, out_file, indent=4, ensure_ascii=False)