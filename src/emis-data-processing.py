import  json;
import pandas as pd;
from IPython.display import display
from mapper import get_mapping, map_data
from enums.resource_types import resource_types
import os

files_directory = "data"

def process_file(file_path):
    
    with open(file_path, 'r') as j:
        contents = json.loads(j.read())

    data = []
    for entry_data in contents["entry"]:
        resource_type = resource_types(entry_data["resource"]["resourceType"])
        mapping = get_mapping(resource_type)

        # Applying the mapping to the patient_json_data
        mapped_patient_data = map_data(mapping, entry_data)
        df = pd.DataFrame([mapped_patient_data])
        df.to_csv(f"test.csv", index=False)

for filename in os.listdir(os.path.abspath(files_directory)):
    if filename.endswith(".json"):        
        print(f"Processing {filename}...")
        process_file(os.path.join(files_directory, filename))
    else:
        print(f"{filename} skipped")
