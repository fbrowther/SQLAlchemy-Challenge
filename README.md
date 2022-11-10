# SQLAlchemy-Challenge

As a part of this research project,  I was required to analyse the climate dataset (hawaii.sqlite) for Honolulu, Hawaii! a favourable destination for most travellers; owing to its spelendid natural beauty. 

Is travelling to Honolulu enjoyable throughout the year? Hmmmmm.....lets find out!

##Part 1: Climate Analysis and Exploration
Employing SQLAlchemy ORM queries, Pandas, and Matplotlib, I carried out climate analysis and data exploration of the climate database. IN order to complete this task i connected to SQLite database (by a creating engine), followed by automap_base() to reflect weather tables into classes and finally connecting to python using a SQLAlchemy session.


### Precipitation Analysis
Precipitation data was analysed for the last 1 year of the climate dataset to get an idea of the most (recent) annual precipation pattern (in inches).

![alt text](https://github.com/fbrowther/SQLAlchemy-Challenge/blob/main/Images/Annual_Precipitation_Hawaii.png)

Eventhough, there were very few distinct days of outpour; for most part of the year, the sky was clear and showed very little to no precipitation for most part of the year. This was also supported by the summary statistical analysis which showed a mean	of 0.048843, std 0.205197, min of 0.000000, and max of 2.620000.

Yay!! Let's find out more!


