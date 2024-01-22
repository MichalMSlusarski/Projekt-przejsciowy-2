import pandas as pd

df = pd.read_csv('C:\\Users\\mslus\\Desktop\\Projekt-Przejsciowy\\output_2.csv')

# Group by 'url' and calculate both the average position and URL count
grouped_df = df.groupby('url')['position'].agg(['mean', 'count']).reset_index()

# Rename the columns
grouped_df = grouped_df.rename(columns={'mean': 'average_position', 'count': 'url_count'})

# Calculate the 'weight' column
const_num_of_searches = 100
grouped_df['weight'] = (grouped_df['url_count'] / const_num_of_searches).round(4)

# Calculate the 'weighted_position' column
grouped_df['weighted_position'] = (grouped_df['average_position'] / grouped_df['weight']).round(4)

# Sort the DataFrame by 'average_position'
grouped_df = grouped_df.sort_values(by=['weighted_position'])
grouped_df = grouped_df.reset_index(drop=True)

grouped_df.to_csv('grouped_df.csv', index=False)

# # Create a new DataFrame with the top 100 records from grouped_df
# top_30_urls = grouped_df.head(100)

# top_30_urls.to_csv('top_urls.csv', index=False)
# print(top_30_urls)