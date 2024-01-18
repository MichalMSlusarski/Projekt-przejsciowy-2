from apify_client import ApifyClient
import json
import os
from datetime import datetime
import time

client = ApifyClient("apify_api_vOJ7wRY9vmrXaCvvrP38MwfPfsL0BE3FvRrr")

query = "psychoterapia warszawa"

run_input = {
    "queries": query,
    "maxPagesPerQuery": 1,
    "resultsPerPage": 30,
    "mobileResults": False,
    "languageCode": "pl",
    "countryCode": "pl",
    "maxConcurrency": 10,
    "saveHtml": False,
    "saveHtmlToKeyValueStore": False,
    "includeUnfilteredResults": False,
    "customDataFunction": """async ({ input, $, request, response, html }) => {
        return {
            pageTitle: $('title').text(),
        };
    };""",
}

folder_path = "C:\\Users\\mslus\\Desktop\\Projekt-Przejsciowy\\Searches_2"

def run_actor(client, query, run_input, folder_path):
    run = client.actor("nFJndFXA5zjCTuudP").call(run_input=run_input)
    
    results = [item for item in client.dataset(run["defaultDatasetId"]).iterate_items()]

    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"{current_datetime}_{query}.json"

    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=2)

    print(f"Results saved to {file_path}")

# pentelka 
max_duration = 1000
sleep_interval = 3

max_runs = max_duration // sleep_interval

for i in range(max_runs):
    print(f"Attepmting run {i+1}/{max_runs}")
    run_actor(client, query, run_input, folder_path)
    print(f"Sleeping for {sleep_interval} seconds...")
    time.sleep(sleep_interval)