#!/usr/bin/env python
# coding: utf-8
1. How do you distinguish between shutil.copy() and shutil.copytree()?
Ans: shutil.copytree() method is used to copy the contents of an entire directory from a source path to a destination path. If the destination directory is not present it creates one.

shutil.copy() method is used to copy a file from a source directory to a destination directory. 

2. What function is used to rename files??
Ans: os.rename()

3. What is the difference between the delete functions in the send2trash and shutil modules?
Ans: send2trash function sends files to recycle bin while shutil functions will permanetly delete the file.
    
4.ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is
equivalent to File objects’ open() method?
Ans: zipfile.ZipFile() is similar to open() function.
    
5. Create a programme that searches a folder tree for files with a certain file extension (such as .pdf
or .jpg). Copy these files from whatever location they are in to a new folder.

# In[23]:


import os
files=os.listdir()
files


# In[24]:


import shutil
current_path=os.getcwd()
destination='C:\\Users\\subho\\Desktop\\des'
count=0
for i in files:
    if '.txt' in i or '.pdf' in i or '.jpg' in i:
        shutil.copy(current_path+'\\'+i,destination)
        count+=1
print('number of files copied:',count)


# In[ ]:




