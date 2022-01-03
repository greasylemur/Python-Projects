#!/usr/bin/env python
#
#  Copyright (c) 2007-2008, Corey Goldberg (corey@goldb.org)
#
#  license: GNU LGPL
#  
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.


import urllib


"""
This is the "ystockquote" module.

This module provides a Python API for retrieving stock data from Yahoo Finance.

sample usage:
>>> import ystockquote
>>> print ystockquote.get_price('GOOG')
529.46
"""


def __request(symbol, stat):
    url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbol, stat)
    return urllib.urlopen(url).read().strip().strip('"')


def get_all(symbol):
    """
    Get all available quote data for the given ticker symbol.
    
    Returns a dictionary.
    """
    values = __request(symbol, 'l1c1va2xj1b4j4dyekjm3m4rr5p5p6s7').split(',')
    data = {}
    data['price'] = values[0]
    data['change'] = values[1]
    data['volume'] = values[2]
    data['avg_daily_volume'] = values[3]
    data['stock_exchange'] = values[4]
    data['market_cap'] = values[5]
    data['book_value'] = values[6]
    data['ebitda'] = values[7]
    data['dividend_per_share'] = values[8]
    data['dividend_yield'] = values[9]
    data['earnings_per_share'] = values[10]
    data['52_week_high'] = values[11]
    data['52_week_low'] = values[12]
    data['50day_moving_avg'] = values[13]
    data['200day_moving_avg'] = values[14]
    data['price_earnings_ratio'] = values[15]
    data['price_earnings_growth_ratio'] = values[16]
    data['price_sales_ratio'] = values[17]
    data['price_book_ratio'] = values[18]
    data['short_ratio'] = values[19]
    return data
    
    
def get_price(symbol): 
    return __request(symbol, 'l1')


def get_change(symbol):
    return __request(symbol, 'c1')
    
    
def get_volume(symbol): 
    return __request(symbol, 'v')


def get_avg_daily_volume(symbol): 
    return __request(symbol, 'a2')
    
    
def get_stock_exchange(symbol): 
    return __request(symbol, 'x')
    
    
def get_market_cap(symbol):
    return __request(symbol, 'j1')
   
   
def get_book_value(symbol):
    return __request(symbol, 'b4')


def get_ebitda(symbol): 
    return __request(symbol, 'j4')
    
    
def get_dividend_per_share(symbol):
    return __request(symbol, 'd')


def get_dividend_yield(symbol): 
    return __request(symbol, 'y')
    
    
def get_earnings_per_share(symbol): 
    return __request(symbol, 'e')


def get_52_week_high(symbol): 
    return __request(symbol, 'k')
    
    
def get_52_week_low(symbol): 
    return __request(symbol, 'j')


def get_50day_moving_avg(symbol): 
    return __request(symbol, 'm3')
    
    
def get_200day_moving_avg(symbol): 
    return __request(symbol, 'm4')
    
    
def get_price_earnings_ratio(symbol): 
    return __request(symbol, 'r')


def get_price_earnings_growth_ratio(symbol): 
    return __request(symbol, 'r5')


def get_price_sales_ratio(symbol): 
    return __request(symbol, 'p5')
    
    
def get_price_book_ratio(symbol): 
    return __request(symbol, 'p6')
       
       
def get_short_ratio(symbol): 
    return __request(symbol, 's7')
    
    
def get_historical_prices(symbol, start_date, end_date):
    """
    Get historical prices for the given ticker symbol.
    Date format is 'YYYYMMDD'
    
    Returns a nested list.
    """
    url = 'http://ichart.yahoo.com/table.csv?s=%s&' % symbol + \
          'd=%s&' % str(int(end_date[4:6]) - 1) + \
          'e=%s&' % str(int(end_date[6:8])) + \
          'f=%s&' % str(int(end_date[0:4])) + \
          'g=d&' + \
          'a=%s&' % str(int(start_date[4:6]) - 1) + \
          'b=%s&' % str(int(start_date[6:8])) + \
          'c=%s&' % str(int(start_date[0:4])) + \
          'ignore=.csv'
    days = urllib.urlopen(url).readlines()
    data = [day[:-2].split(',') for day in days]
    return data

#  Copyright (c) 2012, Hunter Cronier (hcronier@gmail.com)
#
#  license: GNU LGPL
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.
#
#  Thank You - Corey Goldberg (corey@goldb.org)

import sys
import os
import urllib as urllib
import math as math
import numpy as np
import datetime

#Beta is measure of the volatility, or systematic risk, of a security or a portfolio in comparison to the market as a whole.
#Standard Deviation A measure of the dispersion of a set of data from its mean
#Alpha is a risk-adjusted measure of the so-called active return on an investment

#makine the path file names and allowing for the import of some less used modules
dir_name = os.path.join(os.path.expanduser('~'), 'Desktop')
#opens a file named Nasdaq_Stocks_Listed_all and parses it for the lines of stocks
#This list is available at ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.tx
#and is updated regularly
def Nasdaq_File_Maker(fname):
    nyse_lines=[]
    stocklistfile = open(os.path.join(dir_name, fname + '.txt'), 'w')
    stocklistonlinetxt = urllib.urlopen('ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt')
    for line in stocklistonlinetxt.readlines():	
            stocklistfile.write(str(line))
    stocklistfile.close()
    return nyse_lines
#then it places the lines in a list called nyse_stock_list and pulls out the acronyms from the lines
def Nasdaq_List_Maker(fname):
    nyse_lines = Nasdaq_File_Maker(fname)
    stocklistfile = open(os.path.join(dir_name, fname + '.txt'), 'r')
    for line in stocklistfile.readlines():       
            nyse_lines.append(str(line))
    stocklistfile.close()

    nyse_stock_list = []

    for x in range(len(nyse_lines)):
            stockline = nyse_lines[x]
            stnm = stockline.split('|')
            nyse_stock_list.append(stnm[0])
    return nyse_stock_list
def Nasdaq_Name_List_Maker(fname):
    nyse_lines = Nasdaq_File_Maker(fname)
    stocklistfile = open(os.path.join(dir_name, fname + '.txt'), 'r')
    for line in stocklistfile.readlines():       
            nyse_lines.append(str(line))
    stocklistfile.close()

    nyse_stock_list = []

    for x in range(len(nyse_lines)):
            stockline = nyse_lines[x]
            stnm = stockline.split('-')
            nyse_stock_list.append(stnm[0])
    return nyse_stock_list
    
    

#making the prices into floating point numbers and distributing them as a list
def stockprices(symbol,startdate,enddate):
    stock = get_historical_prices(symbol, startdate, enddate)
    stockSlicer = [x[4] for x in stock][1:]
    for i in range(len(stockSlicer)):
             stockSlicer[i] = float(stockSlicer[i])
    return stockSlicer

#making the returns for the stock stock = ystockquote.get_historical('BCRX'. 20120301', '20120929')
def stockreturns(symbol,startdate,enddate):
    stockReturn=[]
    stock = get_historical_prices(symbol, startdate, enddate)
    stockSlicer = [x[4] for x in stock][1:]
    for i in range(len(stockSlicer)):
             stockSlicer[i] = float(stockSlicer[i])
    for x in range(len(stockSlicer)): 
            if x == (len(stockSlicer)-1):
                    break
            else:
                    stockReturn.append((stockSlicer[x]/stockSlicer[x+1])-1)
    return stockReturn
#This Gathers the market return for the top three valued markets or just what ever you tell it and averages them to get a valued average
def MarketReturn(marketsymbols,numberofyears):
    now = datetime.datetime.now()
    day = now.day
    month = now.month
    yearl = now.year - numberofyears
    dif = datetime.date.today() - datetime.date(yearl,day,month)
    dif = dif.days
    yeara = str(now.year)
    yearb = str(now.year-numberofyears)

    if day < 10:
        day = str(0) + str(day)
    if month < 10:
        month = str(0) + str(month)
    dayb = str(now.day)
    monthb = str(now.month)

    todaya = (yeara + dayb + monthb)
    todayb = (yearb + dayb + monthb)
    stock_1 = stockreturns(marketsymbols[0], todaya, todayb)
    stock_2 = stockreturns(marketsymbols[1], todaya, todayb)
    stock_3 = stockreturns(marketsymbols[2], todaya, todayb)
    stock_1 = math.fsum(stock_1)/dif
    stock_2 = math.fsum(stock_2)/dif
    stock_3 = math.fsum(stock_3)/dif
    marketReturnAverage = [stock_1,stock_2,stock_3]
    marketReturnAverage.append((stock_1 + stock_2 + stock_3)/3)
    return marketReturnAverage

#get the average of three market reads nasdaq s&p dow maybe even using more
#stable reads would work better such as currency oil gold silver etc
def Beta(stocksymbol, marketsymbol, startdate, enddate):
    Reta=[]
    lpha = 0.0
    variance = 0.0
    covariance = 0.0
    standardDeviation = 0.0
    varcountings=[]
    covarcountings=[]
    lphacountings=[]
    stocks = stockreturns(stocksymbol, startdate, enddate)
    market = stockreturns(marketsymbol, startdate, enddate)
    x = math.fsum(market)
    y = math.fsum(stocks)
    n = len(stocks)
    meanx = (x/n)
    meany = (y/n)
    for z in range(len(market)):
        varcountings.append(((market[z]-meanx)*(market[z]-meanx)))
    variance = (math.fsum(varcountings)/n)
    for j in range(len(stocks)):
        covarcountings.append((market[j]-meanx) * (stocks[j]-meany))
    covariance = (math.fsum(covarcountings)/n)
    standardDeviation = math.sqrt(variance)
    eta = (covariance/variance)
    lpha = ((-1*meany)-(eta*(-1*meanx)))
    Reta.append(str(variance))
    Reta.append(str(covariance))
    Reta.append(str(standardDeviation))
    Reta.append(str(eta))
    Reta.append(str(lpha))
    return Reta

def masterkey(stocksymbol, marketsymbol, startdate, enddate):
    key = 0.0
    stock = stockprices(stocksymbol, startdate, enddate)
    market = stockprices(marketsymbol, startdate, enddate)
    stockit = stock[0]
    marketit = market[0]
    key = marketit/stockit
    return key

def trendlinePrice(stocksymbol, marketsymbol, startdate, enddate):
    house = Beta(stocksymbol, marketsymbol, startdate, enddate)
    stocks = stockreturns(stocksymbol, startdate, enddate)
    stp = stockprices(stocksymbol, startdate, enddate)
    b = house[3]
    ystart = stp[0] + (b*(0))
    yend = stp[0] - ((b*(len(stocks)-1))/masterkey(stocksymbol, marketsymbol, startdate, enddate))
    trend = [[0,ystart],[len(stocks)-1,yend]]
    return trend

def trendlineReturn(stocksymbol, marketsymbol, startdate, enddate):
    house = Beta(stocksymbol, marketsymbol, startdate, enddate)
    stocks = stockreturns(stocksymbol, startdate, enddate)
    market = stockreturns(marketsymbol, startdate, enddate)
    b = house[3]
    a = house[4]
    ystart = max(stocks)
    yend = min(stocks)
    xstart = max(market)
    xend = min(market)
    startmaker = a + (b*xend)
    endmaker = a + (b*xstart)
    trend = [[xend,startmaker],[xstart,endmaker]]
    return trend

import matplotlib.pyplot as plt

def graphKeyer(stock, market, begin, end, graphtype):
    plt.clf()
    plt.figure
    exception_series = []
    exception_series_2 = []
    exception_series_3 = []
    allprices = []
#retreives stocks historical prices from the stock name pulled from stockswanted and from the dates 
#pulled from stock.txt this information is places in a list which 
    x_series = get_historical_prices(stock, begin, end)
    print x_series
#creates y_series which is a organized list of dates
    y_series = [x[4] for x in x_series][1:]
    y_series.reverse()
    for i in range(len(y_series)):
            y_series[i] = float(y_series[i])
    nextx_series = get_historical_prices(market, begin, end)
    except_series = [w[4] for w in nextx_series][1:]
    except_series.reverse()
    for i in range(len(except_series)):
            except_series[i] = float(except_series[i])
    first = (except_series[0]/y_series[0])
    middle = (except_series[len(except_series)/2]/y_series[len(y_series)/2])
    last = (except_series[len(except_series)-1]/y_series[len(y_series)-1])
    scalekey = (first+middle+last)/3
    for z in range(len(except_series)):
            exception_series.append(except_series[z]/first)
    for z in range(len(except_series)):
            exception_series_2.append(except_series[z]/scalekey)
    for z in range(len(except_series)):
            exception_series_3.append(except_series[z]/last)            
    q_series = range(len(y_series))
    if graphtype == 0:
        plt.fill_between(q_series,exception_series,y_series,color='r',alpha='.5')
    if graphtype == 1:
        plt.fill_between(q_series,exception_series_2,y_series,color='b',alpha='.5')
    if graphtype == 2:
        plt.fill_between(q_series,exception_series_3,y_series,color='g',alpha='.5')
    if graphtype == 3:
        plt.fill_between(q_series,exception_series_3,y_series,color='g',alpha='.5')
        plt.fill_between(q_series,exception_series_2,y_series,color='b',alpha='.5')
    if graphtype == 4:
        plt.fill_between(q_series,exception_series,y_series,color='r',alpha='.5')
        plt.fill_between(q_series,exception_series_2,y_series,color='b',alpha='.5')
    if graphtype == 5:
        plt.fill_between(q_series,exception_series_3,y_series,color='g',alpha='.5')
        plt.fill_between(q_series,exception_series,y_series,color='r',alpha='.5')
    if graphtype == 6:
        plt.fill_between(q_series,exception_series,y_series,color='r',alpha='.5')
        plt.fill_between(q_series,exception_series_3,y_series,color='g',alpha='.5')
        plt.fill_between(q_series,exception_series_2,y_series,color='b',alpha='.5')
    allprices.append(y_series)
    allprices.append(exception_series)
    plt.plot(q_series, y_series, label = stock)
    plt.plot(q_series, exception_series, label = market)

    #finds the maximum stock price and and the minmum stock price
    cachemax = []
    for t in range(len(allprices)):
            cachemax.append(max(allprices[t]))
            maxprice = max(cachemax)

    cachemin = []
    for s in range(len(allprices)):
            cachemin.append(min(allprices[s]))
            minprice = min(cachemin)

    #Creates the asstetic peices of the graph such as name legend and then it saves it
    plt.xlabel("Days")
    plt.ylabel("Stock Price")
    plt.title("Stocks")

    plt.xlim(0, (len(q_series)-1))
    plt.ylim((minprice), (maxprice))

    plt.legend(loc="upper left")
    plt.savefig(os.path.join(dir_name, 'example_02.png'))

    
    #Other Ideas 
