# SQLAlchemy-Challenge

Owing to its splendid natural beauty, Honolulu, Hawaii is a favourite destination for most travellers.  As a part of this research project,  I was required to analyse the climate dataset (hawaii.sqlite) for Hawaii to determine its suitability to be an ideal holiday destination.

Is travelling to Honolulu enjoyable all throughout the year? 

Hmmmmm.....lets find out!

## Part 1: Climate Analysis and Exploration
Employing SQLAlchemy ORM queries, Pandas, and Matplotlib, I carried out climate analysis and data exploration of the climate database. In order to complete this task, i connected to SQLite database by creating engine, followed by automap_base() to reflect weather tables into classes and finally connecting to python using a SQLAlchemy session.

### Precipitation Analysis
Precipitation data was analysed for the last 1 year of the climate dataset, to get an idea of the recent annual precipation pattern.

![alt text](https://github.com/fbrowther/SQLAlchemy-Challenge/blob/main/Images/Annual_Precipitation_Hawaii.png)

Eventhough there were very few distinct days of outpour, for most part of the year, the sky was clear and showed very little to no precipitation for most part of the year. This was also supported by the summary statistical analysis which showed a mean	of 0.1764, std 0.4602, min of 0.0000, and max of 6.7000 (in inches).


### Station Analysis
In order to determine the most favourable station for holiday within Hawaii, I obtained the list of stations with most activity recorded followed by retrieving its ('USC00519281') previous 12 months of temperature observation data (TOBS). The distribution of TOBS for this station is illustrated as follows -

![alt text](https://github.com/fbrowther/SQLAlchemy-Challenge/blob/main/Images/Temperature%20in%20highly_active_station.png)

The tobs for the most active station 'USC00519281' showed a temperature >65 degree F for >90% of the time for the previous 12 months, indicating why this station showed most activity in the previous year.

### Temperature Analysis - Is there a meaningful difference in temperatures in June and December?
For this, i analysed the weather data to identify the average temperature in June for all stations across all available years. This was repeated for the month of december too. 

##### June average temperature:  74.94411764705882
##### Decempber average temperature:  71.04152933421226

Further analyses showed statistically significant difference in temperature (employing unpaired Ttest) for the month of June and December.
Ttest=31.60372399000329, 
pvalue=3.9025129038616655e-191 

Even though, the averages for June and December are very close and there exists only a small difference in averages between the two months, this difference still was statistically significant (P<0.05) indicating the consistency in the temperatures during those two months.

### Temperature Analysis - what does the historic weather data show for Aug 1st to Aug 7th if one were to make a trip during this time of the year?
Employing python calc_temps function, I calculated the minimum, average, and maximum temperatures for the matching dates from a previous year (e.g., "2017-08-01" - "2017-08-07").

![alt text](https://github.com/fbrowther/SQLAlchemy-Challenge/blob/main/Images/Trip_average_temp.png)

The trip duration (analysed above) had an ideal average temperature of ~80degree F.

### Daily Rainfall Average
The rainfall per weather station using the previous year's matching dates was calculated. The data displayed included precipitation amount, along with the list of the station, name, latitude, longitude, and elevation.

![alt text](https://github.com/fbrowther/SQLAlchemy-Challenge/blob/main/Images/data_stationrain.png)

'USC00519281' seems to be an ideal station to visit in Hawaii as it showed comparatively lower rainful (0.06 inches!) along with an ideal temperature greater than 65 degree F for the majority (>90%) of the time. Therefore, once again this station has maintained its consistancy for being the most preferred station by travelers and therfore considered "most active".

### Daily Temperature Normals
The daily normals for the trip duration was calculated. Normals are the averages for the minimum, average, and maximum temperatures.

![alt text](https://github.com/fbrowther/SQLAlchemy-Challenge/blob/main/Images/TempNormalsforTrip.png)

Temperatures throught the year seemed mild and enjoyable.

## Conclusions
With this analysis Hawaii has truly proved that any weather parameter one were to look at, it had an ideal location for a near perfect weather!
So, do plan your trip whenever you can!!

# WEATHER_APP
Last but the not the least, i have created a weather_app for you to plan your trip to Hawaii. 

I used Flask API to develop this app and employed the queries i used above to execute the analysis for you. 

This app will enable you to query the dataset for -
##### (1) Hawaii precipitation data for the entire duration of the dataset.
##### (2) Hawaii stations for their details.
##### (3) Temperature for a specific date.
##### (4) Temperature (Tmin, Tavr, and Tmax) for a specific date.
##### (5) Temperature (Tmin, Tavr, and Tmax) for a specific duration for potential trips (with start and end date) 
