# File responsible for loading the input files.

def load_names_from_csv():
    with open("examples/first_name_1.csv", "r", encoding="utf-8") as csv_file:
        names_line = csv_file.read()
        names = [name.strip() for name in names_line.split(",")]
        return names

def load_names_2_from_csv():
    with open("examples/first_name_2.csv", "r", encoding="utf-8") as csv_file:
        names_line = csv_file.read()
        names = [name.strip() for name in names_line.split(",")]
        return names

def load_last_names_from_csv():
    with open("examples/last_name.csv", "r", encoding="utf-8") as csv_file:
        last_names_line = csv_file.read()
        last_names = [last_name.strip() for last_name in last_names_line.split(",")]
        return last_names

def load_adresses_from_csv():
    with open("examples/address.csv", "r", encoding="utf-8") as csv_file:
        adresses_line = csv_file.read()
        adresses = [adresses.strip() for adresses in adresses_line.split(",")]
        return adresses
    
def load_cities_from_csv():
    with open("examples/city.csv", "r", encoding="utf-8") as csv_file:
        cities_line = csv_file.read()
        cities = [cities.strip() for cities in cities_line.split(",")]
        return cities
    
