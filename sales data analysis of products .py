#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


dataset=pd.read_csv('Sales_data.csv')


# In[3]:


dataset.head()


# In[4]:


dataset.head(10)


# In[5]:


dataset.info


# In[6]:


dataset.shape


# In[7]:


dataset.index


# In[9]:


dataset.nunique()


# In[13]:


dataset['Product'].value_counts()


# In[14]:


dataset.columns


# In[17]:


dataset['Order Date'].dtype


# In[18]:


dataset.isnull().sum()


# In[19]:


dataset.head()


# In[21]:


dataset.dropna()


# In[23]:


dataset.dropna(inplace=True)


# In[24]:


dataset.head()


# In[26]:


dataset[dataset['Order Date'].str[0:2]=='Or']


# In[27]:


dataset[dataset['Order Date'].str[0:2]!='Or']


# In[28]:


dataset=dataset[dataset['Order Date'].str[0:2]!='Or']


# In[29]:


dataset.head()


# In[30]:


dataset['Month']=dataset['Order Date'].str[0:2]
dataset['Month'].astype('int32')


# In[31]:


dataset.head()


# In[37]:


look_up={'01':'jan','02':'feb','03':'mar','04':'apr','05':'may','06':'jun','07':'jul','08':'aug','09':'sep','10':'oct','11':'nov','12':'dec'
}
dataset['Month']=dataset['Month'].apply(lambda x: look_up[x])


# In[38]:


dataset.head()


# In[40]:


dataset['Quantity Ordered']=dataset['Quantity Ordered'].astype('float')
dataset['Price Each']=dataset['Price Each'].astype('float')


# In[41]:


dataset.head()


# In[42]:


import warnings
warnings.filterwarnings('ignore')


# In[44]:


dataset['Sales']=dataset['Quantity Ordered']*dataset['Price Each']


# In[45]:


dataset.head()


# In[48]:


highest_sales=dataset.groupby('Month').sum()


# In[49]:


import matplotlib.pyplot as plt


# In[50]:


plt.figure()
plt.bar()


# In[ ]:




