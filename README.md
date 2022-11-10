# SQLAlchemy-Challenge

As a part of this research project,  I was required to analyse the climate dataset (hawaii.sqlite) for Honolulu, Hawaii! a favourable destination for most travellers owing to its splendid natural beauty. 

Is travelling to Honolulu enjoyable throughout the year? Hmmmmm.....lets find out!

## Part 1: Climate Analysis and Exploration
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

Further analyses, showed statistically significant difference in temperature (employing unpaired Ttest) for the month of June and December.
Ttest=31.60372399000329, 
pvalue=3.9025129038616655e-191 

### Temperature Analysis - what does the historic weather data show for August 1 to August 7 if one were to take a trip during this time of the year?
Employing, python the calc_temps function I calculated the minimum, average, and maximum temperatures for the matching dates from a previous year (e.g., "2017-08-01" - "2017-08-07").

![alt text](https://github.com/fbrowther/SQLAlchemy-Challenge/blob/main/Images/Trip_average_temp.png)


### Daily Rainfall Average
The rainfall per weather station using the previous year's matching dates was calculated. The data was sorted in in descending order by precipitation amount, and along with the list of the station, name, latitude, longitude, and elevation.


### Daily Temperature Normals
The daily normals for the trip duration was calculated. Normals are the averages for the minimum, average, and maximum temperatures.

![alt text](https://github.com/fbrowther/SQLAlchemy-Challenge/blob/main/Images/TempNormalsforTrip.png)




   

