#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
url = "https://api.github.com/repos/pandas-dev/pandas/issues"


# In[2]:


data=requests.get(url)


# In[3]:


type(data)


# In[4]:


data1=data.json()


# In[5]:


type(data1)


# In[6]:


import pandas as pd


# In[7]:


dict_data = data1[0]['user']


# In[8]:


df = pd.DataFrame(data1)


# In[9]:


type(df)


# In[10]:


df1=pd.DataFrame(df.user.values.tolist())


# In[11]:


type(df1)


# In[12]:


df1.head(2)


# In[13]:


df.head(2)


# In[14]:


df_updated=[df,df1]


# In[15]:


df_comb=pd.concat(df_updated,axis=1)


# In[16]:


df_comb.head(2)


# In[17]:


df_comb.columns


# In[18]:


df_comb.shape


# In[19]:


df.shape


# In[20]:


df1.shape


# In[21]:


df_comb['user']


# In[ ]:




