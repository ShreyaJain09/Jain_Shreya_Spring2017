
# coding: utf-8

# In[1]:

Assignment3Q2P1


# In[ ]:

import pandas as pd
import numpy as np
import csv


# In[6]:

employee=pd.read_csv('/Users/sjain/Python/Jain_Shreya_Spring2017/Assignment3/employee_compensation.csv')


# In[11]:

employeeOrgCal=employee.groupby(['Organization Group','Department']).agg({'Total Compensation': np.average})


# In[12]:

employee_sort= employeeOrgCal['Total Compensation'].groupby(level=0, group_keys=False)


# In[13]:

count = employee_sort.apply(lambda x: x.sort_values(ascending=False))


# In[14]:

total=count.to_frame()
total.to_csv('A3_Q2_P1.csv')
total.head()


# In[ ]:



