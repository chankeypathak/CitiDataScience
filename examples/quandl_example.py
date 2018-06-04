#!/usr/bin/env python3

import pandas as pd
import quandl

#quandl.ApiConfig.apikey = 'Uvc7KJzykfvBLjVkNDy2'
quandl.ApiConfig.apikey = 'Uvc7KJzykfvBLjVkNDy2'

data = quandl.get_table('WIKI/PRICES',ticker = ['AAPL','MSFT','GOOG'],
                         qopts = {'columns':['ticker','date','adj_close']},
                         date = {'gte':'2015-12-31','lte':'2016-12-31'},
                         paginate=True)

data.head()


