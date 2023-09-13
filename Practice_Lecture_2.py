#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


np.array([2,4,6,7])


# In[3]:


Ar_list=[5.8,9,9]


# In[6]:


print(type(Ar_list[0]))
print(type(Ar_list[2]))


# In[ ]:





# In[8]:


AR2=np.array([2,4,6,7])
print(type(AR2[0]))


# In[ ]:





# In[10]:


Ar3=np.array([[2,5,7],[5,7,9]])


# In[80]:


print(Ar3)


# In[12]:


print(Ar3)


# In[13]:


Ar4=np.zeros(7)


# In[14]:


print(Ar4)


# In[15]:


Ar5=np.zeros((3,5), dtype = "int")
print(Ar5)


# In[16]:


np.ones(10)


# In[17]:


np.zeros((6,8), dtype = "int")


# In[18]:


np.ones((6,8), dtype = "int")


# In[19]:


np.ones((6,8,4), dtype = "int")


# In[20]:


np.full(8,5)


# In[22]:


np.full((4,6),5, dtype = "float")


# In[24]:


np.arange(7)


# In[25]:


np.arange(8,6, dtype = "float")


# In[31]:


Ar5=np.arange(1,10, dtype = "float")
print(Ar5)


# In[32]:


type(Ar5)


# In[33]:


np.eye(5)


# In[34]:


np.eye(4,7)


# In[35]:


np.eye(3,dtype="bool")


# In[36]:


np.eye(3,4,dtype="bool")


# In[37]:


np.random.rand(6)


# In[38]:


np.random.rand(3,4)


# In[39]:


np.random.randn(3,4)


# In[40]:


np.random.randint(3,4)


# In[41]:


np.random.randint(0,10,(3,4))


# In[42]:


np.random.randint(-10,10,(3,4))


# In[43]:


np.random.normal(20,5,(3,4))


# In[49]:


Ar6=np.random.randint(0,100,(3,4,3))


# In[50]:


Ar6.ndim


# In[51]:


Ar6.shape


# In[52]:


Ar6.size


# In[53]:


Ar6.dtype


# In[54]:


Ar7=np.arange(1,16)


# In[55]:


Ar7


# In[57]:


Ar7.reshape((3,5))


# In[58]:


Ar7.reshape((1,15))


# In[59]:


Ar8=np.random.randint(0,50,10)


# In[60]:


Ar8


# In[61]:


Ar8.max()


# In[62]:


Ar8.argmax()


# In[63]:


Ar8.min()


# In[64]:


Ar8.argmin()


# In[65]:


Ar9=np.random.randint(-10,20,10)
Ar9


# In[69]:


Ar10=np.concatenate([Ar8,Ar9])


# In[73]:


x,y,z=np.split(Ar10, [6,10])


# In[ ]:





# In[74]:


x


# In[75]:


y


# In[76]:


z


# In[77]:


Ar11=np.arange(20).reshape(5,4)


# In[78]:


Ar11


# In[79]:


np.split(Ar11, [1,3])


# In[85]:


np.split(Ar11, [1, 3], axis =1)


# In[83]:


np.hsplit(Ar11, 4)


# In[87]:


np.vsplit(Ar11, 5)


# In[ ]:




