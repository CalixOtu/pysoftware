### TASK 1
This Python script validates and updates a JSON object containing "internet hubs" by ensuring each hub entry conforms to a predefined structure. It then assigns unique serial numbers from a specified range based on the last digit of each hub’s id.

Functionality:
Validation: The script first verifies that the JSON data contains an Internet_hubs list, where each hub entry includes both id and serial_number keys.
Serial Number Assignment: For valid data, the script assigns serial numbers to each hub based on the id. Serial numbers are generated within the range C25CTW00000000001470 to C25CTW00000000001478. The last digit of each hub's id (e.g., "mn1", "mn2", etc.) is used to map to the corresponding serial number in the range, creating unique assignments.

Libraries Used
json: Handles JSON operations, such as formatting and outputting JSON data. The json library is part of Python’s standard library and requires no external installation.
copy: Utilizes deepcopy from the copy module to create a complete copy of the JSON input object. This ensures that the original data remains unchanged while updates are applied to the copy.

### TASK 2
This Python script connects to a hypothetical API service to fetch and validate customer address data, saves the cleaned data to a CSV file, and displays the data in a tabular format.

Functionality
API Requests: Using the requests library, the script retrieves the total number of customers and each customer's address by making API calls with the required API key authentication.
Address Validation: Validates address fields to ensure required data fields are present and formatted correctly, handling missing fields as needed.
CSV Export: Saves the validated address data to a CSV file, stored in the working directory.
Tabular Display: Reads the CSV file into a pandas DataFrame for easy viewing of customer address data in a table format.
Libraries Used
requests: Handles HTTP requests to the API, retrieving customer information. Ensure the requests library is installed with pip install requests.
csv: Used to write data to a CSV file. Part of Python’s standard library.
os: Manages file paths and saves files in the working directory. Part of Python’s standard library.
pandas: Loads the CSV data for easy display in a tabular format. Ensure pandas is installed with pip install pandas.

###TASK 3
This Python script processes questions from a PDF file, parses them, and saves them to a Django database for a computer-based test (CBT) application. It extracts questions and multiple-choice options, validates them, and populates the QUESTION_TABLE in the database.

Functionality
PDF Extraction: The pdfplumber library is used to extract text content from each page of a PDF file.
Text Parsing with Regex: Using the re library, the extracted text is split by numbered questions, and each question’s main text and options (A through E) are parsed individually.
Database Population: Leveraging Django’s ORM and transaction.atomic(), each question and its options are saved to the QUESTION_TABLE model (Question). Predefined fields like category and multiple_quiz_use_subject are set to default or first instances of related objects.

Libraries Used
re: For regular expression operations to identify questions and answer options from the text.
pdfplumber: Extracts text content from PDF pages. Install it with pip install pdfplumber.
