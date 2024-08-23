from data_model.patient import Patient
from data_model.observation import Observation
from enums.resource_types import resource_types

model_dict = {
    resource_types.Patient: Patient,
    resource_types.Observation: Observation
}

def get_model(resource_type):
    if not isinstance(resource_type, resource_types):
        raise TypeError('resource_type must be an instance of resource_types Enum')
    
    return model_dict.get(resource_type, None)
