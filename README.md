# Scrapy-Python
Crawling data and using machine learning to analyze the data

Language: Python
---------------------------
Framework: Scrapy, Scikit-Learn, Pandas, Numpy
-------




---------------------------------------------------------------------------------------------------------------------------
1. write a program to fetch the historical prices and dates of gold and silver from these 2 URLs:

•            https://www.investing.com/commodities/gold-historical-data

•            https://www.investing.com/commodities/silver-historical-data

and store them locally (in a file or database).



 
 
 ---------------------------------------------------------------------------------------------------------------------------

2. write a second program that takes the following 3 command line arguments:

•            Start date (in the format 2017-05-10)

•            End date (in the format 2017-05-22)

•            Commodity type (either "gold" or silver”)


and then returns (via the locally stored data) the mean and variance of the commodity’s price over the specified date range.

For example, the program might be called like so:

                             ./getCommodityPrice 2017-05-01 2017-05-03 gold

and would print out a tuple such as:

                               gold 1253.66 35.79

 


-----------------------------------------------------------------------------------------------------------------------
3. write a program to help you decide if the previous gold or silver prices are good predictors for their future prices.

Also do the same to check if an increase or decrease in the price is predictable. (There is no need to do the actual prediction.)





-----------------------------------------------------------------------------------------------------------------------
How to execute the files:
----------------

1. How to run this program in CMD:

              - extract the folder "gold_table" at the desktop
   
              - enter cd Desktop
   
              - enter cd gold_table
   
              - enter scrapy crawl gold
   
then the program would run and fetch the gold historical table information.



----------------------------------------------
2.  For the second program, the code is Goldcal.py at gold_table/.

To run this program in cmd:

              - cd Desktop
              
              - cd gold_table
              
              - python Goldcal.py
              
              - enter two dates (the available date will be provided before you enter)
              
              - the second date entered should be "earlier" than the first date you entered, for example: if you entered 2018-02-18, then the next date should like 2018-02-16, not date like 2018-02-19.
 
 
 
 ---------------------------------------------
 3. I choose the polynomial regression model to train the data, degree = 4.
 The code is analysis.py at gold_table/


