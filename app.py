import streamlit as st

# Title of the app
st.title("Streamlit Backend")

# Get query parameters from the URL
query_params = st.experimental_get_query_params()

# Check if data is received
if "name" in query_params and "age" in query_params:
    name = query_params["name"][0]
    age = query_params["age"][0]
    st.write(f"Received data: Name = {name}, Age = {age}")

    # Process the data (e.g., save to a database or perform calculations)
    response = {"status": "success", "message": f"Hello {name}, you are {age} years old!"}
else:
    response = {"status": "error", "message": "No data received"}

# Display the response
st.write("Response:", response)

# Store the response in session state
st.session_state["response"] = response
