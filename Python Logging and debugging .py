#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import logging as lg


# In[2]:


pwd()


# In[3]:


os.mkdir('logging')


# In[4]:


os.chdir('logging')


# In[5]:


pwd()


# In[2]:


lg.basicConfig(filename='test.log',level=lg.INFO,format='%(asctime)s %(message)s')


# In[5]:


lg.info('this is log 1')


# In[6]:


lg.info('this is log 2')


# In[19]:


pwd()


# In[7]:


lg.warning('this is first warning')


# In[8]:


lg.info('this is log 1')


# In[9]:


lg.error('this is an error')


# In[5]:


filename.close()


# In[7]:


pwd()


# In[9]:


def test(a,b):
    try:
        lg.info('values are:'+str(a)+','+str(b))
        div=a/b
        return div
    except Exception as e:
        print('an error has occured. check your log')
        lg.error('an error has occured')
        lg.exception(str(e))


# In[10]:


test(4,0)


# In[11]:


pwd()


# In[2]:


os.chdir('logging')


# In[3]:


pwd()


# In[4]:


lg.basicConfig(filename='my_log.log',level=lg.INFO,format='%(asctime)s %(message)s')


# In[5]:


lg.info('this is info 1')


# In[9]:


def test(a,b):
    ans=a+b
    lg.info('input are '+str(a)+','+str(b))
    lg.info('answer is '+str(ans))
    return 'check log for answer'


# In[10]:


test(10,20)


# In[1]:


import ipdb


# In[2]:


def testdebug():
    ipdb.set_trace()
    l=[]
    for i in range(5):
        print('appending started')
        l.append(i)
    return l


# In[3]:


testdebug()


# In[4]:


c='hot'


# In[5]:


c


# In[ ]:




