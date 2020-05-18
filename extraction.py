#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:44:19 2020

@author: kjaisingh
"""

import numpy as np
import pandas as pd


data = pd.read_csv('SP_500.csv')
tickers = data.iloc[:, 0].values
tickers = tickers.tolist()