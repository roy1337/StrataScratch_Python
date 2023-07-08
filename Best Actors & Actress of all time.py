Find the best actors/actresses of all time based on the number of Oscar awards. Output nominees alongside their number of Oscars. Order records in descending order based on the number of awards.

# Import your libraries
import pandas as pd

# Start writing code

result = oscar_nominees.groupby('nominee').size().reset_index().rename(columns={0: 'count'})
max_count = result['count'].max()
result_max = result[result['count']== max_count]
