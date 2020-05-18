#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:44:19 2020

@author: kjaisingh
"""


# imports
import numpy as np
import pandas as pd


# function to ensure format of stocks
def formatted(stock):
    if '$' in stock or '.' in stock:
        return True
    else:
        return False


# data retrieval
dataSP = pd.read_csv('SP500.csv')
tickersSP = dataSP.iloc[:, 0].values
tickersSP = tickersSP.tolist()
tickersSP = [x for x in tickersSP if not formatted(x)]

dataNASDAQ = pd.read_csv('NASDAQ.csv')
tickersNASDAQ = dataNASDAQ.iloc[:, 0].values
tickersNASDAQ = tickersNASDAQ.tolist()
tickersNASDAQ = [x for x in tickersNASDAQ if not formatted(x)]

dataNYSE = pd.read_csv('NYSE.csv')
tickersNYSE = dataNYSE.iloc[:, 0].values
tickersNYSE = tickersNYSE.tolist()
tickersNYSE = [x for x in tickersNYSE if not formatted(x)]

# data concatenation
tickers = tickersSP + tickersNASDAQ + tickersNYSE
tickers = list(set(tickers))