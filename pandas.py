#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd 
#series
data = [12,34,56,78,89]
series = pd.Series(data)
print(series)


# In[20]:


#data frame
data ={'name':['noor','muattar','mahnoor','pipon'],'class':[13,16,15,0]}
df=pd.DataFrame(data)
print(df)


# In[24]:


#q1.Write a Python program to create a pandas Series from the following list:
import pandas as pd
numbers = [5, 10, 15, 20, 25]
series=pd.Series(numbers)
print(series)


# In[1]:


#q2.Create a pandas Series with the following dictionary:
import pandas as pd
marks ={'name':['ali','sara','ahmed','zara'],'score':[90,85,78,92]}
df=pd.DataFrame(marks)
print(df)


# In[8]:


#qno2 but with different method
import pandas as pd
marks = {'Ali': 90, 'Sara': 85, 'Ahmed': 78, 'Zara': 92}
df=pd.Series(marks)
print(df)


# In[10]:


#Create a DataFrame from the following dictionary:
import pandas as pd
students = {
    'Name': ['Ayesha', 'Bilal', 'Hamza', 'Fatima'],
    'Age': [22, 24, 21, 23],
    'Grade': ['A', 'B', 'A', 'C']
}
df=pd.DataFrame(students)
print(df)


# In[16]:


#Use pd.Series() to convert the dictionary into a Series:
#marks_series = pd.Series(marks)
import pandas as pd
data = pd.Series([2, 4, 6, 8, 10])
mark_series=data.tolist()
print(mark_series)


# In[ ]:




