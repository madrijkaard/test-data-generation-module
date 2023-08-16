# File responsible for generating random values of different types.
import random
import config
import default
import hashlib
import string
from datetime import datetime, timedelta

# Function responsible for generating random natural numbers.
def generate_random_natural():
    return random.randint(1, 10)

# Function responsible for generating random integers.
def generate_random_integer():
    return random.randint(-99999, 99999)

# Function responsible for generating random dates.
def generate_random_date():
    start_date = datetime(2000, 1, 1)
    end_date = datetime(2023, 12, 31)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime('%d/%m/%Y')

# Function responsible for generating random timestamps.
def generate_random_datetime():
    random_datetime = datetime(2000, 1, 1) + timedelta(
        seconds=random.randint(0, int((datetime.now() - datetime(2000, 1, 1)).total_seconds()))
    )
    return random_datetime.strftime('%d/%m/%Y %H:%M:%S')

# Function responsible for generating random male names.
def generate_random_name(names_list):
    return random.choice(names_list)

# Function responsible for generating random female names.
def generate_random_name_2(names_2_list):
    return random.choice(names_2_list)

# Function responsible for generating random last names.
def generate_random_last_names(last_names_list):
    return random.sample(last_names_list, 2)

# Function responsible for generating random addresses.
def generate_random_adresses(adresses_list):
    return random.choice(adresses_list)

# Function responsible for generating random cities.
def generate_random_cities(cities_list):
    return random.choice(cities_list)

# Function responsible for generating random dates.
def generate_random_date_list():
    config_data = config.load_config()
    date_collection = config.get_nested_value(config_data, "range.date_collection", default.RANGE)
    return [generate_random_date() for _ in range(date_collection)]

# Function responsible for generating random timestamps.
def generate_random_datetime_list():
    config_data = config.load_config()
    datetime_collection = config.get_nested_value(config_data, "range.datetime_collection", default.RANGE)
    return [generate_random_datetime() for _ in range(datetime_collection)]

def generate_random_hash():
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    hasher = hashlib.sha256()
    hasher.update(random_string.encode('utf-8'))
    random_hash = hasher.hexdigest()
    return random_hash