#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[3]:


import numpy as np
import pandas as pd
import mataplotlib.pyplot as plt
array=np.array(10)
print(array)


# In[7]:


type(array)
print(array.ndim)


# In[9]:


age=np.array([2,4,5,6])
print (age.ndim)


# In[6]:


print(age[2])


# In[20]:


threendim=np.array([[3,4,6],[4,7,9],[1,2,8],[7,9,10]])
print(threendim.ndim)
print(threendim[2])


# In[21]:


'''indexing in numpy arrays'''
onedimension=np.array([5,6,6,7])
twodimension=np.array([[9,4,3,2],[5,8,4,3]])
print(twodimension.ndim)
print(twodimension[0,2])


# In[26]:


#array slicing
'''
comma is for indexing but collon is for slicing
'''
print(twodimension[1,2:])
print(twodimension[0:2])


# In[51]:


#array iterating
for i in twodimension:
    for j in i:
        if j > 4:
            m = j * 2
            print(m)
        else:
            print(j)


# In[55]:


#feature scaling
import matplotlib.pyplot as plt
data=np.array([[5,4,6,3],[53,7,5,4],[4,7,8,4],[5,8,4,3]])
figure=plt.figure(figsize=(20,12))
plt.boxplot(data)
plt.show()


# In[59]:


from sklearn.preprocessing import MinMaxScaler

# Create an instance of the MinMaxScaler
scaler = MinMaxScaler()

# Fit the scaler to your data (compute the min and max values)
scaler.fit(data)

# Transform your data using the fitted scaler
scaledData = scaler.transform(data)
print(scaledData)


# In[63]:


figure=plt.figure(figsize=(10,20))
plt.boxplot(scaledData)
plt.show()


# In[69]:


from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler.fit(data)
scaledData1=scaler.transform(data)

print(scaledData1)


# In[71]:


figure=plt.figure(figsize=(20,10))
plt.boxplot(scaledData1)
plt.show()


# In[75]:


import pandas as pd
my_data={"Gender":["male","unknown","male"],"Name":["kelvin","ronn","james"]}
data=pd.DataFrame(my_data)
print(data)


# In[81]:


#label Encoding
from sklearn.preprocessing import LabelEncoder

lb = LabelEncoder()

data["Gender"]=lb.fit_transform(data["Gender"])
print(data)


# In[ ]:


#onehot Encoding

