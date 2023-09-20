#!/usr/bin/env python
# coding: utf-8

# ## Indexing Numpy Arrays

# In[1]:


import numpy as np


# In[3]:


array = np.arange(0, 11)


# In[4]:


array


# In[5]:


array[4]


# In[6]:


array[-2]


# In[7]:


variable = np.array([[5, 10, 15],
                     [20, 25, 30],
                     [35, 40, 45]])


# In[8]:


variable


# In[9]:


variable[0, 0]


# In[10]:


variable[2, 1]


# In[13]:


variable[-1, -3]


# ## Slicing One-Dimensional Numpy Arrays

# In[14]:


import numpy as np


# In[19]:


example = np.arange(10, 20)


# In[20]:


example


# In[22]:


example[2:6]


# In[23]:


example[3::2]


# In[24]:


example[:7:3]


# ## Slicing Two-Dimensional Numpy Arrays

# In[25]:


import numpy as np


# In[26]:


array = np.arange(30).reshape(6, 5)


# In[27]:


array


# In[39]:


array[2, :]


# In[40]:


array[2]


# In[41]:


array[0]


# In[42]:


array[:, 2]


# In[43]:


array[:, 0]


# In[44]:


array


# In[45]:


array[1:4, 0:3]


# In[46]:


array[0::2, 0::2]


# ## Assigning Value to One-Dimensional Arrays

# In[4]:


import numpy as np 


# In[57]:


variable = np.array([0, 1, 2, 3, 7, 5, 6, 9, 8, 9])


# In[58]:


variable


# In[59]:


variable[4] = 4


# In[60]:


variable[7] = 7


# In[61]:


variable


# In[62]:


variable[0:5] = 10


# In[63]:


variable


# In[64]:


variable[5:]


# In[65]:


variable[5:] = 20, 30, 40, 50, 60


# In[66]:


variable


# ## Assigning Value to Two-Dimensional Arrays

# In[39]:


import numpy as np


# In[40]:


example = np.array([[10, 20, 30], 
                   [40, 50, 60],
                   [70, 80, 90]])


# In[41]:


example


# In[42]:


example[1, 1] = 100


# In[43]:


example


# In[44]:


example[1, 0] = 100.6


# In[45]:


example


# In[47]:


example[:, 2] = 100


# In[48]:


example


# In[49]:


example[0::2, 0:2]


# In[50]:


example[0::2, 0:2] = 100


# In[51]:


example


# In[52]:


example[0]


# In[53]:


example[0] = 10, 20, 30


# In[54]:


example


# ## Fancy Indexing of One-Dimensional Arrrays

# In[67]:


import numpy as np


# In[69]:


fancy = np.arange(0, 50, 5)


# In[70]:


fancy


# In[71]:


fancy[1]


# In[72]:


fancy[3]


# In[73]:


fancy[5]


# In[74]:


[fancy[1], fancy[3], fancy[5]]


# In[75]:


indexes = [1, 3, 5]


# In[76]:


fancy[indexes]


# In[82]:


array = np.array([1, 3, 5])


# In[83]:


array


# In[84]:


fancy[array]


# ## Fancy Indexing of Two-Dimensional Arrrays

# In[130]:


import numpy as np


# In[131]:


variable = np.zeros((10, 10), dtype = "int")


# In[132]:


variable


# In[133]:


variable.shape


# In[134]:


variable.shape[0]


# In[135]:


row = variable.shape[0]


# In[136]:


for i in range(row):
    variable[i] = i


# In[137]:


variable


# In[117]:


list1 = [1, 3, 5, 7]


# In[118]:


variable[list1]


# In[119]:


list2 = [8, 5, 2, 7, 3]


# In[120]:


variable[list2]


# In[126]:


example = np.arange(1,17).reshape((4,4))


# In[122]:


example 


# In[127]:


example[[0,3], [1,2]]


# In[138]:


row = [0, 2, 3, 1]
column = [3, 0, 2, 1]


# In[139]:


example[row, column]


# ## Combining Fancy Index with Normal Indexing

# In[140]:


import numpy as np


# In[141]:


example = np.arange(1,17).reshape((4,4))


# In[142]:


example


# In[144]:


example[1, [1,3]]


# In[145]:


example[[0, 3], 1]


# ## Combining Fancy Index with Normal Slicing

# In[146]:


import numpy as np


# In[147]:


example = np.arange(1,17).reshape((4,4))


# In[148]:


example


# In[149]:


example[0:, [1,2]]


# In[150]:


example[1:3, [1, 2]]


# ## Operations with Comparison Operators

# In[151]:


import numpy as np


# In[152]:


array = np.arange(1, 11)


# In[153]:


array


# In[154]:


array > 5


# In[155]:


array[array > 5]


# In[156]:


condition = array <= 4


# In[157]:


array[condition]


# In[169]:


new_condition = (array != 8) & (array >= 6)


# In[170]:


array[new_condition]


# ## Arithmetic Operations in Numpy

# In[1]:


import numpy as np


# In[172]:


array = np.arange(1, 11)


# In[173]:


array


# In[174]:


array - 2


# In[175]:


array * 10 


# In[176]:


array / 10


# In[178]:


((array * 10) + 20) / 5


# In[26]:


array * array


# In[27]:


array / array


# In[179]:


np.subtract(array, 2)


# In[180]:


np.multiply(array, 10)


# In[181]:


np.add(array, 20)


# In[183]:


np.divide(array, 10)


# In[184]:


array ** 3


# In[185]:


np.power(array, 3)


# In[2]:


np.sqrt(4)


# In[3]:


np.sqrt(100)


# In[186]:


array % 5


# In[187]:


np.mod(array, 5)


# In[199]:


np.sin(180)


# In[200]:


np.cos(180)


# In[201]:


np.log(array)


# In[202]:


np.log10(array)


# ## Statistical Operations in Numpy

# In[7]:


import numpy as np


# In[8]:


array = np.arange(1, 11)


# In[9]:


array


# In[10]:


np.sum(array)


# In[11]:


np.mean(array)


# In[18]:


np.median(array)


# In[12]:


np.min(array)


# In[13]:


np.max(array)


# In[14]:


np.std(array)


# In[15]:


np.var(array)


# In[16]:


np.sqrt(np.var(array))


# ## Solving Second-Degree Equations with NumPy

# In[1]:


import numpy as np


#  2X1 + X2  = 5

# -3X1 + 6X2 = 0

# In[2]:


coefficient = np.array([[2, 1], [-3, 6]])


# In[3]:


coefficient


# In[7]:


output = np.array([5, 0])


# In[8]:


output


# In[9]:


np.linalg.solve(coefficient, output)

