#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd


# In[32]:


df=pd.read_csv("deneme1.csv",sep=";")


# In[33]:


df


# In[34]:


students=[
    {"name":"Ahmet","surname":"Cevik","email":"ahmet@gmail.com"},
    {"name":"Mehmet","surname":"Varsiz","email":"mehmet@gmail.com"}
]


# In[35]:


df=pd.DataFrame(students)


# In[36]:


df


# In[37]:


students={
    "name":["Ahmet","Mehmet","Ali"],
    "surname":["Cevik","Varsiz","Yilmaz"],
    "email":["ahmet@gmail.com","mehmet@gmail.com","ali@gmail.com"]
}


# In[38]:


df=pd.DataFrame(students)


# In[39]:


df


# In[40]:


df['surname']


# In[41]:


type(df['surname'])


# In[42]:


df[['name','surname']]


# In[43]:


df.columns


# In[44]:


list(df.columns)


# In[45]:


df.columns.tolist()


# In[46]:


df['email']


# In[47]:


df.index


# In[48]:


df.iloc[1]


# In[49]:


df.iloc[2]['name']


# In[50]:


df.loc[1]


# In[55]:


df.index=df.index+5


# In[56]:


df


# In[52]:


df.iloc[1]


# In[53]:


df.loc[1]


# In[62]:


df.loc[10]


# In[61]:


df.shape


# In[60]:


df.loc[11]


# In[ ]:




