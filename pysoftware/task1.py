

import json
from copy import deepcopy
import requests
import csv
import os
import pandas as pd
import re


def validate_and_assign_serial_numbers(data):
    base_serial = "C25CTW0000000000147"
    serial_range = [base_serial + str(i) for i in range(8, -1, -1)]
    
    if "Internet_hubs" not in data or not isinstance(data["Internet_hubs"], list):
        raise ValueError("Invalid schema: 'Internet_hubs' key is missing or not a list.")
    
    for hub in data["Internet_hubs"]:
        if "id" not in hub or "serial_number" not in hub:
            raise ValueError("Invalid schema: Each hub entry must contain 'id' and 'serial_number' keys.")
    
    updated_data = deepcopy(data) 
    for hub in updated_data["Internet_hubs"]:
        hub_id = hub["id"]
        if hub_id.startswith("mn") and hub_id[2:].isdigit():
            last_digit = int(hub_id[2:])
            serial_index = 8 - (last_digit % 10)
            hub["serial_number"] = serial_range[serial_index]
    
    return data, updated_data

original_data = {
    "comment": "Do NOT commit local changes to this file to source control",
    "Internet_hubs": [
        {"id": "men1", "serial_number": "C25CTW00000000001470"},
        {"id": "mn1", "serial_number": "<serial number here>"},
        {"id": "mn2", "serial_number": "<serial number here>"},
        {"id": "mn3", "serial_number": "<serial number here>"},
        {"id": "mn4", "serial_number": "<serial number here>"},
        {"id": "mn5", "serial_number": "<serial number here>"},
        {"id": "mn6", "serial_number": "<serial number here>"},
        {"id": "mn7", "serial_number": "<serial number here>"},
        {"id": "mn8", "serial_number": "<serial number here>"},
        {"id": "mn9", "serial_number": "<serial number here>"},
    ]
}


try:
    original, updated = validate_and_assign_serial_numbers(original_data)
    print("Original JSON Object:")
    print(json.dumps(original, indent=4))
    print("\nUpdated JSON Object:")
    print(json.dumps(updated, indent=4))
except ValueError as e:
    print(f"Validation Error: {e}")
