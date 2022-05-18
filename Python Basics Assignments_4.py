#!/usr/bin/env python
# coding: utf-8
1. What exactly is []?
Ans: Lists are created in Python using []. So it denotes a list.
  
2. In a list of values stored in a variable called spam, how would you assign the value 'hello'; as the
third value? (Assume [2, 4, 6, 8, 10] are in spam.)
Ans: 
# In[1]:


spam=[2, 4, 6, 8, 10]
spam[2]='hello'
spam

Let's pretend the spam includes the list ['a', 'b','c','d'] for the next three queries.
# In[2]:


spam=['a', 'b','c','d']

3. What is the value of spam[int(int('3'* 2) / 11)]?
# In[3]:


spam[int(int('3'* 2) / 11)]

4. What is the value of spam[-1]?
# In[4]:


spam[-1]

5. What is the value of spam[:2]?
# In[5]:


spam[:2]

Let's pretend bacon has the list [3.14,'cat'; 11,'cat', True] for the next three questions.
# In[7]:


bacon=[3.14,'cat', 11,'cat', True]

6. What is the value of bacon.index('cat')?
# In[8]:


bacon.index('cat')

7. How does bacon.append(99) change the look of the list value in bacon?
# In[9]:


bacon.append(99)
bacon

8. How does bacon.remove('cat') change the look of the list in bacon?
# In[10]:


bacon.remove('cat')
bacon

9. What are the list concatenation and list replication operators?
Ans: list concatenation can be done using '+'
list replication can be done using '*'
# In[11]:


lis1=[1,'a',2,'b']
lis2=[3,'c',4,'d']
lis=lis1+lis2 #concatenation
lis


# In[15]:


lis1=lis1*2 #replication
lis1

10. What is difference between the list methods append() and insert()?
Ans: 'Append' method adds an object at the end of the list whereas, 'insert' method adds an object at the specific position/index.
# In[17]:


lis1=[1,'a',2,'b']
lis1.append(100)
print(lis1)
lis1.insert(3,999)
print(lis1)

11. What are the two methods for removing items from a list?
Ans: 'pop' and 'remove'
'pop' removes object from left or right end of the list. 'remove' deletes a particular object from it's position. 
# In[23]:


lis1=[1,2,3,4,5,6,7]
print(lis1)
lis1.pop()
print(lis1)
lis1.remove(3)
print(lis1)

12. Describe how list values and string values are identical.
Ans: Both string and list are iterable objects and indexing,slicing can be done in both. Values in both string and list are sequenced. 

13. What's the difference between tuples and lists?
Ans: Tuples are immutable objects. We can not assign values in tuples. Lists are mutable.
  
14. How do you type a tuple value that only contains the integer 42?
# In[34]:


t=(42,)
t

15. How do you get a list value's tuple form? How do you get a tuple value's list form?
# In[37]:


lis=[1,2,3]
tup=(5,6,7)
lis1=[tup]
tup1=(lis,)
print(lis1)
print(tup1)

16. Variables that 'contain' list values are not necessarily lists themselves. Instead, what do they
contain?
Ans: Variables containing list values can be anything. Below is an example of a tuple containg a list value.
# In[41]:


t=([1,2,3],4,'a')
print(type(t))
print(type(t[0]))

17. How do you distinguish between copy.copy() and copy.deepcopy()?
Ans: copy.copy() is shallow copy and copy.deepcopy() is deep copy. In deep copy changes made in the copied objects do not reflect in the original objects.
# In[ ]:




