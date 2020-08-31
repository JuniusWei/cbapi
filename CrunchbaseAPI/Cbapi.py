# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 19:34:19 2020

@author: Zhiyue June Wei
"""

from CrunchbaseAPI.DataProcess import get_data

# In this module, we simply wrap up all the method and will put the returned dataframe into a client defined csv file
def Cbapi_query_org(csv_name = None, number = 0, since_time = None, sort_order = None, page = 1, name = None, query = None, domain_name = None, locations = None, types = None, socials = None):
    try:
        # Call get_data(), and set the "label" to be 1 (specified for organization)
        query_df = get_data(1, number = number, since_time = since_time, sort_order = sort_order, page = page, name = name, query = query, domain_name = domain_name, locations = locations, types = types, socials = socials)
    
        # Put the dataframe into an csv file
        query_df.to_csv(csv_name, index = False, encoding = "utf-8")
        
        return query_df
    except Exception as e:
        print("Major Exception Occur!!!")

def Cbapi_query_ppl(csv_name = None, number = 0, since_time = None, sort_order = None, page = 1, name = None, query = None, domain_name = None, locations = None, types = None, socials = None):
    try:
        # Call get_data(), and set the "label" to be 0 (specified for people)
        query_df = get_data(0, number = number, since_time = since_time, sort_order = sort_order, page = page, name = name, query = query, domain_name = domain_name, locations = locations, types = types, socials = socials)
    
        # Put the dataframe into an csv file
        query_df.to_csv(csv_name, index = False, encoding = "utf-8")
        
        return query_df
    except Exception as e:
        print("Major Exception Occur!!!")        

