# Title: NYC Yellow Taxi Data

Due to the recent explosion of ridesharing apps (uber & Lyft), yellow taxi drivers are struggling to stay ahead of the competition. We decided to investigate ways for taxi drivers to maximize their revenue.

## Summary
Research Question: 
* What factors have the highest impact on a taxi driver’s revenue per unit of time?
  
In this report, we will compare the relationship between revenue and the following independent variables 
* Pickup Location
* Dropoff Location
* Passenger number
* Rate ID
* Time of Day
* Day of Week

Our Hypotheses are:
* H1: Rides starting in midtown would yield the most revenue
* H2: Rate Code (e.g. trips to airport) would be the strongest determinant in revenue generation
* H3: Weekday rush hour trips (7-10am and 4-7pm) would generate more revenue than weekend rides and non-rush hour trips
* H4: Higher passenger counts would yield higher revenue than low passenger count rides

We plan to examine what trip data says about areas in New York, and come up with recommendations for taxi drivers to get the most out of their time on the road.

Data Source:
* NYC Taxi and Limosine Comission 2018 Yellow Taxi Trip Data, which provides variables such as:
 * Pickup and dropoff time
 * Pickup and dropoff location (zone ID)
 * Passenger count
 * Rate type
 * Trip distance
 * Total amount (inc. fares, fees, taxes, tips)
 * Payment type
... and others, totaling 17 columns and 8MM+ rows.
 
 
 
