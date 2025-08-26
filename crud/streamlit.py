import streamlit as st
import requests 
import pandas as pd

API_URL = "http://localhost:8000"
st.title("Patient Management System")
st.write("CRUD Operations with FastAPI and Streamlit for Patient Management")

if 'show_patients' not in st.session_state:
    st.session_state.show_patients = False

if 'add_patient' not in st.session_state:
    st.session_state.add_patient = False

if 'update_patient' not in st.session_state:
    st.session_state.update_patient = False

if 'delete_patient' not in st.session_state:
    st.session_state.delete_patient = False    



col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("All Patients"):
        st.session_state.show_patients = True
        st.session_state.add_patient = False
        st.session_state.update_patient = False
        st.session_state.delete_patient = False

with col2:
    if st.button("Add Patient"):
        st.session_state.add_patient = True
        st.session_state.show_patients = False
        st.session_state.update_patient = False
        st.session_state.delete_patient = False

with col3:
    if st.button("Update Patient"):
        st.session_state.update_patient = True
        st.session_state.show_patients = False
        st.session_state.add_patient = False
        st.session_state.delete_patient = False

with col4:
    if st.button("Delete Patient"):
        st.session_state.delete_patient = True
        st.session_state.show_patients = False
        st.session_state.add_patient = False
        st.session_state.update_patient = False

if st.session_state.show_patients:
    st.subheader("All Patients")
    response = requests.get(f"{API_URL}/patients")
    if response.status_code == 200:
        patients = response.json().get("patients", {})
        df = pd.DataFrame.from_dict(patients , orient='index')
        st.dataframe(df)
    else:
        st.write("Error fetching patients")

elif st.session_state.add_patient:
    st.subheader("Add New Patient")
    with st.form("add_patient_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        gender = st.text_input("Gender")
        medical_history = st.text_area("Medical History")
        submitted = st.form_submit_button("Add Patient")
        if submitted:
            new_patient = {
                "name": name,
                "age": age,
                "gender": gender,
                "medical_history": medical_history.split(",")
            }
            response = requests.post(f"{API_URL}/patients/add", json=new_patient)
            if response.status_code == 200:
                st.success("Patient added successfully")
            else:
                st.error("Error adding patient")


elif st.session_state.update_patient:
    st.subheader("Update Patient")
    with st.form("update_patient_form"):
        patient_id = st.text_input("Patient ID (e.g., P1234)")
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        gender = st.text_input("Gender")
        medical_history = st.text_area("Medical History")
        submitted = st.form_submit_button("Update Patient")
        if submitted:
            updated_patient = {
                "name": name,
                "age": age,
                "gender": gender,
                "medical_history": medical_history.split(",")
            }
            response = requests.put(f"{API_URL}/patients/update/{patient_id}", json=updated_patient)
            response = requests.put(f"{API_URL}/patients/update/{patient_id}", json=updated_patient)

            if response.status_code == 200:
                st.success(response.json().get("message", "Patient updated successfully"))
            else:
                st.error(f"Error {response.status_code}: {response.json().get('detail', 'Unknown error')}")

elif st.session_state.delete_patient:
    st.subheader("Delete Patient")
    with st.form("delete_patient_form"):
        patient_id = st.text_input("Patient ID (e.g., P1234)")
        submitted = st.form_submit_button("Delete Patient")
        if submitted:
            response = requests.delete(f"{API_URL}/patients/delete/{patient_id}")
            if response.status_code == 200:
                st.success(response.json().get("message", "Patient deleted successfully"))
            else:
                st.error(f"Error {response.status_code}: {response.json().get('detail', 'Unknown error')}")

