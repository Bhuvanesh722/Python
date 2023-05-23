#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


num1=[12,23,45,55]
num2 = np.array(num1)
print(num2)


# In[4]:


np.random.rand(2,3)


# In[5]:


np.random.random(size=20)


# In[6]:


np.random.randn(4,6)


# In[7]:


np.random.randint(2,8)


# In[8]:


np.random.randint(1,101,100)


# In[9]:


np.arange(1,22,2)


# In[10]:


np.arange(0,50,5)


# In[11]:


np.arange(100,0,-1)


# In[12]:


np.linspace(0,1,10)


# In[13]:


np.zeros(10,int)


# In[14]:


np.ones(100,int)


# In[15]:


matrix = np.empty((5,5),int)
print(matrix)


# In[16]:


matrix = np.full((3,3),45)
print(matrix)


# In[17]:


np.identity(6)


# In[18]:


np.eye(4,5,2)


# In[21]:


a = np.arange(1,21)
print(a)


# In[22]:


a.reshape(4,5)


# In[32]:


sample_arr=np.arange(0,10)
print(sample_arr)


# In[33]:


print(sample_arr[4])


# In[35]:


weight = np.array([55,32,44,22,99])
print(weight[2:4])


# In[ ]:




