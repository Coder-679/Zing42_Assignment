import pandas as pd
import os
from sqlalchemy import create_engine

# assign directory
directory = 'Past30Days'
oldestdate_file = "sec_bhavdata_full_16Nov2022bhav.csv"
latestdate_file = "sec_bhavdata_full_27Dec2022bhav.csv"
oldestdate_file = os.path.join(directory, oldestdate_file)
latestdate_file = os.path.join(directory, latestdate_file)

oldest_bhavcopy = pd.read_csv(oldestdate_file)
latest_bhavcopy = pd.read_csv(latestdate_file)

# creating a sqllite database engine and creating table
engine = create_engine('sqlite:///:memory:')

oldest_bhavcopy.to_sql('oldest_bhavcopy_table', engine)
latest_bhavcopy.to_sql('latest_bhavcopy_table', engine)

# SQL query for fetching top 25 gainers between oldest and latest days
query = """
            select SYMBOL , gainpercentage
            from 
            (
            SELECT oldest.SYMBOL as SYMBOL, ((latest.\" CLOSE_PRICE\" - oldest.\" OPEN_PRICE\")/oldest.\" OPEN_PRICE\")*100 as gainpercentage 
            from   
              (select SYMBOL, \" SERIES\", \" OPEN_PRICE\" from oldest_bhavcopy_table) oldest
              JOIN
              (select SYMBOL, \" SERIES\", \" CLOSE_PRICE\" from latest_bhavcopy_table) latest
              on oldest.SYMBOL= latest.SYMBOL AND oldest.\" SERIES\" = latest.\" SERIES\"
            )
            order by gainpercentage desc limit 25
         """
res = pd.read_sql_query(query, engine)
res.to_csv('Question3_Output_Top25_over30days.csv')


