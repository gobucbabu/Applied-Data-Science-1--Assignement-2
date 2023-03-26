#!/usr/bin/env python
# coding: utf-8

# In[64]:


import  pandas as pd


# In[171]:


def read_df(fname):
    df0 = pd.read_csv(fname, on_bad_lines='skip', skiprows=4, index_col=0)
    df0.drop(columns=["Indicator Code", "Country Code"], axis=1, inplace=True)
    df1a = df0.iloc[:, 31:61]
    df1b = df1a[["1990", "1995", "2000", "2005", "2010", "2015"]]
    df1 = df1b.loc[["Korea, Rep.", "Japan", "Pakistan", "United Kingdom", "Australia", "Brazil",
                    "India","Africa Eastern and Southern",  "United States", "China"]]
    df2 = df1.T
    
    return df1, df2


# In[172]:


df_1, df_2 = read_df("API_EN.ATM.CO2E.KT_DS2_en_csv_v2_5347102.csv")


# In[178]:


df_3, df_4 = read_df("API_SP.URB.TOTL.IN.ZS_DS2_en_csv_v2_5348271.csv")


# In[182]:


df_3.plot(kind='bar', figsize=(12, 5), rot=35)


# In[ ]:





# In[ ]:




