import csv
import pandas as pd
import numpy

df = pd.read_csv('article-Regions.csv')
df['Date'] = pd.to_datetime(df['Date'])

#replaces integer indices with date/time
df.set_index(['Date'], inplace=True)                            

#a dataframe organizing the mean values/hour is created

#calculates mean for each hour using the values from rows H:15 - H+1:00
hourlyMeans = df.groupby(df.index.ceil('H')).mean()             

#print(hourlyMean)                                              

#shifts the groupby result to accruately correlate the hourly mean with the correct hour
shiftedMeans = pd.DataFrame(hourlyMeans.shift(-1, freq='H'))    

#print(shiftedMeans)      


#a dataframe is produced to hold data on the hour with the highest mean for each region
maxRegionalMeans = pd.DataFrame({'RegionalMaxMean': shiftedMeans.max(),
                                 'viewedHour': shiftedMeans.idxmax()})
maxRegionalMeans.index.name = 'Region'
#print(maxRegionalMeans)

maxRegionalMeans.to_csv('jhusary_c.csv')
