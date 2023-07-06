Find the number of employees working in the Admin department that joined in April or later.

# Import your libraries
import pandas as pd

# Start writing code

df = worker[(worker['joining_date'] > '2014-04-01') & (worker['department'] == 'Admin')]
len(df)
