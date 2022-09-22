#!/usr/bin/env python
# coding: utf-8

# In[9]:


import sqlite3


# In[10]:


conn = sqlite3.connect('gunni.db')


# In[11]:


cur = conn.cursor()


# In[13]:


cur.execute("create table std1(id int,name char)")


# In[16]:


cur.execute("insert into std1 values(1,'adams'),(2,'gunni'),(3,'nikki')")


# In[17]:


for row in cur.execute('select * from std1'):
    print(row)


# In[18]:


for row in cur.execute('SELECT * FROM std1 ORDER BY name'):
    print(row)


# In[ ]:




