import pandas as pd
import requests
import time

api_key = ''
urls = []

with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()

df = pd.read_csv('C:\\Users\\mslus\\Desktop\\Projekt-Przejsciowy\\grouped_df.csv')

fields_to_fetch = ['performance_score', 'best_practices_score', 'accessibility_score', 'seo_score']

def get_performance_metrics(url: str, df: pd.DataFrame):

    params = {
        'url': url,
        'fields': 'lighthouseResult/categories/*/score',
        'prettyPrint': 'false',
        'strategy': 'desktop',
        'category': [
            'performance',
            'pwa',
            'best-practices',
            'accessibility',
            'seo'
        ],
        'key': api_key
    }

    response = requests.get('https://www.googleapis.com/pagespeedonline/v5/runPagespeed', params=params)

    if response.status_code != 200:
        print(f"Error getting metrics for {url}")
        return
    
    data = response.json()

    df.loc[df['url'] == url, 'performance_score'] = data['lighthouseResult']['categories']['performance']['score']
    df.loc[df['url'] == url, 'best_practices_score'] = data['lighthouseResult']['categories']['best-practices']['score']
    df.loc[df['url'] == url, 'accessibility_score'] = data['lighthouseResult']['categories']['accessibility']['score']
    df.loc[df['url'] == url, 'seo_score'] = data['lighthouseResult']['categories']['seo']['score']

urls = df['url'].tolist()

for url in urls:
    print(f"Getting metrics for {url}")
    print(f"Progress: {urls.index(url) + 1}/{len(urls)}")
    get_performance_metrics(url, df=df)
    print("Sleeping for 1 second...")
    time.sleep(1)

    df.to_csv(f'C:\\Users\\mslus\\Desktop\\Projekt-Przejsciowy\\lighthouse-output.csv', index=False)

