Number Of Bathrooms And Bedrooms
Find the average number of bathrooms and bedrooms for each city’s property types. Output the result along with the city name and the property type.


# Import your libraries
import pandas as pd

# Start writing code
df = airbnb_search_details
df = df.groupby(['city','property_type'])['bedrooms','bathrooms'].mean().reset_index()
df
