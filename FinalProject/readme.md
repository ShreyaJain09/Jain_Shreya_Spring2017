![alt tag](https://github.com/ShreyaJain09/Jain_Shreya_Spring2017/blob/master/FinalProject/Images/bay_area_bike_share.png)
# PYTHON EXPLORATORY ANALYSIS - BAY AREA BIKE SHARE

## Introduction
Bay Area Bike Share is the region’s bike sharing system with 700 bikes and 61 stations across the region, with different locations in California. It is a company that provides Bay Area residents and visitors with an additional transportation option for getting around the region. Users have the access to pick up and drop the bike from and to any station irrespective of where it was picked from. There are two ways in which users pay for this service.
By getting a yearly subscription – Subscribers
By purchasing a 3-day or 24-hours pass – Customers There is an overtime fee charge if the trip length exceeds thirty minutes with an option to make unlimited number of trips under thirty minutes.

### Dataset
The data set contains the bike data from the year 2015-2016. It contains 3 different csv's that has been used in the analysis:

1. 201608_station_data.csv - Basic information about station locations and capacities.
2. 201608_trip_data.csv - Information about each trip taken using the bike share system.
3. 201608_weather_data.csv - Weather information by day for one station in each city in the bike share program.


### Data Cleansing

- Data cleaning to replace camelcase with underscores
- Replace any empty space in column headers 
- Renaming columns in the dataframe where ever required
- Removing the  outliers with values greater than 99.5th percentile
- Extracting hour, day and month from the Date columns
- Creating SQL connection and loading the data to sql

'''
After cleaning the Data, the cleaned data has been saved to the output folder.
'''

# ANALYSIS 1

DISTRIBUTION OF REGIONS IN BAY AREA BASED ON THE NUMBER OF TRIPS

![ALT TAG](https://github.com/ShreyaJain09/Jain_Shreya_Spring2017/blob/master/FinalProject/AnalysisPlot/Analysis1/landmark.png)

```
1. From the landmark plot it can be seen that the top stations are Mountain View, Palo Alto, San Fransisco and San Jose. It can also be analyzed that San Fransisco gets the highest number of trips followed by San Jose being the half of SF and Mountain View and Palo Alto the other halfs of San Jose.
```

![ALT TAG](https://github.com/ShreyaJain09/Jain_Shreya_Spring2017/blob/master/FinalProject/AnalysisPlot/Analysis1/Start_station.png)

```
2. From the list of 91 stations, it can be seen which station has most of the trips starting from there. It can be analyzed that the stations in SF region is ranked as the highest start station. And the total number of trips started from SF over the year is in between 25000 - 20000.
```

![ALT TAG](https://github.com/ShreyaJain09/Jain_Shreya_Spring2017/blob/master/FinalProject/AnalysisPlot/Analysis1/End_station.png)

```
3. Again, from the list of 61 stations, it can be noticed that SF is the End Stations for most of the trips. And the total number of trips ended at SF over the year is closer to 30000 which more than the start stations.
```

![ALT TAG](https://github.com/ShreyaJain09/Jain_Shreya_Spring2017/blob/master/FinalProject/AnalysisPlot/Analysis1/Start_Terminal.png)

```
4. To confirm that the plot with the start terminal matches the plot with the start stations.
```

![ALT TAG](https://github.com/ShreyaJain09/Jain_Shreya_Spring2017/blob/master/FinalProject/AnalysisPlot/Analysis1/End_Terminal.png)

```
5. To confirm that the plot with the end terminal matches the plot with the end stations.
```

### Conclusion

From the first analysis there are certain things that can be concluded which is
1. San Fransisco is the Top Station in the Bay Area.
2. San Fransisco has most of the rides starting from their station.
3. San Fransisco has even more ride ending at their station.
4. Also, per year around 25000 bikes start from SF and 28000 bikes come back to SF station

It can be infered that more number of bikes should always be presnt in SF area as that has the highest traveling rate and would always be requiring more number of bikes when compared to the other stations.


# ANALYSIS 2

Interaction between all the stations in the bay area using the Haversine Formula defined in the code

```
1. Examining traffic between all the stations

```
![ALT TAG](https://github.com/ShreyaJain09/Jain_Shreya_Spring2017/blob/master/FinalProject/AnalysisPlot/Analysis2/StationUsage_customers.png)
Traffic between stations for customers


![ALT TAG](https://github.com/ShreyaJain09/Jain_Shreya_Spring2017/blob/master/FinalProject/AnalysisPlot/Analysis2/StationUsage_subscribers.png)
Traffic between stations for subscribers

```
Created a Heat Map to get the number of rides determination between all the stations for both the Subscribers and the Customers. From the heat map it can be seen that station terminal from 40 -90 is all having heavy traffic between stationa and this also confirm the heavy traffic in SF. The heat map also shows the relation between one station to another and the relations between stations. For customers heat map it is seen that there is not much of traffic for customers as they would be the travelers who are visiting bay area and prefer takin smaller stops.
```
### Conclusion
It can be concluded that 
1. The distribution of traffic is different for customers and subscribers.
2. A fewer stations have a huge percentage of traffic compared to the other stations. 


# ANALYSIS 3
```
1. Calculating the total trips made in the whole dataset using the usage_stats() function. Also, analyzed the statistics in respect to how the trip looked like in the over all sense. 
```
![ALT TAG](https://github.com/ShreyaJain09/Jain_Shreya_Spring2017/blob/master/FinalProject/AnalysisPlot/Analysis3/usage_stats.png)
It can be noted that there were 312121 trips made in the year 2015-2016 in the Bay Area. Also it is surprising to note that the average trip duration is greater than the median trip duration which explains the shorter trips in the analysis 1.


```
2. Using the data_plot function to see how these trips are layed down based on the duration of time. 
What does the distribution of trip durations look like?
```
![ALT TAG](https://github.com/ShreyaJain09/Jain_Shreya_Spring2017/blob/master/FinalProject/AnalysisPlot/Analysis3/TripsByDurationFilter2.png)
It looks pretty strange. Looking at the duration value on x-axis it can be seen that most of the rides are in the duration of less than 1650. Since all the rides are expected to be 30 minutes or less as there is an overage charges for longer rides in one single trip. It shows the span of duration mostly upto 1200 minutes which is equivalent to around 17 hours.
From the statistics that I got from the usage_stats, it was expected that some trips would be really long which brings the average value to be so much higher than the median.

To understand the data better, using the visualization function. Setting filters as a list of conditions for the data points. Limiting the Duration to be less than 60 minutes.
![ALT TAG](https://github.com/ShreyaJain09/Jain_Shreya_Spring2017/blob/master/FinalProject/AnalysisPlot/Analysis3/TripsByDuration.png)
This also does not give a lot of idea about the trip. To understand it better, plotting the graph for all the trips under 1600 minutes.

![ALT TAG](https://github.com/ShreyaJain09/Jain_Shreya_Spring2017/blob/master/FinalProject/AnalysisPlot/Analysis3/TripsByDurationFilter1.png)
Yes, this looks better. It can be seen that most of the trips range in between 300-700 minutes in length. As it can be noted that none of the trips are for 0 minutes, the left side of the plot is above 0. So even that can be removed.
Also changing the bin widht to 100 for better visualization of the data.

![ALT TAG](https://github.com/ShreyaJain09/Jain_Shreya_Spring2017/blob/master/FinalProject/AnalysisPlot/Analysis3/TripsByDurationFilter3.png)
It can be interpreted that the bin with 100 minutes has the most trip for the range 355 - 450 minutes, whicn represents aproximately 40000 trips made for this time duration. To understand the data better, the bin width and few other filters can be changed to understand different scenarios of the data.

### Conclusion 
From this analysis, it can be concluded that 
1. The total number of trips in the Bay Area for the year 2015-2016 were 312121 and the average duration of trips was 698.95 minutes.
2.  25% of trips are shorter than 353.00 minutes.
3. 25% of trips are longer than 731.00 minutes.
4. From the graphs, it is seen that the maximum trips took place between 350-450 minutes which justifies with the shorter and longer rides that took place. 


# ANALYSIS 4

```
Using the second argument of the function usage_stats() to count up the trips across a selected variable called Subscription_Type , to display the information in the plot. This plot shows the number of trips made by the customers and how many were made by the subscribers.
```
![ALT TAG](https://github.com/ShreyaJain09/Jain_Shreya_Spring2017/blob/master/FinalProject/AnalysisPlot/analysis4/Subscription.png)
It can be inferred that around 10% of the total trips were made by Customers and the remaining 90% were made by the Subscribers. Customers made around 30000 trips where as the subscribers made around 280000 which is equivalent to the total number of trips that is 312121.

![ALT TAG](https://github.com/ShreyaJain09/Jain_Shreya_Spring2017/blob/master/FinalProject/AnalysisPlot/analysis4/SubscriptionMetrics.png)
Perfect. This gives the a very good picture of the spread of customers and subscribers in the dataset. As seen in the graphs above it can be said that customers are 10% of the total riders. From how it should have been, the customers having a high median duration of rentals compared to that of subscribers.


### Conclusion
It can be concluded that,
1. The duration  and the median distance travelled for the customers is twice as that of the subscribers.
2. The 90% of the total trips are made by the Subscribers and the 10% were made by the customers.

# ANALYSIS 5

Now that I know the trips made between the different subscription types and different places where the trips happened, I would want to know about the overtime fees and the traffic during the hour of the day.
Plot to see the duration of rides for the different subscription type and their overtime.

![ALT TAG](https://github.com/ShreyaJain09/Jain_Shreya_Spring2017/blob/master/FinalProject/AnalysisPlot/Analysis5/WeekPlot.png)
The plot shows the trend of trips made by the subscribers and the customers. Also,from the plot it can be seen that that mostly customers are the ones who pays the overtime fee.

![ALT TAG]()
It tells us the exact over time feee paid by the subscribers and the customers. 29% of customers pay an overtime fee and very negligible amount of subscribers would pay the overtime fee. This alos matches from the graph plotted above which gives us a very good visualiztion of customers paying overtime fee.

![ALT TAG](https://github.com/ShreyaJain09/Jain_Shreya_Spring2017/blob/master/FinalProject/AnalysisPlot/Analysis5/WeekTrend.png)

![ALT TAG](https://github.com/ShreyaJain09/Jain_Shreya_Spring2017/blob/master/FinalProject/AnalysisPlot/Analysis5/Pattern%20over%20the%20week.png)
It can be seen that the weekday peak hours for Subscribers is in the morning at around 8 AM and for weekdays it is different
Where as the weekday peek hours for cutomers is very random which shows that they are mostly tourists visiting the place.
Also, the graph shows the traffic at every hour of the day for the entire week for both customers and subscribers.

### Conclusion
It can be concluded that,
0% of subscribers pay overtime fee, whereas 26% of casual customers pay overtime fee.
Patterns between subscribers and casual customers over the course of the day is very different.

# To Summarize:

1. Top regions where there are bike rentals are Mountain View, Palo Alto, San Fransisco and San Jose, San Fransisco having the highest bike rentals pick ups and drops.
2. Traffic distribution for customers and subscribers between the loactions of different station terminals by taking in account their GPS location.
3. Data status which shows that total bike rentals that they get over the year is 312121 and the different stastitical analysis.
4. Distribution of customers and subscribers duration  and the median distance travelled to show that 90% of the total trips are made by the Subscribers and the 10% were made by the customers.
5. Patterns between subscribers and casual customers over the course of the day and the percentage of overtime fee that is paid by the customers.

