#!/usr/bin/env python
# coding: utf-8

# ## Import Data

# In[1]:


# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# In[2]:


# Reading Data
df = pd.read_csv('E:/Data Analysis Projects/Kickstarter projects/ks-projects-2018.csv')
df.head()


# ## Data Preprocessing

# In[3]:


# Display Information About Dataset
df.info()


# In[4]:


# Convert Object Datatype in columns ['deadline', 'launched'] to Date
df['deadline'] = pd.to_datetime(df['deadline'], errors = 'coerce', format= '%Y/%m/%d').dt.date
df['launched'] = pd.to_datetime(df['launched'], errors = 'coerce', format= '%Y/%m/%d').dt.date


# In[5]:


# Check Duplicates Values
df.duplicated().value_counts()


# In[6]:


# Check Missing Data For Each Column
df.isnull().sum()


# In[7]:


# Remove Null Values
df.dropna(subset='name',inplace=True)


# In[8]:


# Drop Unnecessary Columns From Dataset
df = df.drop(['usd pledged','goal','pledged'], axis=1)


# In[9]:


# Count Of Unique Values in country column
df['country'].value_counts()


# In[10]:


# Drop N,0" Values From Country Column
df = df.drop(df[df['country'] == 'N,0"'].index)


# In[11]:


# Count Of Unique Values in main_category column
df['main_category'].value_counts()


# In[12]:


# Create Column year from Date Datatype column
df['launched_year'] = pd.DatetimeIndex(df['launched']).year
df['deadline_year'] = pd.DatetimeIndex(df['deadline']).year


# In[13]:


df.head()


# In[14]:


# Count Of Unique Values in launched_year Column
df['launched_year'].value_counts()


# In[15]:


# Drop Date (1970) from Dataset Because they don't match with data
df = df.drop(df[df['launched_year'] == 1970].index)


# In[16]:


# Count Of Unique Values in [deadline_year] Column
df['deadline_year'].value_counts()


# In[17]:


# Display First 5 Rows
df.head()


# ## Exploratory Data Analysis

# In[18]:


# Display Statistical Summary About Numerical Data
df[['backers','usd_pledged_real','usd_goal_real']].describe()


# In[19]:


# Display Statistical Summary About Non-Numerical Data
df.describe(include='object')


# In[20]:


# Projects by Status
df['state'].value_counts().to_frame(name='Projects')


# In[21]:


# Projects per launched_year 
df['launched_year'].value_counts().to_frame(name='Projects')


# In[22]:


# Projects per deadline_year 
df['deadline_year'].value_counts().to_frame(name='Projects')


# In[23]:


# Projects per country 
df['country'].value_counts().to_frame(name='Projects')


# In[24]:


# Total Backers per Country
df[['country','backers']].groupby(['country']).sum().sort_values(['backers'],ascending=False)


# In[25]:


# Total Backers per deadline_year
df[['deadline_year','backers']].groupby(['deadline_year']).sum().sort_values(['backers'],ascending=False)


# In[26]:


# Total Pledged per country
df[['country','usd_pledged_real']].groupby(['country']).sum().sort_values(['usd_pledged_real'],ascending=False)


# In[27]:


# Total Pledged per deadline_year
df[['deadline_year','usd_pledged_real']].groupby(['deadline_year']).sum().sort_values(['usd_pledged_real'],ascending=False)


# In[28]:


# Projects Per main_category
df['main_category'].value_counts().to_frame(name='Projects')


# In[29]:


# Total Pledged Per main_category
df[['main_category','usd_pledged_real']].groupby(['main_category']).sum().sort_values(['usd_pledged_real'],ascending=False)


#  ##### Successful Projects Analysis

# In[30]:


# Create A New Dataframe Of Successful Projects From Dataset
df_success = df[df['state'] == 'successful']


# In[31]:


df_success.head()


# In[32]:


# Display A Statistical Summary Of Numerical Values Of Successful Projects
df_success[['backers','usd_pledged_real','usd_goal_real']].describe()


# In[33]:


# Display A Statistical Summary Of Non-Numerical Values Of Successful Projects
df_success.describe(include='object')


# In[34]:


# Total Successful Projects Per launched_year
df_success['launched_year'].value_counts().to_frame(name='Projects')


# In[35]:


# Total Successful Projects Per main_category
df_success['main_category'].value_counts().to_frame(name='Projects')


# In[36]:


# Total Successful Projects Per Country
df_success['country'].value_counts().to_frame(name='Projects')


# In[37]:


# Total backers Of Successful Projects Per deadline_year
df_success[['deadline_year','backers']].groupby(['deadline_year']).sum().sort_values(['backers'],ascending=False)


# In[38]:


# Total backers Of Successful Projects Per country
df_success[['country','backers']].groupby(['country']).sum().sort_values(['backers'],ascending=False)


# In[39]:


# Total Pledged of Successful Projects Per main_category
df_success[['main_category','usd_pledged_real']].groupby(['main_category']).sum().sort_values(['usd_pledged_real'],ascending=False)


# In[40]:


# Total Pledged Of Successful Projects Per deadline_year
df_success[['deadline_year','usd_pledged_real']].groupby(['deadline_year']).sum().sort_values(['usd_pledged_real'],ascending=False)


# In[41]:


df.to_csv('E:/Data Analysis Projects/Kickstarter projects/ks-projects-Transformation.csv')

