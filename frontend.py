import streamlit as st
import requests

st.title("Image Describer with Gemini")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image', use_container_width=True)
    
    if st.button('Describe Image'):
        # Prepare the file to send to Flask
        files = {"image": uploaded_file.getvalue()}
        
        with st.spinner('Asking Gemini...'):
            try:
                # Hit the Flask endpoint
                response = requests.post("http://127.0.0.1:5000/describe", files=files)
                
                if response.status_code == 200:
                    description = response.json().get("description")
                    st.success("Description:")
                    st.write(description)
                else:
                    st.error(f"Error: {response.status_code}")
            except Exception as e:
                st.error(f"Could not connect to backend: {e}")