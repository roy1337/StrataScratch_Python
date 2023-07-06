You have been asked to find the job titles of the highest-paid employees.


Your output should include the highest-paid title or multiple titles with the same salary.

#Solution 1
# Import your libraries
import pandas as pd

# Start writing code
df = forbes_global_2010_2014
df = df[(df['profits'] == df['profits'].max()) & (df['sector'] == 'Financials')]
df[['company', 'continent']]


#Solution 2
# Import your libraries
import pandas as pd
import numpy as np
# Start writing code

workers_with_max_salary = worker[worker['salary'] == worker['salary'].max()]
df = pd.merge(workers_with_max_salary,title, left_on = 'worker_id', right_on = 'worker_ref_id')
df['worker_title']

#Solution 3
# Import your libraries
import pandas as pd
import numpy as np
# Start writing code

new_title_df = title.rename(columns={'worker_ref_id':'worker_id'})
df = pd.merge(worker, new_title_df, on='worker_id')
df = df.groupby('worker_title').max('salary').reset_index()
max_salary = df['salary'].max()

df.loc[df['salary']== max_salary, ['worker_title']]
