from data_model.patient import Patient
from enums.resource_types import resource_types
from data_mapper.patient_mapper import patient_mapping
from data_mapper.observation_mapper import observation_mapping
import re

mapper_dict = {
    resource_types.Patient: patient_mapping,
    resource_types.Observation: observation_mapping
}

def get_mapping(resource_type):
    if not isinstance(resource_type, resource_types):
        raise TypeError('resource_type must be an instance of resource_types Enum')
    
    return mapper_dict.get(resource_type, None)

def get_nested_value(data, path):
    """Recursively access nested dictionary or list data using a string path."""
    keys = re.split(r'\.|\[|\]', path)
    keys = [key for key in keys if key]  # Filter out empty strings
    for key in keys:
        if isinstance(data, list):
            key = int(key)  # Convert to integer if accessing a list by index
        data = data[key]
    return data

def map_data(mapping, data):
    """Map data from JSON to a dictionary using a dynamic mapping."""
    mapped_data = {}
    for target_key, json_path in mapping.items():
        try:
            mapped_data[target_key] = get_nested_value(data, json_path)
        except (KeyError, IndexError, TypeError):
            mapped_data[target_key] = None  # Handle missing or incorrect paths gracefully
    return mapped_data
