Reviews of Hotel Arena

Find the number of rows for each review score earned by 'Hotel Arena'. Output the hotel name (which should be 'Hotel Arena'), review score along with the corresponding number of rows with that score for the specified hotel.



#Solution 1
# Import your libraries
import pandas as pd
# Start writing code
hotel_reviews.query('hotel_name == "Hotel Arena"').groupby(['reviewer_score','hotel_name']).size().reset_index()




#Solution 2
# Import your libraries
import pandas as pd
# Start writing code

df = hotel_reviews[hotel_reviews["hotel_name"] == 'Hotel Arena']
df1 = df.groupby(['reviewer_score','hotel_name']).size().reset_index()
