Find the top 5 businesses with most reviews. Assume that each row has a unique business_id such that the total reviews for each business is listed on each row. Output the business name along with the total number of reviews and order your results by the total reviews in descending order.

# Import your libraries
import pandas as pd

# Start writing code
df = yelp_business
top_5 = df[['name','review_count']].sort_values(by='review_count',ascending=False).head(5).reset_index()
top_5[['name','review_count']]


