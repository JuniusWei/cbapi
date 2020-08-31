# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 19:55:27 2020

@author: Zhiyue June Wei
"""

from CrunchbaseAPI import Cbapi_query_ppl, Cbapi_query_org
from datetime import datetime, date, time, timedelta, timezone

def test_fct():
    # Find the orginization/people that are updated since the previous day's timestamp
    # Convert the time according to the required format
    current_date = datetime.combine(date.today(), time(0, 0, 0))
    yesterday_date = current_date - timedelta(days=1)
    yday_timestamp_utc = int(yesterday_date.replace(tzinfo=timezone.utc).timestamp())
    print("Scanning Crunchbase API for company updates on " + yesterday_date.strftime("%m/%d/%YYYY"))
    print(yday_timestamp_utc)
    
    ppl_df = Cbapi_query_ppl("output_ppl.csv", number = 250, since_time = yday_timestamp_utc, page = 1)
    org_df = Cbapi_query_org("output_org.csv", number = 250, since_time = yday_timestamp_utc, page = 1)
    
    print(ppl_df.head())
    print(org_df.head())
    
if __name__ == "__main__":
    test_fct()




