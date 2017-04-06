
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import re


# In[10]:

#Reading the file and giving it all a unique identifier
data = pd.read_csv("/Users/sjain/Python/Jain_Shreya_Spring2017/Assignment3/employee_compensation.csv", usecols=[0,1,9,11,12,13,14,15,16,17,18,19,20,21])


# In[11]:

#Printing few rows 
data.head()


# In[12]:

#Filtering it based on selecting Calendar as the year type
employee_calendar=data[data['Year Type'] == 'Calendar']


# In[13]:

employee_calendar.head()


# In[17]:

#Getting the unique employee, their salaries and the overtime amount 
unique_employee=employee_calendar.groupby(['Employee Identifier']).agg({'Salaries': np.sum,'Overtime': np.sum})


# In[18]:

unique_employee.head()


# In[25]:

#Selecting people with more than 5% overtime
employee_overtime=unique_employee[unique_employee['Overtime']/unique_employee['Salaries']>0.05]


# In[26]:

employee_overtime.head()


# In[28]:

#Creating a dataframe by comparing the index of with the index of the calendar year type
employee_clean=employee_calendar[employee_calendar.index.isin(employee_overtime.index)]


# In[29]:

employee_clean.head()


# In[30]:

#Using the dataframe to Groupby the Job Family and calculating on it.
employee_calendar1= employee_clean.groupby('Job Family').agg({'Total Benefits': np.average,'Total Compensation':np.average})


# In[31]:

employee_calendar1.head()


# In[32]:

#Calculating Percentage of Total Benefits to Total Compensation
employee_calendar1['Percentage']=employee_calendar1['Total Benefits']/employee_calendar1['Total Compensation']


# In[33]:

employee_calendar1.to_csv('A3_Q2_P2.csv')
employee_calendar1.head()


# In[ ]:



