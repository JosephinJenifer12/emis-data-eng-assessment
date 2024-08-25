
from collections import defaultdict
from datetime import datetime
import os
from data_access.database import create_db_engine, insert_bulk_data
from data_mapper.helper import get_mapping, map_data
from data_model.helper import get_model
from enums.resource_types import resource_types
import json


class DataPipeline():
    def extract(self, filename):
        if filename.endswith(".json"):        
            print(f"Processing {filename}...")
            with open(filename, 'r', encoding="utf8") as j:
                try:
                    return json.loads(j.read())
                except ValueError as e:
                    print(f"Invalid json file: {filename}")
        else:
            print(f"{filename} skipped")

    def transform(self, file_content):
        bulk_data  = defaultdict(list)
        for entry_data in file_content["entry"]:
            resource_type = resource_types(entry_data["resource"]["resourceType"])
            if (resource_type == resource_types.Patient or
                resource_type == resource_types.Observation):
                print(f"{len(bulk_data[resource_type.value])} - Processing {resource_type}: {entry_data["resource"]["id"]}")
                mapping = get_mapping(resource_type)
                mapped_patient_data = map_data(mapping, entry_data)
                data_model = get_model(resource_type)(mapped_patient_data)
                bulk_data[resource_type.value].append(data_model)
        return bulk_data
    
    def load(self, bulk_data):        
        if bulk_data:
            db_engine = create_db_engine()
            insert_bulk_data(db_engine, bulk_data[resource_types.Patient.value])
            insert_bulk_data(db_engine, bulk_data[resource_types.Observation.value])

    def run(self, file_source_directory):
        start_time = datetime.now()
        for filename in os.listdir(os.path.abspath(file_source_directory)):
            json_content = self.extract(os.path.join(file_source_directory, filename))
            transformed_data = self.transform(json_content)
            self.load(transformed_data)

        print(f"Processing completed in {datetime.now() - start_time}")