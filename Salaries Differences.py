Salaries Differences
Write a query that calculates the difference between the highest salaries found in the marketing and engineering departments. Output just the absolute difference in salaries.


import pandas as pd

df = db_employee 
df = df[df['department_id'] == 4]['salary'].max()-df[df['department_id']==1]['salary'].max()

df
