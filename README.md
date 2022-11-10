# SQLAlchemy-Challenge

As a part of this research project,  I was required to analyse the climate dataset (hawaii.sqlite) for Honolulu, Hawaii! a favourable destination for most travellers; owing to its spelendid natural beauty. 

Is travelling to Honolulu enjoyable throughout the year? Hmmmmm.....lets find out!

##Part 1: Climate Analysis and Exploration
Employing SQLAlchemy ORM queries, Pandas, and Matplotlib, I carried out climate analysis and data exploration of the climate database. IN order to complete this task i connected to SQLite database (by a creating engine), followed by automap_base() to reflect weather tables into classes and finally connecting to python using a SQLAlchemy session.


### Precipitation Analysis
Precipitation data was analysed for the last 1 year of the climate dataset to get an idea of the most (recent) annual precipation pattern (in inches).

![alt text](https://github.com/fbrowther/SQLAlchemy-Challenge/blob/main/Images/Annual_Precipitation_Hawaii.png)

Eventhough, there were very few distinct days of outpour; for most part of the year, the sky was clear and showed very little to no precipitation for most part of the year. This was also supported by the summary statistical analysis which showed a mean	of 0.048843, std 0.205197, min of 0.000000, and max of 2.620000.


### Station Analysis
In order to determine the most favourable station for holiday within Hawaii I obtained the list of stations with most activity recorded first, followed by retrieving its ('USC00519281') previous 12 months of temperature observation data (TOBS). The distribution of TOBS for this station has been illustrated as follows -

![alt text](https://github.com/fbrowther/SQLAlchemy-Challenge/blob/main/Images/Temperature%20in%20highly_active_station.png)





### Temperature Analysis - Is there a meaningful difference in temperatures in June and December?
For this i analysed the weather dataset to identify the average temperature in June for all stations across all available years in the dataset. This was repeated for the month of december too. 

June average temperature:  74.94411764705882
Decempber average temperature:  71.04152933421226

Further analyses also showed no statistically significant difference in temperature (employing unpaired Ttest) for the month of June and for December.
Ttest=31.60372399000329, 
pvalue=3.9025129038616655e-191


Do the same for the temperature in December.


Use the t-test to determine whether the difference in means, if any, is statistically significant. Will you use a paired t-test or an unpaired t-test? Why?



Temperature Analysis 2
You want to take a trip from August 1 to August 7 of this year, but you are worried that the weather will be less than ideal. Using historical data in the dataset, find out what the temperature has previously been for this timeframe.
Note: The starter notebook contains a function called calc_temps that will accept a start date and end date in the format %Y-%m-%d. The function will return the minimum, average, and maximum temperatures for that range of dates.
Complete the following steps:


Use the calc_temps function to calculate the minimum, average, and maximum temperatures for your trip using the matching dates from a previous year (for example, use "2017-08-01").


Plot the minimum, average, and maximum temperature from your previous query as a bar chart, as captured in the following steps and image:


Use "Trip Avg Temp" as the title.


Use the average temperature as the bar height (y value).


Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).

Daily Rainfall Average
Now that you have an idea of the temperature, let’s find out what the rainfall has been. You don't want to visit if it rains the whole time! Complete the following steps:


Calculate the rainfall per weather station using the previous year's matching dates.

Sort this in descending order by precipitation amount, and list the station, name, latitude, longitude, and elevation.




Daily Temperature Normals
Calculate the daily normals for the duration of your trip. Normals are the averages for the minimum, average, and maximum temperatures.
You are provided with a function called daily_normals that will calculate the daily normals for a specific date. This date string will be in the format %m-%d. Make sure to use all historic TOBS that match that date string.
Complete the following steps:


Set the start and end date of the trip.


Use the date to create a range of dates.


Strip off the year, and save a list of strings in the format %m-%d.


Use the daily_normals function to calculate the normals for each date string, and append the results to a list called normals.


Load the list of daily normals into a Pandas DataFrame, and set the index equal to the date.


Use Pandas to plot an area plot (stacked=False) for the daily normals, as shown in the following image:




   

