Find the number of apartments per nationality that are owned by people under 30 years old.
Output the nationality along with the number of apartments.
Sort records by the apartments count in descending order.


# Import your libraries
import pandas as pd

# Start writing code

merged = pd.merge(airbnb_hosts, airbnb_units, on='host_id')
merged.query('(age < 30) & (unit_type == "Apartment")').drop_duplicates().groupby('nationality').size().reset_index().sort_values(by=0,ascending=False)

merged_df = pd.merge(airbnb_apartments,airbnb_hosts, on = 'host_id')
