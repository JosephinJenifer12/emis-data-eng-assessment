import json
from data_access.database import create_db_engine, insert_data
from data_mapper.helper import get_mapping, map_data
from data_model.helper import get_model
from enums.resource_types import resource_types
import os
from constants import files_directory
from time import sleep

sleep(10)

db_engine = create_db_engine()

def process_file(file_path):    
    with open(file_path, 'r') as j:
        contents = json.loads(j.read())

    for entry_data in contents["entry"]:
        resource_type = resource_types(entry_data["resource"]["resourceType"])
        if resource_type == resource_types.Patient:
            print(f"Processing {resource_type}")
            mapping = get_mapping(resource_type)
            mapped_patient_data = map_data(mapping, entry_data)
            model = get_model(resource_type)(mapped_patient_data)
            insert_data(db_engine, model)

for filename in os.listdir(os.path.abspath(files_directory)):
    if filename.endswith(".json"):        
        print(f"Processing {filename}...")
        process_file(os.path.join(files_directory, filename))
    else:
        print(f"{filename} skipped")
