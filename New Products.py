You are given a table of product launches by company by year. Write a query to count the net difference between the number of products companies launched in 2020 with the number of products companies launched in the previous year. 
Output the name of the companies and a net difference of net products released for 2020 compared to the previous year.



#Solution 1                      
# Import your libraries
import pandas as pd

# Start writing code
df = car_launches
total = df.groupby(['company_name','year']).size().reset_index(name='number_of_products')
nop19 = total[total['year'] == 2019]
nop20 = total[total['year'] == 2020]

new_df = nop19.merge(nop20, how='inner', on='company_name')

new_df['diff'] = new_df['number_of_products_y']-new_df['number_of_products_x']
new_df[['company_name','diff']]

#Solution 2
# Import your libraries
import pandas as pd

# Start writing code
df = car_launches.groupby(['company_name','year']).size().reset_index(name='product_name')
df = pd.merge(df, df, how = 'inner', on='company_name')
df = df.query('year_x == 2020 & year_y == 2019')[['company_name', 'product_name_x', 'product_name_y']]

df['diff'] = df['product_name_x'] - df['product_name_y']
df[['company_name','diff']]
