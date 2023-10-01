#!/usr/bin/env python
# coding: utf-8

# # Import Libraries

# In[2]:


import pandas as pd


# In[3]:


import numpy as np


# In[4]:


import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')


# # Load the Dataset

# In[54]:


df = pd.read_csv("C:/Users/PCC/Downloads/IMDB_MoviesUP.csv")


# In[55]:


df


# In[56]:


#Lets first understand the basic information about this data


df.info()


# In[57]:


# Preview top 5 rows using head()

df.head()


# In[58]:


# preview bottom 5 rows using tail()

df.tail()


# In[59]:


# The column names in the data can be viewed by using 'columns'

df.columns


# In[60]:


# The shape of the dataset can be viewed by using 'shape'

df.shape

This function tells us that there are 3849 rows and 9 columns in the dataset

Let's use describe( ) method to understand the numerical attributes in the data

describe( ) shows the basic statistical summaries of numerical attributes in the data.
# In[61]:


df.describe()

Some Insights from description of data
The min and max values in 'gross' depict the minimum and maximum release gross. We can see that the dataset contains 
movies.

The average imdb_score 6.46 for the movies in this dataset is about and the mininum imdb_score is 1.6 and the maximum imdb_score is 9.3

The maximum budget by a movie is 1.221550e+10
# In[62]:


# check null values
df.isnull().sum()


# # Data Selection - Indexing and Slicing
# 
Extracting data from Pandas column is similar to Series. The column label is used to extract data from the column


# # Extracting data by columns
# 

# In[63]:


# Extract data as series
genre = df['genres']


# In[64]:


genre


# In[65]:


type(genre)


# In[66]:


# Extract data as dataframe
df[['genres']]


# In[67]:


type(df[['genres']])


# In[68]:


df.columns


# In[69]:


some_cols = df[['director_name','duration','genres','movie_title','imdb_score']]


# In[70]:


some_cols.head()


# # Extract data by row index
# 

# In[71]:


df.head()


# In[72]:


# Retrieving movie with director_name
df.iloc[3:4]


# In[73]:


# Pick rows from indexes 10-17
df.iloc[10:17]


# In[74]:


df.iloc[10:17][['director_name','genres','movie_title','budget','imdb_score']]


# # Data Selection - based on Conditional Filtering
# 

# In[75]:


imdb_score = np.where(df['imdb_score'] == max(df['imdb_score']))
df.iloc[imdb_score][['director_name','genres','movie_title','budget','imdb_score']]


# In[78]:


# Get unique values in director_name column
df['director_name'].unique()


# In[80]:


df['director_name'].value_counts()


# # Groupby operations

# In[81]:


df.groupby('director_name').sum()


# In[82]:


df.groupby('director_name')[['imdb_score']].mean().head()


# # Sorting

# In[83]:


df.groupby('director_name')[['imdb_score']].mean().sort_values(['imdb_score'], ascending=False).head()


# In[84]:


df.sort_values(['movie_title','imdb_score'], ascending=False).head(5)


# # Dealing with missing values
# 

# In[85]:


# To see if there are null values in the whole data
df.isnull()


# In[86]:


# To check null values row-wise
df.isnull().sum()


# # Dropping null values
# 

# In[87]:


# Drops all rows containing missing data
df.dropna()


# In[88]:


# Drop all columns containing missing data
df.dropna(axis=1)


# In[89]:


df.dropna(axis=0, thresh=6)


# In[90]:


# Use drop function to drop columns
df.drop('language', axis=1).head()


# In[92]:


budget_mean = df['budget'].mean()
print("The mean budget is: ", budget)


# In[93]:


# We can fill the null values with this mean revenue
df['budget'].fillna(budget_mean, inplace=True)

inplace = True signifies that the changes be made permanently in the dataset.


# In[94]:


df.isnull().sum()


# # Apply( ) Functions

# In[95]:


# Classify movies based on ratings
def imdb_score_group(imdb_score):
    if imdb_score >= 7:
        return 'Good'
    elif imdb_score >= 6:
        return 'Average'
    else:
        return 'Bad'


# In[96]:


# Lets apply this function on our movies data
# creating a new variable in the dataset to hold the rating category
df['imdb_score_category'] = df['imdb_score'].apply(imdb_score_group)


# In[97]:


df[['director_name','genres','imdb_score','imdb_score_category']].head(5)


# # Pivot table
# 

# In[98]:


df.pivot_table('movie_title', index='director_name', aggfunc='sum', columns='duration').head(10)


# In[ ]:




