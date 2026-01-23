#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("deneme1.csv",sep=";")


# In[3]:


df


# In[4]:


students=[
    {"name":"Ahmet","surname":"Cevik","email":"ahmet@gmail.com"},
    {"name":"Mehmet","surname":"Varsiz","email":"mehmet@gmail.com"}
]


# In[5]:


df=pd.DataFrame(students)


# In[6]:


df


# In[7]:


students={
    "name":["Ahmet","Mehmet","Ali"],
    "surname":["Cevik","Varsiz","Yilmaz"],
    "email":["ahmet@gmail.com","mehmet@gmail.com","ali@gmail.com"]
}


# In[8]:


df=pd.DataFrame(students)


# In[9]:


df


# In[10]:


df['surname']


# In[11]:


type(df['surname'])


# In[12]:


df[['name','surname']]


# In[13]:


df.columns


# In[14]:


list(df.columns)


# In[15]:


df.columns.tolist()


# In[18]:


df['email']


# In[19]:


df.index


# In[20]:


df.iloc[1]


# In[21]:


df.iloc[2]['name']


# In[22]:


df.loc[1]


# In[25]:


df.index=df.index+5


# In[26]:


df


# In[27]:


df.iloc[1]


# In[28]:


df.loc[1]


# In[29]:


df.loc[10]


# In[30]:


df.shape


# In[ ]:




