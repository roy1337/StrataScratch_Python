Find the top ten hotels with the highest ratings.

Output the hotel name along with the corresponding average score.
Sort records based on the average score in descending order.


#Solution 1
# Import your libraries
import pandas as pd

# Start writing code
hotel_reviews.groupby('hotel_name')['average_score'].nlargest(10).reset_index()

