import json
import os
import csv
from urllib.parse import urlparse


folder_path = "C:\\Users\\mslus\\Desktop\\Projekt-Przejsciowy\\Wyniki-wyszukiwania"

def extract_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return domain

# Ekstrakcja URL i przypisanej mu pozycji
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

aggregated_data = []

for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        extracted_data = extract_data_from_file(file_path)

        # Add the extracted data to the list
        aggregated_data.extend(extracted_data)

csv_file_path = "C:\\Users\\mslus\\Desktop\\Projekt-Przejsciowy\\output_2.csv"

with open(csv_file_path, 'w', newline='') as csv_file:
    fieldnames = ['url', 'domain', 'position']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    
    for item in aggregated_data:
        writer.writerow(item)

print("Data saved to CSV.")




