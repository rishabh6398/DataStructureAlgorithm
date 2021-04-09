#!/usr/bin/env python
# coding: utf-8

# In[5]:


import array as ar
arr=ar.array('i',[1, 4, 6, 8, 7])
temp=0
y=-1
for i,j in enumerate(arr): 
    temp=arr[i] 
    arr[i]=arr[y] 
    arr[y]=temp
print(arr)


# In[ ]:




