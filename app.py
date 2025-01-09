import streamlit as st
from PIL import Image
import pytesseract
import json

def save_data_to_json(file_path, new_data):
    try:
        with open(file_path, "r") as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    if isinstance(existing_data, list):
        existing_data.append(new_data)
    else:
        raise ValueError("The JSON file must contain a list of items.")

    with open(file_path, "w") as file:
        json.dump(existing_data, file, indent=4)

picture = st.camera_input('Capture', disabled=False)

if picture:
    image = Image.open(picture)
    text = pytesseract.image_to_string(image)

    st.info("Extracted Text:")
    st.write(text)

    data = {"extracted_text": text}
    save_data_to_json('data.json', data)

    try:
        with open('data.json', 'r') as file:
            json_data = json.load(file)
        st.success("Saved Data:")
        st.json(json_data)
    except FileNotFoundError:
        st.error("Data file not found.")
