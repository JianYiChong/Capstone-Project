import streamlit as st

# Define your functions to generate content

def suggestion_gen(budget, usage, requirement):
  system_prompt = '''
  You are a IT device suggestion generator. Your objective is to assist users—especially those lacking technical knowledge—in
selecting suitable personal or commercial IT devices tailored to their needs and budget.
  Provide the needed  product or list of customised suggestions based on user's requirement.
  '''
  prompt = f'My budget is RM{budget}, my mainly usage is {usage}, I need to {requirement}'

  response = client.chat.completions.create(
      model = 'gpt-4o-mini',
      messages = [
          {'role': 'system', 'content': ''},
          {'role': 'user', 'content': prompt}
      ],
      temperature = 1.1,
      max_tokens = 2000
  )
  return response.choices[0].message.content
    


# Streamlit UI
st.title("Product Suggestion Generator")

# Input fields for product name, usage, and budget
requirement = st.text_input("Enter the requirement")
usage = st.text_input("Enter the usage")
budget = st.text_input("Enter your budget")

# Button to generate the outputs
if st.button("Generate"):
    # Call the functions with the user inputs
    suggestion = suggestion_gen(budget, usage, requirement)



    # Display the results
    st.write(suggestion)

    
    



















import requests

def fetch_devices(api_url, requirements):
    """
    Fetches IT devices from the API based on user requirements.

    Parameters:
        api_url (str): The URL of the API to call.
        requirements (dict): The user's requirements and budget.

    Returns:
        list: A list of devices with their details including price.
    """
    response = requests.post(api_url, json=requirements)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()  # Assuming the response is in JSON format

def compare_device_prices(devices):
    """
    Compares the prices of devices and returns the cheapest and most expensive ones.

    Parameters:
        devices (list): A list of devices with price information.

    Returns:
        tuple: (cheapest_device, most_expensive_device)
    """
    if not devices:
        return None, None  # Return None if the list is empty

    # Assuming each device has a 'name' and 'price' key
    cheapest_device = min(devices, key=lambda x: x['price'])
    most_expensive_device = max(devices, key=lambda x: x['price'])

    return cheapest_device, most_expensive_device

def main(api_url, requirements):
    """
    Main function to fetch devices and compare their prices.

    Parameters:
        api_url (str): The URL of the API to call.
        requirements (dict): The user's requirements and budget.
    """
    try:
        devices = fetch_devices(api_url, requirements)
        cheapest_device, most_expensive_device = compare_device_prices(devices)

        print("Cheapest Device:", cheapest_device)
        print("Most Expensive Device:", most_expensive_device)

    except requests.RequestException as e:
        print(f"Error fetching devices: {e}")

# Example usage
if __name__ == "__main__":
    api_url = "https://example.com/api/devices"  # Replace with your API URL
    user_requirements = {
        "usage": "office",
        "budget": 1000,
        "specific_requirements": {
            "ram": "16GB",
            "storage": "512GB SSD"
        }
    }

    main(api_url, user_requirements)
