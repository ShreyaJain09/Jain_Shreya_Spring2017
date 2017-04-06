
# coding: utf-8

# # Assignment3_Q1_P1

# In[ ]:

import pandas as pd
import calendar
import csv


# In[5]:

#Read file from csv
vehicle= pd.read_csv("/Users/sjain/Python/Jain_Shreya_Spring2017/Assignment3/Data/vehicle_collisions.csv")


# In[8]:

with open('A3_Q1_P1.csv','w') as csvfile:
    fieldnames = ['MONTH','MANHATTAN','NYC','PERCENTAGE']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for a in range(1,13):
        year=vehicle[(vehicle['BOROUGH'] =="MANHATTAN") & (vehicle['DATE'].apply(lambda x:x.split("/")[2]) == "16") ]
        nyc=((vehicle['DATE'].apply(lambda x:x.split("/")[2]) == "16") & (vehicle['DATE'].apply(lambda x:x.split("/")[0]) == str(a))).sum()
        manhattan_acc=(year['DATE'].apply(lambda x:x.split("/")[0]) == str(a)).sum()
        percentage=manhattan_acc/nyc
        #print(percentage.round(8),nyc,manhattan_acc,calendar.month_name[int(a)][:3])
        writer.writerow({'MONTH':calendar.month_name[int(a)][:3],'MANHATTAN':manhattan_acc,'NYC':nyc,'PERCENTAGE':percentage.round(8)})


# In[ ]:




# In[ ]:



