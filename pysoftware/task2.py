


import requests
import csv
import os
import pandas as pd

API_KEY = "ssfdsjfksjdhfgjfgvjdshgvshgkjsdlgvkjsdgjkl" # May not work since it is hypothetical like you said
BASE_URL = "https://pysoftware.com/v1" # But it would for a live endpoint

headers = {
    "X-API-KEY": API_KEY
}

def fetch_total_customers():
    """Retrieve the total number of customers."""
    response = requests.get(f"{BASE_URL}/customer_numbers", headers=headers)
    response.raise_for_status() 
    return int(response.text) 

def fetch_customer_address(customer_number):
    """Retrieve the address of a single customer."""
    url = f"{BASE_URL}/address_inventory/{customer_number}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def validate_address(address):
    """Validate and clean address data."""
    required_keys = ["id", "first_name", "last_name", "street", "postcode", "state", "country", "lat", "lon"]
    cleaned_address = {}
    
    for key in required_keys:
        if key not in address:
            cleaned_address[key] = None  
        else:
            if key in ["lat", "lon"]:
                cleaned_address[key] = float(address[key]) if isinstance(address[key], (int, float)) else None
            else:
                cleaned_address[key] = str(address[key]).strip() if address[key] else None

    return cleaned_address

def fetch_and_save_all_addresses():
    """Fetch all customer addresses, clean them, and save to CSV."""
    total_customers = fetch_total_customers()
    all_addresses = []
    
    for customer_number in range(1, total_customers + 1):
        address = fetch_customer_address(customer_number)
        validated_address = validate_address(address)
        all_addresses.append(validated_address)
    
    csv_filename = "customer_addresses.csv"
    csv_filepath = os.path.join(os.getcwd(), csv_filename)

    with open(csv_filepath, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=all_addresses[0].keys())
        writer.writeheader()
        writer.writerows(all_addresses)

    print(f"CSV file saved as '{csv_filename}' at path: {csv_filepath}")
    
    return csv_filepath, all_addresses

def display_addresses_table(csv_filepath):
    """Display addresses in a tabular form."""
    df = pd.read_csv(csv_filepath)
    print(df)


csv_path, addresses_list = fetch_and_save_all_addresses()
display_addresses_table(csv_path)
