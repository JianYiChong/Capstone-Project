import streamlit as st
from PIL import Image

# Define the functions for each page
def home():
    st.write("Welcome to the home page")

    #st.image("./ITdevices.png")
    
    #image = Image.open('content/IT deives.png')
    #st.image(image, caption = 'IT Devices')
    
    #st.image("ITdevices.jpg", caption="") 
    

def product():
    st.write("Welcome to the product suggestion page")
     
    product = st.text_input("What product/package do you want:")
    budget = st.text_input("Enter your budget:")
    usage = st.text_input("Enter the usage:")
    requirement = st.text_input("Enter the requirement:")

    if st.button("Generate"):
        #suggestion = suggestion_gen(budget, usage, requirement)  
        st.write(suggestion)

def image():
    st.write("Welcome to the image-based product search page")
    st.write("Please upload an image of the product you want to search for")

    if st.button("Upload"):
        Image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
        
        #Image = it_product_analysis(image)
        #st.image(Image)

def email():
    st.write("Welcome to the email section")
    email = st.text_input("Enter your email:")


# Page navigation using a sidebar
page = st.sidebar.selectbox("Choose a page", ["Home", "Product Suggestion", "Image-based Product Search", "Email"])

# Show the selected page
if page == "Home":
    home()
elif page == "Product Suggestion":
    product()
elif page == "Image-based Product Search":
    image()
elif page == "Email":
    email()