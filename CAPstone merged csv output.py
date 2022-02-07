#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd


# In[18]:


data1 = pd.read_csv('https://raw.githubusercontent.com/Kanikadel/capstone/main/BOOKSMASTERTEST.csv')
data2 = pd.read_csv('https://raw.githubusercontent.com/Kanikadel/capstone/main/BOOKSMASTERTRAIN.csv')


# In[19]:


data1


# In[20]:


data2


# In[21]:


#data3 = pd.merge(data1, data2,on='BookID',how='left')
#print(data3)


# In[35]:


data3 = pd.concat(map(pd.read_csv, ['https://raw.githubusercontent.com/Kanikadel/capstone/main/BOOKSMASTERTEST.csv', 'https://raw.githubusercontent.com/Kanikadel/capstone/main/BOOKSMASTERTRAIN.csv']), ignore_index=True)
print(data3)


# In[36]:


data3


# In[37]:


d1=data3.columns[data3.dtypes!='object']
d2=data3.columns[data3.dtypes =='object']
print(d1)
print(d2)


# In[38]:


data3[d1].isnull().sum()


# In[39]:


data3[d1].isnull()


# In[40]:


data3.dropna()


# In[42]:


print(data3["USERRATINGS"])


# In[43]:


c1 = (data3["USERRATINGS"]>3.5)


result= data3[c1]
print(result)


# In[44]:


ques4= data3.sample()
q4=pd.DataFrame(ques4)
q4


# In[46]:


q4[["BOOKTITLE","AUTHORDESC"]]


# In[48]:


q4=data3[data3["USERRATINGS"]>4.5].iloc[0]
q4["AUTHORDESC"]


# In[49]:


unique_book=print(data3['BOOKTITLE'].unique())
print(unique_book)


# In[33]:


max_books=data3[data3["Popularity_x"].max()==data3["Popularity_x"]]

max_books.iloc[0]


# In[ ]:




