import json
import os
import csv
from urllib.parse import urlparse


# Define the folder containing the JSON files
folder_path = "C:\\Users\\mslus\\Desktop\\Projekt-Przejsciowy\\Searches_2"

def extract_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return domain

# Function to extract 'url' and 'position' from the top 'organicSearch' results
def extract_data_from_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        data = json.load(file)

    extracted_data = []
    if 'organicResults' in data[0]:
        for result in data[0]['organicResults'][:100]:
            url = result.get('url', '')
            domain = extract_domain(url)
            position = result.get('position', 0)
            extracted_data.append({'url': url, 'domain': domain, 'position': position})

    return extracted_data

# Create a list to store the aggregated data
aggregated_data = []

# Process all JSON files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        extracted_data = extract_data_from_file(file_path)

        # Add the extracted data to the list
        aggregated_data.extend(extracted_data)

# Save the data to a CSV file
csv_file_path = "C:\\Users\\mslus\\Desktop\\Projekt-Przejsciowy\\output_2.csv"

with open(csv_file_path, 'w', newline='') as csv_file:
    fieldnames = ['url', 'domain', 'position']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    
    for item in aggregated_data:
        writer.writerow(item)

print("Data saved to CSV.")




