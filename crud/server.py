import os
from fastapi import FastAPI , HTTPException
from helper_functions import (
    show_all_patients,
    add_patient,
    update_patient,
    delete_patient
)

app = FastAPI()

@app.get('/')
async def hello():
    return {"message": "Patient Management System API is running"}

@app.get('/patients')
async def get_patients():
    patients =  show_all_patients()
    return {"patients": patients}

@app.post('/patients/add')
async def add_patient_endpoint(patient: dict):
    added = add_patient(new_data=patient)
    return {"message": "Patient added successfully"}

@app.put('/patients/update/{patient_id}')
async def update_patient_endpoint(patient_id: str, updated_data: dict):
    updated = update_patient(patient_id=patient_id, updated_data=updated_data)
    if updated:
        return {"message": "Patient updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Patient not found")
    
@app.delete('/patients/delete/{patient_id}')
async def delete_patient_endpoint(patient_id: str):
    deleted = delete_patient(patient_id=patient_id)
    if deleted:
        return {"message": "Patient deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Patient not found")
