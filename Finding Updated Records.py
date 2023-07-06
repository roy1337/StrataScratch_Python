Finding Updated Records
We have a table with employees and their salaries, however, some of the records are old and contain outdated salary information. Find the current salary of each employee assuming that salaries increase each year. Output their id, first name, last name, department ID, and current salary. Order your list by employee ID in ascending order.

#Solution 1
# Import your libraries
import pandas as pd

# Start writing code
df = ms_employee_salary.groupby('id').max().reset_index()

#Solution 2
# Import your libraries
import pandas as pd
import numpy as np
# Start writing code
ms_employee_salary.groupby(['first_name','last_name']).max('salary').reset_index()


#Solution 3
# Import your libraries
import pandas as pd
import numpy as np
# Start writing code
result = ms_employee_salary.groupby(['id','first_name','last_name','department_id'])['salary'].max().reset_index().sort_values('id')
