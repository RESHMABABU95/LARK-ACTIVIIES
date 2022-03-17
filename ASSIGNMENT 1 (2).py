#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT 1 - PYTHON FOR DATA SCIENCE

# In[ ]:


# 1-READ THE DATA SET TO PYTHON ENVIRONMENT


# In[ ]:


#pandas


# In[ ]:


import pandas as pd


# In[12]:


iris_data=pd.read_excel('iris.xls')
iris_data


# In[ ]:


#2 -DISPLAY COLUMNS IN THE DATA SHEET.


# In[13]:


iris_data.columns


# In[16]:


import pandas

file=pandas.read_excel('iris.xls')
for col in file.columns:
    print (col)


# In[ ]:


#3 -CALCULATE THE MEAN OF EACH COLUMN OF THE DATA SET.


# In[45]:


import pandas as pd

df1=df[['SL','SW','PL','PW']].mean()

print( 'Average of each column', df1)


# In[ ]:


#4-CHECK FOR THE NULL VALUES PRESENT IN THE DATASET


# In[46]:


import pandas as pd
import numpy as np

df=pd.DataFrame(iris_data)
df.isnull()


# In[ ]:


#5-PERFORM MEANINGFUL VISUALISATIONS USING THE DATA SET.BRING ATLEAST 3 VISUALISATIONS


# In[ ]:


*1-HISTOGRAM using values in columns SL and SW.


# In[47]:


iris_data=pd.read_excel('iris.xls')
iris_data


# In[48]:


iris_data.columns


# In[62]:



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 
plt.figure(figsize=(5,5))
plt.hist(iris_data["SL"],color= "red", rwidth=0.6,density=True)
plt.title("Histogram of SL",fontsize=12)
plt.xlabel('SL')
plt.ylabel('Frequency')
plt.xticks()
plt.yticks()


# In[ ]:


*2- HISTOGRAM of SW and PW together in a graph


# In[64]:


iris_data[['SW','PW']].plot.hist()


# In[ ]:


*3-SCATTERPLOT of SL vs PL


# In[69]:



plt.figure(figsize=(5,5))
plt.scatter(iris_data['SL'],iris_data['PL'], s=16,c='violet',marker='^')
plt.title('Plot of SL vs PL', fontsize=14)
plt.xlabel('SL')
plt.ylabel('PL')


# In[ ]:




