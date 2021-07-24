#!/usr/bin/env python
# coding: utf-8

# In[4]:


# assignment-5
# exception handling assignment


# In[6]:


# question-1
# write a python program to implement 5/0 and use try/except to catch exceptions


# In[7]:


try:
    a = int(input('enter the number: '))
    result = 5/a
    print(result)
except Exception as e:
    print(e)
    


# In[8]:


# problem-2
# implement a python program to generate all sentences where subject is in ['americans','indians'] and verb is in ['play','watch'] and the object is in ['baseball','cricket']


# In[12]:


subjects = ['Americans','Indians']
verbs = ['play','watch']
objects = ['Baseball','cricket']

for i in subjects:
    for j in verbs:
        for k in objects:
            print(i+' '+j+' '+k,end = '\n')


# In[ ]:




