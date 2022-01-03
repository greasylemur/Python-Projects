************************hstockquote.py Read ME ******************************

Part One: Copyright (c) 2007-2008, Corey Goldberg (corey@goldb.org)
The foundation of this module is written as 'ystockquote.py' which has been
altered to be named 'hstockquote.py' by the party below. This being said
part one is simply pulled from Corey Goldbergs website
http://goldb.org/ystockquote.html.

Part Two: Copyright (c) 2012, Hunter Cronier (hcronier@gmail.com)
This is the part of the module that I have added in hopes to make this module more
usefull.

Click - MakingQTFiles.Py

Part One:

The ystockquote module provides a Python API for retrieving stock data from Yahoo Finance.

This module contains the following functions:
get_all(symbol)
get_price(symbol)
get_change(symbol)
get_volume(symbol)
get_avg_daily_volume(symbol)
get_stock_exchange(symbol)
get_market_cap(symbol)
get_book_value(symbol)
get_ebitda(symbol)
get_dividend_per_share(symbol)
get_dividend_yield(symbol)
get_earnings_per_share(symbol)
get_52_week_high(symbol)
get_52_week_low(symbol)
get_50day_moving_avg(symbol)
get_200day_moving_avg(symbol)
get_price_earnings_ratio(symbol)
get_price_earnings_growth_ratio(symbol)
get_price_sales_ratio(symbol)
get_price_book_ratio(symbol)
get_short_ratio(symbol)
get_historical_prices(symbol, start_yyyymmdd, end_yyyymmdd)

Part Two:

The hstockquote module provided a Python retreiving of the most current list of NYSE Stocks
along with some needed calculations for creating more 'needed' historial data. 

This module contains the following functions:

Nasdaq_File_Maker(fname)  **fname = 'nameoftxtdocumentwithoutsuffix'**
	Nasdaq_File_Maker('Nasdaq_list')
		
Nasdaq_List_Maker(fname)
	Nasdaq_List_Maker('Nasdaq_list')
stockprices(symbol,startdate,enddate)
	stockprices('BCRX', '20120301', '20120929')
stockreturns(symbol,startdate_yyyymmdd,enddate_yyyymmdd)
	stockreturns('BCRX', '20120301', '20120929')
MarketReturn([marketsymbol,marketsymbol,marketsymbol],numberofyears_int)
	MarketReturn(['^GSPC','^IXIC','DJIA'],1)
Beta(stocksymbol, marketsymbol, startdate_yyyymmdd, enddate_yyyymmdd)
	Beta('BCRX', '^GSPC', '20120301', '20120929')
masterkey(stocksymbol, marketsymbol, startdate_yyyymmdd, enddate_yyyymmdd)
	masterkey('BCRX', '^GSPC', '20120301', '20120929')
trendlinePrice(stocksymbol, marketsymbol, startdate_yyyymmdd, enddate_yyyymmdd)
	trendlinePrice('BCRX', '^GSPC', '20120301', '20120929')
trendlineReturn(stocksymbol, marketsymbol, startdate_yyyymmdd, enddate_yyyymmdd)
	trendlineReturn('BCRX', '^GSPC', '20120301', '20120929')