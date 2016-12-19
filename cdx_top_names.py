"""
Author: Siddhartha Gandhi
Date: 2016-12-18
Description: Creates a table of the top traded CDX names.
"""
import re

import bs4
import pandas as pd
import requests


def parse(url, page_name):
    """Given a DTCC URL and the name, parses the HTML table."""
    table = (pd.read_html(url, attrs={'id' : 'dataTable'})[0]
             .pipe(lambda df: df.loc[df.iloc[:, 5].str.isnumeric(), :])
             .iloc[:, :8]
             .assign(period=page_name))
    table.columns = ['Reference Entity', 'Region', 'Index Constituent',
                     'Total Number of Clearing Dealers',
                     'Average Monthly Clearing Dealers',
                     'Average Daily Notional (USD)',
                     'Average Number of Trades per Day', 'DOC Clause %',
                     "Period"]
    return table

source = r'http://www.dtcc.com/repository-otc-data/'
soup = bs4.BeautifulSoup(requests.get(source).text, "html.parser")
links = soup.find_all('a', href=re.compile('top-1000-single-names-'))
data = (pd.concat([parse(source + '/'.join((link.get('href').split('/')[2:])),
                         link.contents[0])
                   for link in links])
        .sort_values(by=['Average Daily Notional (USD)',
                         'Average Number of Trades per Day'],
                     ascending=False)
        .reset_index(drop=True))
