import csv
import pandas as pd
import numpy

df = pd.read_csv('article-devices.csv')
#sets date to DateTime datatype
df['Date'] = pd.to_datetime(df['Date'])  

#sets index to Date
df.set_index(['Date'], inplace=True)                                

mobileMeans = df['Mobile'].groupby(df.index.ceil('H')).mean()

#shifts the groupby result to accruately correlate the hourly mean with the correct hour
shiftedMeans = mobileMeans.shift(-1, freq='H')

#calculates the overall mean page views
overallMean = df['Total'].mean()

#checks if hourly mean is greater than overall mean
mobileHourlyMeans = mobileMeans[mobileMeans > overallMean]

#creates a new dataframe to hold the results
mobileHourlyMeans = pd.DataFrame({'Hour' : mobileHourlyMeans.index,
                                  'greaterMean' : mobileHourlyMeans.values})

#print (mobileHourlyMeans)

mobileHourlyMeans.to_csv('jhusary_e.csv')
