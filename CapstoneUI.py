import os
import streamlit as st 
from openai import OpenAI
#from suggestion_gen import suggestion_gen

from streamlit_option_menu import option_menu

client = OpenAI(api_key = os.environ['OPENAI_API_KEY'])


# Create a horizontal navigation menu
selected = option_menu(
    menu_title="Main Menu",
    options=["Home", "Product", "Upload", "Email"],
    icons=['house', 'search', 'cloud-upload', 'email'],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

# Home Section
if selected == "Home":
    st.title("Welcome to the Home Page")
    st.write("This is the home page of the app.")

# Product Suggestion Section
if selected == "Product Suggestion":
    st.title("Product Suggestion")

    # Input fields for product suggestion
    product = st.text_input("What product/package do you want:")
    budget = st.text_input("Enter your budget:")
    usage = st.text_input("Enter the usage:")
    requirement = st.text_input("Enter the requirement:")

   

# Upload Section
elif selected == "Upload":
    st.title("Upload Section")
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

# Email Section
if selected == "Email":
    st.title("Enter Email Section")
    email = st.text_input("Enter your email:")
    if st.button("Submit"):
        st.write(f"Email submitted: {email}")


