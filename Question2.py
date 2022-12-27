import pandas as pd
import os
from jugaad_data.nse import full_bhavcopy_save
from jugaad_data.holidays import holidays
from sqlalchemy import create_engine


# fetching past 30 days data
date_range_2022 = pd.bdate_range(start='16/11/2022', end = '27/12/2022',freq='C', holidays = holidays(2022))
dates_2022 = [x.date() for x in date_range_2022]
print(len(dates_2022))

# iterating over past 30 days
for dates in dates_2022:
    full_bhavcopy_save(dates, "Past30Days")


# assign directory
directory = 'Past30Days'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    bhavcopy = pd.read_csv(f)

    # creating a sqllite database engine and creating table
    engine = create_engine('sqlite:///:memory:')
    bhavcopy.to_sql('bhavcopy_table', engine)

    # SQL query for fetching top 25 gainers on current date
    query = """ 
               SELECT *
                FROM ( 
                     SELECT bhavcopy_table.*, ((\" CLOSE_PRICE\" - \" OPEN_PRICE\") / \" OPEN_PRICE\")*100 as gainpercentage 
                     FROM bhavcopy_table
                     ) 
                order by gainpercentage desc limit 25 
            """
    res = pd.read_sql_query(query, engine)

    fout = os.path.join('Question2_Output_Top25_Past30Days', 'Top25'+filename)
    res.to_csv(fout)
