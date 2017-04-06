
# coding: utf-8

# In[1]:

import pandas as pd
import calendar
import csv,ast
import numpy as np


# In[31]:

#Read file from csv
vehicle= pd.read_csv("/Users/sjain/Python/Jain_Shreya_Spring2017/Assignment3/vehicle_collisions.csv")


# In[32]:

with open('A3_Q1_P2.csv','w') as csvfile:
    fieldnames = ['BOROUGH','ONE_VEHICLE_INVOLVED','TWO_VEHICLE_INVOLVED','THREE_VEHICLE_INVOVLED','MORE_VEHICLES_INVOLVED']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()


# In[33]:

import ast


# In[35]:

abc[:5]


# In[36]:

one_vehicle=((abc['VEHICLE 1 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 2 TYPE'] == ast.literal_eval('True')) & (abc['VEHICLE 3 TYPE'] == ast.literal_eval('True')) & (abc['VEHICLE 4 TYPE'] == ast.literal_eval('True')) & (abc['VEHICLE 5 TYPE'] == ast.literal_eval('True'))).sum()


# In[37]:

two_vehicle=((abc['VEHICLE 1 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 2 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 3 TYPE'] == ast.literal_eval('True')) & (abc['VEHICLE 4 TYPE'] == ast.literal_eval('True')) & (abc['VEHICLE 5 TYPE'] == ast.literal_eval('True'))).sum()


# In[38]:

three_vehicle=((abc['VEHICLE 1 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 2 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 3 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 4 TYPE'] == ast.literal_eval('True')) & (abc['VEHICLE 5 TYPE'] == ast.literal_eval('True'))).sum()


# In[39]:

more_vehicle=len(abc)-(one_vehicle+two_vehicle+three_vehicle)


# In[40]:

writer.writerow
({'BOROUGH':borough,
  'ONE_VEHICLE_INVOLVED':one_vehicle,
  'TWO_VEHICLE_INVOLVED':two_vehicle,
  'THREE_VEHICLE_INVOVLED':three_vehicle,
  'MORE_VEHICLES_INVOLVED':more_vehicle})


# In[42]:

with open('A3_Q1_P2.csv','w') as csvfile:
    fieldnames = ['BOROUGH','ONE_VEHICLE_INVOLVED','TWO_VEHICLE_INVOLVED','THREE_VEHICLE_INVOVLED','MORE_VEHICLES_INVOLVED']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for borough in(vehicle[~vehicle['BOROUGH'].isnull()]['BOROUGH'].unique()):
        queens=vehicle[vehicle['BOROUGH'] == borough]
        abc=pd.isnull(queens)
        one_vehicle=((abc['VEHICLE 1 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 2 TYPE'] == ast.literal_eval('True')) & (abc['VEHICLE 3 TYPE'] == ast.literal_eval('True')) & (abc['VEHICLE 4 TYPE'] == ast.literal_eval('True')) & (abc['VEHICLE 5 TYPE'] == ast.literal_eval('True'))).sum()
        two_vehicle=((abc['VEHICLE 1 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 2 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 3 TYPE'] == ast.literal_eval('True')) & (abc['VEHICLE 4 TYPE'] == ast.literal_eval('True')) & (abc['VEHICLE 5 TYPE'] == ast.literal_eval('True'))).sum()
        three_vehicle=((abc['VEHICLE 1 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 2 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 3 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 4 TYPE'] == ast.literal_eval('True')) & (abc['VEHICLE 5 TYPE'] == ast.literal_eval('True'))).sum()
        more_vehicle=len(abc)-one_vehicle-two_vehicle-three_vehicle
        writer.writerow({'BOROUGH':borough,'ONE_VEHICLE_INVOLVED':one_vehicle,'TWO_VEHICLE_INVOLVED':two_vehicle,'THREE_VEHICLE_INVOVLED':three_vehicle,'MORE_VEHICLES_INVOLVED':more_vehicle})
        

