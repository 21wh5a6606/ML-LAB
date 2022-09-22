#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
irisData = load_iris()


# In[2]:


x = irisData.data
y = irisData.target
print(x)
print(y)


# In[3]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 42)


# In[14]:


knn = KNeighborsClassifier(n_neighbors = 7)


# In[15]:


knn.fit(x_train,y_train)


# In[17]:


knn.predict(x_test)


# In[18]:


knn.score(x_test,y_test)


# In[ ]:




