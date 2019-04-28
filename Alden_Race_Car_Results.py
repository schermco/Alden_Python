#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[3]:


pwd


# In[4]:


car_data = pd.read_csv("C:\\Users\\Garrick Schermer\\Documents\\Data\\ML\\Alden_race_car_Data.csv",sep = ',')
car_data.head()


# In[5]:


max_avg_speed = max(car_data['average_speed'])
print ('Highest Max Speed: ', max_avg_speed)


# In[ ]:




