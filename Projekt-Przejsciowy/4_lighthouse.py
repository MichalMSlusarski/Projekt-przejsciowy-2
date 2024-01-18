import pandas as pd
import requests
from urllib.parse import urlparse
import time

api_key = ''
domains = []

with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()

df = pd.read_csv('C:\\Users\\mslus\\Desktop\\Projekt-Przejsciowy\\top_30_urls.csv')

fields_to_fetch = ['performance_score', 'pwa', 'best_practices_score', 'accessibility_score', 'seo_score']

for field in fields_to_fetch:
    df[field] = [None] * len(df)

def extract_domain(url: str):
    parsed_url = urlparse(url)
    result = parsed_url.scheme + "://" + parsed_url.netloc
    return str(result)

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

    df.loc[df['domain'] == url, 'performance_score'] = data['lighthouseResult']['categories']['performance']['score']
    df.loc[df['domain'] == url, 'pwa'] = data['lighthouseResult']['categories']['pwa']['score']
    df.loc[df['domain'] == url, 'best_practices_score'] = data['lighthouseResult']['categories']['best-practices']['score']
    df.loc[df['domain'] == url, 'accessibility_score'] = data['lighthouseResult']['categories']['accessibility']['score']
    df.loc[df['domain'] == url, 'seo_score'] = data['lighthouseResult']['categories']['seo']['score']


df['domain'] = [None] * len(df)
df['domain'] = df['url'].apply(extract_domain)

domains = df['domain'].tolist()


for dom in domains[2:]: # pomijam domenę znanylekarz.pl
    print(f"Getting metrics for {dom}")
    print(f"Progress: {domains.index(dom) + 1}/{len(domains)}")
    get_performance_metrics(dom, df=df)
    print("Sleeping for 1 second...")
    time.sleep(1)

    df.to_csv(f'C:\\Users\\mslus\\Desktop\\Projects\\top_30_urls_with_metrics_desktop.csv', index=False)    

