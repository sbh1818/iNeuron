#!/usr/bin/env python
# coding: utf-8
1. What does an empty dictionary code look like?
# In[1]:


#Ans
Dict={}
Dict

2. What is the value of a dictionary value with the key 'foo' and the value 42?
# In[6]:


#Ans:
dict={}
dict['foo']=42
dict

3. What is the most significant distinction between a dictionary and a list?
Ans: Dictionary contains data in 'key:value' format whereas, lists contain only values.4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
Ans: It'll throw KeyError
# In[14]:


spam={}
spam['bar']=100
spam['foo']

5. If a dictionary is stored in spam, what is the difference between the expressions 'cat'; in spam and
'cat' in spam.keys()?
Ans: 'cat stored in the dictionary spam is a variable and can be of any type. Whereas 'cat' in spam.keys() is a dict_keys object.6. If a dictionary is stored in spam, what is the difference between the expressions 'cat'; in spam and
'cat' in spam.values()?
Ans: 'cat stored in the dictionary spam is a variable and can be of any type. Whereas 'cat' in spam.values() is a dict_values object.7. What is a shortcut for the following code?
if 'color' not in spam:
    spam['color'] = 'black'
Ans: spam.setdefault('color', 'black')8. How do you 'pretty print' dictionary values using which module and function?
Ans:pprint.pprint()
# In[24]:


import pprint
pprint.pprint(spam)


# In[ ]:




