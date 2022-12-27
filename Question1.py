import pandas as pd
from sqlalchemy import create_engine


# Acquiring data


def fetchdata_constructdb():

    #################### fetching data ##############################

    ## 1 - fetching “Securities available for Equity segment (.csv)”
    eqsecurity = pd.read_csv('https://archives.nseindia.com/content/equities/EQUITY_L.csv')
    # eqsecurity.to_csv(r'eq.csv')

    ## 2 - fetching the latest “bhavcopy” csv
    bhavcopy = pd.read_csv('https://archives.nseindia.com/products/content/sec_bhavdata_full_27122022.csv')
    # bhavcopy.to_csv(r'bhav.csv')


    #################### constructing relational datamodel###########
    # Create the db engine
    engine = create_engine('sqlite:///:memory:')

    # Store the dataframe as a table
    eqsecurity.to_sql('eqsecurity_table', engine)
    bhavcopy.to_sql('bhavcopy_table', engine)

    #################### SQL Queries #################################

    ## 1

    #SQL query for fetching top 25 gainers on 27th December 2022
    query = """ 
                SELECT SYMBOL, gainpercentage 
                FROM ( 
                     SELECT SYMBOL, ((\" CLOSE_PRICE\" - \" OPEN_PRICE\") / \" OPEN_PRICE\")*100 as gainpercentage 
                     FROM bhavcopy_table
                     ) 
                order by gainpercentage desc limit 25 
            """
    res = pd.read_sql_query(query, engine)
    res.to_csv('Question1_Output_Top25_27Dec.csv')


fetchdata_constructdb()
