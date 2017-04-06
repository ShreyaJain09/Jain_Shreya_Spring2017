
# coding: utf-8

# # Assignment3_Q3_P1

# In[ ]:

import numpy as np
import pandas as pd
import math
import ast


# In[59]:

cricketData=pd.read_csv('/Users/sjain/Python/Jain_Shreya_Spring2017/Assignment3/cricket_matches.csv')
cricketHost=cricketData[cricketData['home'] == cricketData['winner']]


# In[60]:

cricScore=cricketHost[['home','winner','innings1','innings1_runs','innings2','innings2_runs']] # Taking the needed columns.


# In[61]:

cricScore.head()


# In[62]:

#Creating a new column called score with a 0 score
cricScore['Score']=0


# In[63]:

cricScore.head()


# In[64]:

pd.options.mode.chained_assignment = None 


# In[65]:

#Checking the inning of the team and adding it to the score
cricScore['Score'][(cricScore['home']==cricScore['innings1'])] = cricScore['innings1_runs'] 


# In[66]:

cricScore['Score'][(cricScore['home']==cricScore['innings2'])] = cricScore['innings2_runs']


# In[67]:

cricScore=cricScore[['home','Score']]


# In[68]:

#Taking the avg score of each team.
cricScore=pd.DataFrame(cricScore.groupby(['home']).mean()) 
cricScore.to_csv('A3_Q3_P1.csv')
cricScore.head()


# In[ ]:




# In[ ]:




# In[ ]:



