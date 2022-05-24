#!/usr/bin/env python
# coding: utf-8
1. Create an assert statement that throws an AssertionError if the variable spam is a negative
integer.
# In[4]:


#Ans:
spam=5
assert spam<0

2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain
strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are
considered the same, and 'goodbye' and 'GOODbye' are also considered the same).
# In[21]:


#Ans
spam=input('spam= ').lower()
bacon=input('bacon= ').lower()
assert spam!=bacon

3. Create an assert statement that throws an AssertionError every time.

# In[27]:


#Ans
assert 5>6

4. What are the two lines that must be present in your software in order to call logging.debug()?
#Ans:
import logging as lg
logger=lg.getLogger('logger')
logger.setLevel('debug')

5. What are the two lines that your program must have in order to have logging.debug() send a
logging message to a file named programLog.txt?
Ans:
file_handler=lg.FileHandler('programLog.txt')
logger.addHandler=(file_handler)

6. What are the five levels of logging?
Ans: DEBUG, INFO, WARNING, ERROR and CRITICAL
 
7. What line of code would you add to your software to disable all logging messages?
Ans:
lg.disable(level=50)

8.Why is using logging messages better than using print() to display the same message?
Ans:
Logging has several advantages over the print() function. It can log into any files. We can easily disable logs. There are several levels of logging based on severity. print() function does not offer such advantages.

9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?
Ans: Not Sure
  
10.After you click Continue, when will the debugger stop ?
Ans: No idea11. What is the concept of a breakpoint?
Ans: No idea
