#!/usr/bin/env python
# coding: utf-8

# In[26]:


import  pandas as pd
import numpy as np
from scipy.stats import gmean, variation
from matplotlib import cm


# In[3]:


def read_df(fname, countries, years):
    """
    Function to read the csv file and return 2 dataframes,one with years 
    as columns and the other with countries as columns. Takes the filename as
    the parameter.
    """
    # read file into a dataframe
    df0 = pd.read_csv(fname, on_bad_lines='skip', skiprows=4, index_col=0)
    # some cleaning
    df0.drop(columns=["Country Code"], axis=1, inplace=True)
    df1 = df0.loc[countries,years]
    # dataframe methods for the points
    df1 = df1.sort_index().rename_axis("Years", axis=1)
    # transpose
    df2 = df1.T
    
    return df1, df2


# In[4]:


def stats_df(df):
    """
    Function to do some basic statistics on the dataframes.
    Takes the dataframe with countries as columns as the parameter.
    """
    # exploring the dataset
    print(df.describe())
    # some basic stats with scipy
    print("Weighted geometric mean is ", gmean(df, axis=0), "\n Coefficient of variation is ", variation(df, axis=0))
    
    return 
    


# In[5]:


def plot_df(df, kind, title):
    df0.iloc[:, 31:61]


# In[6]:


# supressing scientific notation to use the statistical tools
pd.set_option('display.float_format', lambda x: f'{x:,.2f}')


# In[7]:


cntrs = ["Japan", "Russian Federation", "China", "Korea, Rep.", "Saudi Arabia", "United Kingdom", "Brazil",
                    "India", "United States", "Germany", "Canada"]
yrs = ["1990", "1995", "2000", "2005", "2010", "2015"]
df_co2emission_1, df_co2emissions_2 = read_df("API_EN.ATM.CO2E.KT_DS2_en_csv_v2_5347102.csv", cntrs, yrs)
df_n20emissions_1, df_n20emissions_2 = read_df("API_EN.ATM.NOXE.KT.CE_DS2_en_csv_v2_4902772.csv", cntrs, yrs)


# In[8]:


stats_df(df_co2emissions_2)
stats_df(df_n20emissions_2)


# Coefficient of variation was calculated instead of standard deviation because we would be looking at different datasets of similar type(Carbon diooxide and Nitrous oxide emissions). This would help us in finding out which countries had the most relative increase in emissions in that 25 year time period.
# 

# In[14]:


df_co2emission_1


# In[76]:


color1 = cm.viridis(np.linspace(.1, .9, 6)[::-1])   # inferno, remove np
color2 = cm.inferno(np.linspace(.2, .9, 6)[::-1])
ax = df_co2emission_1.plot(kind='bar', figsize=(8, 4), rot=45, title='Carbon Dioxide emissions(kt)',
                            width=.8, color=color2)

ax = df_n20emissions_1.plot(kind='bar', figsize=(8, 4), rot=45, title='Carbon Dioxide emissions(kt)',
                            width=.8, color=color1)


# In[ ]:




