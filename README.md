# Zing42_Assignment

NSE stock data fetcher + query

Acquire Data:

1. Programatically fetch “Securities available for Equity segment (.csv)” file From the URL: https://www.nseindia.com/market-data/securities-available-for-trading
2. Programatically get the latest “bhavcopy” csv file from the following URL - https://www.nseindia.com/all-reports
3. Construct a (relational) database with normalized tables & insert both the data files into it
4. In addition to step 2, programmatically get bhavcopies of the last 30 days instead of just the latest one.

Queries:

1. Write a SQL query to fetch the top 25 gainers of the day sorted in the order of their gains. Gains is defined as [(close - open) / open] for the day concerned as per point 2 above.
2. Get datewise top 25 gainers for last 30 days as per point 4 above.
3. Get a single list of top 25 gainers using the open of the oldest day and close of the latest day of those 30 days as per point 4.

Rules of the game:

Code must be written in python & SQL queries wherever applicable. Jupyter notebooks must not be submitted in the final code, instead proper python / SQL code files must be submitted. You can use any open source tools / libraries to complete this task as required.
