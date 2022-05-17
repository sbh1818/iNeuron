#!/usr/bin/env python
# coding: utf-8
1. Why are functions advantageous to have in your programs?
Ans: Functions are customizable. Functions are used to carry out a specific task. They are reusable. It prevents writing codes repeatatively.
2. When does the code in a function run: when it's specified or when it's called?
Ans: The code runs when the function is called with proper paraments and arguments.
3. What statement creates a function?
Ans: 'def'
4. What is the difference between a function and a function call?
Ans: A function is a set of instructions written to carry out a specific task. Whereas, function call is a procedure to call the function to carry out the task.
# In[1]:


#example:
#creating a function:
def func():
    print('This is a function')


# In[2]:


#function call:
func()

5. How many global scopes are there in a Python program? How many local scopes?
Ans: there will be only one global scope. Local scope can be unlimited.
6. What happens to variables in a local scope when the function call returns?
Ans: Local scope variables are executed when the function call returns. However, they do not return values if the local scope variables are called outside the function.
7. What is the concept of a return value? Is it possible to have a return value in an expression?
Ans: 'return' statement returns the desired outcome of a function to the function caller. This keyword can only be used inside of a function, not outside. So, it is not possible to use 'return' keyword in an expression.
8. If a function does not have a return statement, what is the return value of a call to that function?
Ans: Nothing.
Also, if nothing is mentioned after the 'return' statement, the function returns 'None'.
9. How do you make a function variable refer to the global variable?
Ans: We need to declare the variable as 'global' using the 'global' keyword. Then only it will refer to the global variable.
10. What is the data type of None?
Ans: 'None' is a datatype that has a null value. It is not same as False or 0 or empty string. None is itself a datatype of it's own.
11. What does the sentence import areallyourpetsnamederic do?
Ana: It will import the module named 'areallyourpetsnamederic'.
12. If you had a bacon() feature in a spam module, what would you call it after importing spam?
Ans: spam.bacon()
13. What can you do to save a programme from crashing if it encounters an error
Ans: We can make use of exception handling. Using 'try', 'except' keywords we can handle the error/exception.
14. What is the purpose of the try clause? What is the purpose of the except clause?
Ans: 'try' caluse is used to run a suspicious piece of code which has the possibility of returning an error. 'except' clause is used to handle the error in case the suspicious code returns an error.
# In[ ]:




