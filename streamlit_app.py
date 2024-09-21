import streamlit as st

# Define the Streamlit app
def app():
    st.title("Animal-10 Image Classification")

    # Add a file uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])


# Run the app
if __name__ == "__main__":
    app()
