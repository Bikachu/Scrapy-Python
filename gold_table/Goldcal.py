import pandas as pd
import numpy as np
from time import strptime
from datetime import datetime
from functools import reduce

dataset = pd.read_csv("gold.csv")
data = dataset.drop('vol',1)
date_info = data.iloc[:,0]

date_new_format = [datetime.strptime(a,'%b %d, %Y') for a in date_info]
date_new_frame = pd.DataFrame({'col': date_new_format}) 

data['date'] = date_new_frame['col']

def gold():

    global price1
    global price2

    print('\n')
    print("Please choose the date from the following date")
    print(data['date'])
    print('\n')

    date_entry_1 = input('Enter a  start date in YYYY-MM-DD format:  ')

    date1 = datetime.strptime(date_entry_1, "%Y-%m-%d")

    for date_e in data['date']:

        if date1 ==date_e:

            price1 = data.loc[data['date'] ==date1, 'price']

    date_entry_2 = input('Enter a date EARLIER than the start day you just entered in YYYY-MM-DD format:  ')

    date2 = datetime.strptime(date_entry_2, "%Y-%m-%d")

    for date_e in data['date']:

        if date2 ==date_e:

            price2 = data.loc[data['date'] ==date2, 'price']



    n1 = price1.index.values.tolist()[0]

    n2 = price2.index.values.tolist()[0]

    n = price2.index.values - price1.index.values
       
    n = n.tolist()[0]
            
    price_inter = data.iloc[n1:n2+1, 1]
            
    price_list = [float(x.replace(',', '')) for x in price_inter]
            
    price_mean = reduce(lambda x, y: x + y, price_list) / len(price_list)

    price_variance = np.var(price_list)

    print('\n')
    print( str("gold"), price_mean, price_variance)


if __name__ == '__main__':

    gold()