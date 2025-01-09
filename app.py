import streamlit as st
from PIL import Image
import pytesseract
import json

# Set the path for Tesseract-OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to save data to JSON file
def save_data_to_json(file_path, new_data):
    try:
        # Try to read the existing data from the file
        with open(file_path, "r") as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn't exist or is invalid, initialize as an empty list
        existing_data = []

    # Ensure existing data is a list
    if isinstance(existing_data, list):
        existing_data.append(new_data)
    else:
        raise ValueError("The JSON file must contain a list of items.")

    # Write the updated data back to the file
    with open(file_path, "w") as file:
        json.dump(existing_data, file, indent=4)

# Streamlit app
st.title("OCR Text Extraction and Storage")

# Capture an image from the camera
picture = st.camera_input('Capture an Image')

if picture:
    # Open the image from the captured input
    image = Image.open(picture)
    
    # Extract text using pytesseract
    text = pytesseract.image_to_string(image)
    
    # Display the extracted text
    st.info("Extracted Text:")
    st.write(text)
    
    # Save the extracted text to a JSON file
    data = {"extracted_text": text}
    save_data_to_json('data.json', data)
    
    # Load and display the saved JSON data
    try:
        with open('data.json', 'r') as file:
            json_data = json.load(file)
        st.success("Saved Data:")
        # st.json(json_data)
    except FileNotFoundError:
        st.error("Data file not found.")

with st.sidebar :
    with open('data.json','r') as f:
        data = json.load(f)
    for line in data:
        st.code(line["extracted_text"])
        
