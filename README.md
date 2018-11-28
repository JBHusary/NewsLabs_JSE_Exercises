NewsLabs JSE Exercises

A set of programs to perform statistical analysis on viewing behavior of BBC articles.  

Contents

jhusary_c.py: script to determine the 1-hour period with the maximum mean of page views for each region

jhusary_c.text: table displaying the hour with the maximum mean of page views for the day for each region (region = dataframe index)

jhusary_e.py: script to calculate every 1-hour time interval where the mean number of Page Views  was greater than the overall mean for the day, for mobile phones

jhusary_e.text: table displaying the hours( hours = dataframe index) and hourlyMean when the  mean number of page views was greater than the overall daily mean for mobile phones

Data format

The data comes from two .csv files showing the number of page views collected at fifteen minute intervals of an article from 15 October 2018 at 13:00. "article-Regions.csv" is organised by region showing the total view count and the view count for each region, at each interval; and "article-Devices.csv" is organised by type of device on which the article was read showing the total view count and the view count for each type of device, at each interval.  

Getting started
  1. Ensure python3 is installed on machine
  2. Ensure anaconda is installed on machine, if not, install in command line with:
      | conda install anaconda
  this will have pandas, numpy libraries already installed to run functions in each file
  4. run file:
      | $python exercise_letter.py

