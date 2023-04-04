# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 17:16:41 2023

@author: gobub
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import cm
from scipy.stats import gmean, variation, skew


def read_df(fname, countries, years):
    """
    Function to read the csv file and return 2 dataframes,one with years
    as columns and the other with countries as columns. Takes the filename as
    the argument.
    """
    # read file into a dataframe
    df0 = pd.read_csv(fname, on_bad_lines='skip', skiprows=4, index_col=0)
    # some cleaning
    df0.drop(columns=["Country Code"], axis=1, inplace=True)
    df1 = df0.loc[countries, years]
    # some dataframe methods
    df1 = df1.sort_index().rename_axis("Years", axis=1).fillna(0)
    # transpose
    df2 = df1.T

    return df1, df2


def stats_df(df):
    """
    Function to do some basic statistics on the dataframes.
    Takes the dataframe with countries as columns as the argument.
    """
    # exploring the dataset
    print("The summary statistics of the dataframe are: \n", df.describe())
    # some basic stats with scipy and dataframe methods
    print(
        "Weighted geometric means of each country are ", gmean(df, axis=0),
        "\n Coefficient of variation of each country are ",
        variation(df, axis=0),
        "\n Maximum values for each country in these years are ",
        df.max(axis=0),
        "\n Minimum values for each country in these years are ",
        df.min(axis=0),
        "\n Skewness is ", skew(df))

    return


def plot_df(df, knd, title, color):
    """
    Function to plot the dataframes using the dataframe.plot method.

    Arguments:
    The dataframe to be plotted.
    The kind of plot required.
    The title of the figure.
    The color scheme for the plot.

    """
    # using conditional statements for different kinds for better customization
    if knd == "line":
        ax = df.plot(kind=knd, figsize=(9, 5), rot=20, color=color)
        ax.legend(loc='best', fontsize=10)
        ax.set_title(title, fontweight='bold', fontsize='x-large',
                     fontname="Times New Roman")
        ax.set_xlabel("Years", fontweight='bold')
        ax.grid(axis='x', alpha=.85, linewidth=.75)
        plt.savefig(title+".png", dpi=350)
    else:
        ax = df.plot(kind=knd, figsize=(10, 5), rot=20, color=color)
        ax.legend(loc='best', fontsize=10)
        ax.set_title(title, fontweight='bold', fontsize='x-large',
                     fontname="Times New Roman")
        plt.savefig(title+".png", dpi=350)

    return


def makeheatmap(filename, country, indicators, c):
    """
    Function to plot the heatmap of a country's indicators. Parameters:
    The name of the csv file containing data of all indicators of
    all countries as a string(should end in .csv).
    The country of which we're plotting the heatmap of.
    The list of indicators we're consodering for the heat map.
    The color scheme.
    """
    # making the dataframe with which the
    # correlation matrix is to be calculated
    df0 = pd.read_csv(filename, skiprows=4)
    df0.drop(columns=["Country Code", "Indicator Code"], inplace=True)
    # setting multi-index to easily select the country
    df0.set_index(["Country Name", "Indicator Name"], inplace=True)
    df1 = df0.loc[country].fillna(0).T
    # slicing the dataframe to have only the years with nonzero data
    df = df1.loc["1970":"2015", indicators]
    # plotting the heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(), cmap=c, annot=True)
    plt.xticks(rotation=25)
    # setting a title and saving the figure
    plt.title(country,  fontweight='bold', fontsize='x-large',
              fontname="Times New Roman")
    plt.savefig(country+"'s Heatmap"+".png", dpi=350)

    return


# choosing the countries and years for the dataframes
cntrs = ["Japan", "Russian Federation", "China", "United Kingdom",
         "Brazil", "India", "United States", "Canada"]
yrs = ["1990", "1995", "2000", "2005", "2010", "2015"]

# creating the dataframes using the function
a, b = read_df("API_EN.ATM.CO2E.KT_DS2_en_csv_v2_5347102.csv", cntrs, yrs)
df_co2emissions_1, df_co2emissions_2 = a, b
c, d = read_df("API_EN.ATM.NOXE.KT.CE_DS2_en_csv_v2_4902772.csv", cntrs, yrs)
df_n20emissions_1, df_n20emissions_2 = c, d
e, f = read_df("API_AG.LND.ARBL.ZS_DS2_en_csv_v2_5346580.csv", cntrs, yrs)
df_arableland_1, df_arableland_2 = e, f
g, h = read_df("API_AG.LND.FRST.ZS_DS2_en_csv_v2_5348845.csv", cntrs, yrs)
df_agricultularland_1, df_agriculturalland_2 = g, h

# creating some cool colormaps for the bar plots
c1 = cm.viridis(np.linspace(.1, .9, 6)[::-1])
c2 = cm.inferno(np.linspace(.2, .9, 6)[::-1])
# some distinctive colors for the line plots
c3 = ['black', 'maroon', 'goldenrod', 'green',
      'teal', 'navy', 'hotpink', 'red']
c4 = ['b', 'g', 'r', 'k', 'm', 'y', 'c', 'brown']

# plotting dataframes with the function
plot_df(df_co2emissions_1, 'bar', 'Carbon Dioxide emissions(kt)', c2)
plot_df(df_n20emissions_1, 'bar',
        'Nitrous Oxide emissions(thousand metric tons of CO2 equivalent)', c1)
plot_df(df_agriculturalland_2, 'line', 'Agricultural land(% of land area)', c3)

# supressing scientific notation to use the statistical tools
pd.set_option('display.float_format', lambda x: f'{x:,.2f}')

# doing the basic sattistics with the function
stats_df(df_co2emissions_2)
stats_df(df_n20emissions_2)

"""
Coefficient of variation was calculated instead of standard deviation because
we would be looking at different datasets of similar type(Carbon diooxide and
Nitrous oxide emissions). This would help us in finding out which countries
had the most relative increase in emissions in that 25 year time period.
"""

# choosing the indicators to make heatmaps
indicators = [
    "Urban population", "Arable land (% of land area)",
    "Forest area (% of land area)",
    "Nitrous oxide emissions (thousand metric tons of CO2 equivalent)",
    "CO2 emissions (kt)",
    "Energy use (kg of oil equivalent per capita)"]

# creating some heatmaps to compare indicators of
# countries, explore it's correlations(or lack of)
makeheatmap("API_19_DS2_en_csv_v2_5346672.csv", "India", indicators, cm.winter)
makeheatmap("API_19_DS2_en_csv_v2_5346672.csv", "China", indicators, cm.jet)
makeheatmap("API_19_DS2_en_csv_v2_5346672.csv", "United Kingdom",
            indicators, cm.cool)
makeheatmap("API_19_DS2_en_csv_v2_5346672.csv", "Brazil", indicators, cm.bone)
