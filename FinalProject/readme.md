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

