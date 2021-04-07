#!/usr/bin/env python
# coding: utf-8

# In[ ]:


l1 = [2,7,5]
l2 = []
l3 = []
for i in range(len(l1)):
    for j in range(i,len(l1)):
        for k in range(i,(j+1)):
            l3.append(l1[k])
        l2.append(l3)
        l3 = []
print(l2)


# In[ ]:




