import pandas as pd

df = pd.read_csv('C:\\Users\\mslus\\Desktop\\Projekt-Przejsciowy\\Dane\\output.csv')

grouped_df = df.groupby('url')['position'].agg(['mean', 'count']).reset_index()
grouped_df = grouped_df.rename(columns={'mean': 'average_position', 'count': 'url_count'})

# Wyliczenie wagi pozycji w wyszukiwaniu
const_num_of_searches = 100
grouped_df['weight'] = (grouped_df['url_count'] / const_num_of_searches).round(4)
grouped_df['weighted_position'] = (grouped_df['average_position'] / grouped_df['weight']).round(4)

# Przesortowanie pozycji
grouped_df = grouped_df.sort_values(by=['weighted_position'])
grouped_df = grouped_df.reset_index(drop=True)

grouped_df.to_csv('grouped.csv', index=False)
