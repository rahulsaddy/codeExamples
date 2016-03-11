
  
import json
import urllib2

# Getting data from Quandl API  - add key to every request
# for each ticker symbol, need to go back to Quandl and get the data
url = "https://www.quandl.com/api/v3/datasets/WIKI/FB/data.json?api_key=7JMJ6VpnxSDZXi_iJmUj" # data
url = "https://www.quandl.com/api/v3/datasets/WIKI/FB/metadata.json?api_key=7JMJ6VpnxSDZXi_iJmUj" # metadata
url = "https://www.quandl.com/api/v3/datasets/WIKI/FB.json?api_key=7JMJ6VpnxSDZXi_iJmUj" # both metadata and data
url = "https://www.quandl.com/api/v3/databases/WIKI/codes.json?api_key=7JMJ6VpnxSDZXi_iJmUj" # List of datasets in Wiki .... not working

# Additional parameters passed through the URL
url = "https://www.quandl.com/api/v3/datasets/WIKI/FB/data.csv?column_index=4&exclude_column_names=true&rows=3&start_date=2012-11-01&end_date=2013-11-30&order=asc&collapse=quarterly&transform=rdiff"


data = json.load(urllib2.urlopen(url))

print data['objects']



# https://www.youtube.com/watch?v=pxofwuWTs7c
# Restaurant search

import urllib2
import json
import numpy              as np
import pandas             as pd
import matplotlib.pyplot  as plt   

api_key = '7JMJ6VpnxSDZXi_iJmUj' 

def quandl_search(ticker)
  url = 'https://www.quandl.com/api/v3/datasets/WIKI/' + ticker + '/data.json?api_key=' + api_key
  data = json.load(urllib2.urlopen(url))
  
quandl_search('WMT')
  
dataFrame = data.values()

# At this point, I am stuck trying to convert the dictionary into a dataframe
# trying to do this with .csv instead
# Help From: https://www.quantstart.com/articles/downloading-historical-futures-data-from-quandl

import urllib2
import json
import numpy              as np
import pandas             as pd
import matplotlib.pyplot  as plt
%matplotlib inline  # tell Ipython to show plots in line

def quandl_search(ticker):
  api_key = '/data.csv?api_key=7JMJ6VpnxSDZXi_iJmUj' 
  url = 'https://www.quandl.com/api/v3/datasets/WIKI/'
        
  try:      
    data = urllib2.urlopen("%s%s%s" % (url, ticker, api_key)).read()
    fc = open('temp_file.csv' , 'w')
    fc.write(data)
    fc.close()
  
    es = pd.read_csv('temp_file.csv', parse_dates=['Date'])

    myplot = es.plot(x='Date', y='Close', legend=None, title="Closing Price and Volumes for %s" % (ticker))
    myplot.set_ylabel("Closing Price")
  
  except urllib2.HTTPError, err:
    if err.code == 404:
      print "This symbol is not avaiable on Quandl Wiki"
    else:
      print "Oops!! Something is wrong ... sorry"
  
   
quandl_search('WMT')


es = pd.read_csv('temp_file.csv', parse_dates=['Date'])
es.head
es.describe()
es['Open'].describe()
  
  
  
  
  
  