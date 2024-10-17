# Streamlit UI
st.title("Product Suggestion Generator")
'''
if st.button("Home"):
  st.write("Welcome to the Product Suggestion Generator!")
'''
#st.button("Model Suggestion"):
  # Input fields for product name, usage, and budget
product = st.text_input("What product/package do you want:")
budget = st.text_input("Enter you budget: ")
usage = st.text_input("Enter the usage: ")
requirement = st.text_input("Enter the requirement: ")

'''
  if st.button("Generate"):
    # Call the functions with the user inputs
    suggestion = suggestion_gen(budget, usage, requirement)

    # Display the results
    st.write(suggestion)

#if st.button("Image-based ")
'''