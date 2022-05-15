#!/usr/bin/env python
# coding: utf-8
1.What are the two values of the Boolean data type? How do you write them?

Ans:
2 values of Boolean data type are True and False. We get them using the bool() function as below.
# In[4]:


bool(1)


# In[5]:


bool(0)

3. What are the three different types of Boolean operators?
Ans: AND,OR,NOT3. Make a list of each Boolean operator&#39;s truth tables (i.e. every possible combination of Boolean
values for the operator and what it evaluate ).

Ans:
condition 1	condition 2	NOT X	X AND Y	X OR Y
(e.g., X)	(e.g., Y)	( ~ X )	( X && Y )	( X || Y )
FALSE	FALSE	TRUE	FALSE	FALSE
FALSE	TRUE	TRUE	FALSE	TRUE
TRUE	FALSE	FALSE	FALSE	TRUE
TRUE	TRUE	FALSE	TRUE	TRUE
4. What are the values of the following expressions?
Ans: 
(5 > 4) and (3 == 5): False
not (5 > 4): False
(5 > 4) or (3 == 5): True
not ((5 > 4) or (3 == 5)): False
(True and True) and (True == False): False
(not False) or (not True): True
    
5. What are the six comparison operators?
Ans:
>,<,==,>=,<=,!=

6. How do you tell the difference between the equal to and assignment operators?Describe a
condition and when you would use one.
Ans:

# In[6]:


#assignment:
a=5
a+5


# In[9]:


#equal to
if a==5:
    print('correct')
else:
    print('incorrect')

7. Identify the three blocks in this code:
spam = 0
if spam == 10:
    print('eggs')
if spam >5:
    print('bacon')
else:
    print('ham')
    print('spam')
    print('spam')

Ans:block1:
if spam == 10:
    print('eggs')
block 2:
if spam >5:
    print('bacon')
block3:
else:
print('ham')
print('spam')
print('spam')

8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.

    spam=int(input('enter value: '))
    if spam==1:
        print('Hello')
    elif spam==2:
        print('Howdy')
    else:
        print('Greetings!')

9.If your programme is stuck in an endless loop, what keys you’ll press?
ans: Ctrl+C
    
10. How can you tell the difference between break and continue?
Ans:
Break statement breaks out of the current loop
Continue statement skips the current iteration and moves on to the next one,

11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
Ans: No difference. All are same.
    
12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop. 
# In[2]:


for i in range(1,11):
    print(i)


# In[5]:


i=1
while i!=11:
    print(i)
    i+=1

13. If you had a function named bacon() inside a module named spam, how would you call it after
importing spam?
Ans:
import spam
spam.bacon()
# In[ ]:




