#!/usr/bin/env python
# coding: utf-8

# In[197]:


import  pandas as pd
import numpy as np


# In[198]:


def read_df(fname, countries, years):
    """
    Function to read the csv file and return 2 dataframes,one with years 
    as columns and the other with countries as columns. Takes the filename as
    the parameter
    """
    df0 = pd.read_csv(fname, on_bad_lines='skip', skiprows=4, index_col=0)
    df0.drop(columns=["Country Code"], axis=1, inplace=True)
    df1 = df0.loc[countries,years]
    df1 = df1.sort_index().rename_axis("Years", axis=1)
 
    df2 = df1.T
    
    return df1, df2


# In[199]:


def Stats_df(df):
    """
    Function to do some basic statistics on the dataframes
    """


# In[200]:


def plot_df(df, kind, title):
    df0.iloc[:, 31:61]


# In[201]:


cntrs = ["Japan", "Pakistan", "China", "Korea, Rep.", "Australia", "United Kingdom", "Brazil",
                    "India",  "United States","Africa Eastern and Southern"]
yrs = ["1990", "1995", "2000", "2005", "2010", "2015"]
df_1, df_2 = read_df("API_EN.ATM.CO2E.KT_DS2_en_csv_v2_5347102.csv", cntrs, yrs)


# In[202]:


df_2


# In[203]:


df_3, df_4 = read_df("API_SP.URB.TOTL.IN.ZS_DS2_en_csv_v2_5348271.csv", cntrs, yrs)


# In[205]:


df_3.plot(kind='bar', figsize=(10, 5), rot=45)


# In[ ]:





# In[ ]:




