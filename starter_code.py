# Dependencies and Setup
%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# from scipy.stats import sem
import os

# Hide warning messages in notebook
import warnings
warnings.filterwarnings('ignore')

# File to Load
taxi_201801_csv = os.path.join("TaxiData", "yellow_tripdata_201801.csv")
taxi_201802_csv = os.path.join("TaxiData", "yellow_tripdata_2018-02.csv")
taxi_201803_csv = os.path.join("TaxiData", "yellow_tripdata_2018-03.csv")
taxi_201804_csv = os.path.join("TaxiData", "yellow_tripdata_2018-04.csv")
taxi_201805_csv = os.path.join("TaxiData", "yellow_tripdata_2018-05.csv")
taxi_201806_csv = os.path.join("TaxiData", "yellow_tripdata_2018-06.csv")
taxi_201807_csv = os.path.join("TaxiData", "yellow_tripdata_2018-07.csv")
taxi_201808_csv = os.path.join("TaxiData", "yellow_tripdata_2018-08.csv")
taxi_201809_csv = os.path.join("TaxiData", "yellow_tripdata_2018-09.csv")
taxi_201810_csv = os.path.join("TaxiData", "yellow_tripdata_2018-10.csv")
taxi_201811_csv = os.path.join("TaxiData", "yellow_tripdata_2018-11.csv")
taxi_201812_csv = os.path.join("TaxiData", "yellow_tripdata_2018-12.csv")

taxi_zone_lkup_csv = os.path.join("TaxiData", "taxi_zone_lookup.csv")

# Read the Taxi Data
taxi_201801_df = pd.read_csv(taxi_201801_csv)
taxi_zone_lkup_df = pd.read_csv(taxi_zone_lkup_csv)

taxi_zone_lkup_df.head()

############################################################################################


# taxi_zone_lkup_df.nunique()
taxi_zone_dic = pd.Series(taxi_zone_lkup_df.Zone.values, index=taxi_zone_lkup_df.LocationID).to_dict()
taxi_zone_dic
taxi_201801_df['PU_zone_name'] = taxi_201801_df.PULocationID.map(taxi_zone_dic)
taxi_201801_df['DO_zone_name'] = taxi_201801_df.DOLocationID.map(taxi_zone_dic)

taxi_201801_df['trip_time'] = pd.to_datetime(taxi_201801_df["tpep_dropoff_datetime"]) - pd.to_datetime(taxi_201801_df["tpep_pickup_datetime"])

taxi_201801_df['trip_time_min'] = taxi_201801_df['trip_time'].dt.total_seconds()/60 

taxi_201801_df.head()


############################################################################################


groupby_PUzone_taxi_201801 = taxi_201801_df.groupby(["PU_zone_name"])
gb_PU_trip_count = groupby_PUzone_taxi_201801['PULocationID'].count()
gb_PU_trip_rev_avg = groupby_PUzone_taxi_201801['total_amount'].mean()
gb_PU_trip_rev_total = groupby_PUzone_taxi_201801['total_amount'].sum()
gb_PU_trip_time_total = groupby_PUzone_taxi_201801['trip_time_min'].sum()
gb_PU_trip_time_avg = groupby_PUzone_taxi_201801['trip_time_min'].mean()
gb_PU_trip_miles_total = groupby_PUzone_taxi_201801['trip_distance'].sum()
gb_PU_trip_miles_avg = groupby_PUzone_taxi_201801['trip_distance'].mean()

gb_PU_summary_df = pd.DataFrame({"trip_count": gb_PU_trip_count,
                             "avg_revenue": gb_PU_trip_rev_avg,
                             "sum_revenue": gb_PU_trip_rev_total,
                             "total_time_min": gb_PU_trip_time_total,
                             "avg_time_min": gb_PU_trip_time_avg,
                             "total_miles": gb_PU_trip_miles_total,
                             "avg_miles": gb_PU_trip_miles_avg})

gb_PU_summary_df['avg_rev_per_min'] = gb_PU_summary_df['sum_revenue']/gb_PU_summary_df['total_time_min'] 
gb_PU_summary_df['avg_rev_per_min']


gb_PU_summary_df = gb_PU_summary_df.sort_values('avg_rev_per_min', ascending=False)

jfk_df = gb_PU_summary_df.loc[['JFK Airport','Newark Airport','LaGuardia Airport']]

jfk_df

# gb_PU_summary_df