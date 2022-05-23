#!/usr/bin/env python
# coding: utf-8
1. What are escape characters, and how do you use them?
Ans: To insert certain characters that are not allowed in a string we use escape characters. One example is "\" followed by  the characters we want to insert. Below is an example.
# In[1]:


s="we live in \"India\""
print(s)

2. What do the escape characters n and t stand for?
Ans:/n stands for new lines and \t stands for tabs.
  
3. What is the way to include backslash characters in a string?
Ans: s="we live in \"India\""
  
  
4. The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the
word Howl's not escaped a problem?
Ans: Since the string is enclosed in double quotes, single quoted character is not a problem. However, if the string would have been enclosed in single quotes, it would throw a syntax error as below,
# In[5]:


txt='Howl's Moving Castle'
print(txt)

5. How do you write a string of newlines if you don't want to use the n character?
Ans: we can use print() function as below.
# In[11]:


#with \n
print('hello \nworld')


# In[14]:


#without \n
print('hello')
print('world')

6. What are the values of the given expressions?
'Hello, world!'[1]
'Hello, world!'[0:5]
'Hello, world!'[:5]
'Hello, world!'[3:]
# In[16]:


#Ans:
hw='Hello, world!'
print(hw[1])
print(hw[0:5])
print(hw[:5])
print(hw[3:])

7. What are the values of the following expressions?
'Hello'.upper()
'Hello'.upper().isupper()
'Hello'.upper().lower()
# In[17]:


#Ans:
print('Hello'.upper())
print('Hello'.upper().isupper())
print('Hello'.upper().lower())

8. What are the values of the following expressions?
'Remember, remember, the fifth of July'.split()
'_'.join('There can only one'.split())
# In[18]:


#Ans:
print('Remember, remember, the fifth of July'.split())
print('_'.join('There can only one'.split()))

9. What are the methods for right-justifying, left-justifying, and centering a string?
Ans: ljust, rjust, center
  
10. What is the best way to remove whitespace characters from the start or end?
Ans: .strip()
# In[ ]:




