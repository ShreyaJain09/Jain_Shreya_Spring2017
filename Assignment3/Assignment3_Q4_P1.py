
# coding: utf-8

# # Assignment3_Q4_P1

# In[1]:

import csv
import pandas as pd
import re


# In[19]:

#Read the csv
movie= pd.read_csv('/Users/sjain/Python/Jain_Shreya_Spring2017/Assignment3/movies_awards.csv',encoding ='latin1')


# In[20]:


awards=pd.DataFrame(columns=["Awards","Awards_Won","Awards_Nominated","Prime_Awards_Nominated","Oscar_Awards_Nominated","Golden_Globe_Awards_Nominated","BAFTA_Awards_Nominated","Prime_Awards_won","Oscar_Awards_won","Golden_Globe_Awards_won","BAFTA_Awards_won"])
awards['Awards'] = movie['Awards'].dropna()


# In[21]:

awards.head()


# In[15]:

#From the awards column, extracting all the numbers
awards['Awards_Won'] = movie['Awards'].apply(lambda x: (re.findall(r"(\d+) win", str(x))))
awards['Awards_Nominated'] = movie['Awards'].apply(lambda x: (re.findall(r"(\d+) nomination", str(x))))
awards['Prime_Awards_Nominated'] = movie['Awards'].apply(lambda x: (re.findall(r"Nominated for (\d+) Primetime Emmy", str(x))))
awards['Prime_Awards_won'] = movie['Awards'].apply(lambda x: (re.findall(r"Won (\d+) Primetime Emmy", str(x))))
awards['Oscar_Awards_Nominated'] = movie['Awards'].apply(lambda x: (re.findall(r"Nominated for (\d+) Oscar", str(x))))
awards['Oscar_Awards_won'] = movie['Awards'].apply(lambda x: (re.findall(r"Won (\d+) Oscar", str(x))))
awards['Golden_Globe_Awards_Nominated'] = movie['Awards'].apply(lambda x: (re.findall(r"Nominated for (\d+) Golden Globe", str(x))))
awards['Golden_Globe_Awards_won'] = movie['Awards'].apply(lambda x: (re.findall(r"Won (\d+) Golden Globe", str(x))))
awards['BAFTA_Awards_Nominated'] = movie['Awards'].apply(lambda x: (re.findall(r"Nominated for (\d+) BAFTA", str(x))))
awards['BAFTA_Awards_won'] = movie['Awards'].apply(lambda x: (re.findall(r"Won for (\d+) BAFTA", str(x))))


# In[16]:

awards.head()


# In[17]:

#Filling empty list with 0's, removing the list and changing the type to int for all except the first column 
firstline = True
for a in awards.columns:
    if firstline:
        firstline = False
        continue
    awards[a] = (awards[a].apply(lambda x: 0 if len(x) == 0 else "".join(x))).astype(int)


# In[18]:

awards.head()


# In[6]:

# Summing of all the awards won and other nominations as mentioned above
awards['Awards_Won'] = awards['Awards_Won'] + awards['Prime_Awards_won'] + awards['Oscar_Awards_won'] + awards['Golden_Globe_Awards_won'] + awards['BAFTA_Awards_won']
awards['Awards_Nominated'] = awards['Awards_Nominated'] + awards['Prime_Awards_Nominated'] + awards['Oscar_Awards_Nominated'] + awards['Golden_Globe_Awards_Nominated'] + awards['BAFTA_Awards_Nominated']
awards.reset_index('Awards',inplace=True,drop=True)


# In[8]:

awards.to_csv('A3_Q4_P1.csv')


# In[10]:

awards.head()


# In[ ]:



