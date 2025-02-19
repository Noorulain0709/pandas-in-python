#!/usr/bin/env python
# coding: utf-8

# In[3]:


#create series
import pandas as pd 
data=[221,334,56,78,9,9805,54,5]
series=pd.Series(data)
print(series)


# In[9]:


#creat data frame
import pandas as pd
data = {'name':['bia','anabia','shafa','sufia','pipon'],'age':[12,34,2,34,45]}
dataframe=pd.DataFrame(data)
print(dataframe)


# In[15]:


#cleaning of data
import pandas as pd
data= {
    'Name': ['Ali', 'Sara', 'Ahmed', 'Zara', 'Bilal'],
    'Age': [22, 25, 20, 23, 24],
    'Marks': [90, 85, 78, 92, 88]
}
df=pd.DataFrame(data)
print(df)
filtered_data=df[df['Marks']>80]
print(filtered_data)


# In[29]:


#cleaning with rows 
import pandas as pd
data= {
    'Name': ['Ali', 'Sara', 'Ahmed', 'Zara', 'Bilal'],
    'age': [22, 25, 20, 23, 24],
    'marks': [90, 85, 78, 92, 88]
}
df=pd.DataFrame(data)
print(df)
# Students who have Marks > 85 AND Age >22
filtered_data=df[(df['marks']>85) & (df['age']>22)]
print(filtered_data)


# In[31]:


#cleaning with rows and columns
import pandas as pd
data= {
    'Name': ['Ali', 'Sara', 'Ahmed', 'Zara', 'Bilal'],
    'age': [22, 25, 20, 23, 24],
    'marks': [90, 85, 78, 92, 88]
}
# Students who have Marks > 85 or Age >22
filtered_datai=df[(df['marks']>90) | (df['age']>23)]
print(filtered_datai)


# In[33]:


#concept of slicing
#slicing thorugh rows
import pandas as pd
data= {
    'Name': ['Ali', 'Sara', 'Ahmed', 'Zara', 'Bilal'],
    'age': [22, 25, 20, 23, 24],
    'marks': [90, 85, 78, 92, 88]
}
print(df.iloc[0:3])


# In[39]:


#slicing through columns
import pandas as pd
data= {
    'Name': ['Ali', 'Sara', 'Ahmed', 'Zara', 'Bilal'],
    'age': [22, 25, 20, 23, 24],
    'marks': [90, 85, 78, 92, 88]
}
print(df[['marks','age']])


# In[43]:


#selecting rows and columns
print(df.iloc[0:3, 0:2])  


# In[ ]:




