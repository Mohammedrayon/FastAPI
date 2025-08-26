import json
import os 
import pandas as pd
import uuid

def show_all_patients(file_path=os.path.abspath('data/patients.json')):
    """Reads a JSON file and returns its content as a dictionary."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def add_patient(new_data, file_path=os.path.abspath('data/patients.json')):
    """Appends new data to a JSON file."""
    data = show_all_patients(file_path)
    patient_id = "P" + str(uuid.uuid4().hex[:4]).upper()
    data[patient_id] = new_data
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    return new_data

def update_patient(patient_id, updated_data , file_path=os.path.abspath('data/patients.json')):
    """Updates an entry in a JSON file at a specific index."""
    data = show_all_patients(file_path)
    if patient_id in data:
        data[patient_id] = updated_data
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        return True
    return False    

def delete_patient(patient_id, file_path=os.path.abspath('data/patients.json')):
    """Deletes a key from a JSON file."""
    data = show_all_patients(file_path)
    if patient_id in data:
        del data[patient_id]
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        return True
    return False
