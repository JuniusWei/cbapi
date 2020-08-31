# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 10:28:56 2020

@author: Zhiyue June Wei
"""

# Trigger function "trail"
# Importing all the packages
import json
import requests

# Able to set this to be an input parameter of the function
RAPIDAPI_KEY = "31b4706a2emsh1cdf7419915e1dbp1af38cjsnaae32b9e0c29"

# About the input parameters
'''
FOR the organizations, the optional parameters are:
    num_records, since_time, sort_order, name, query, domain_name, locations, 
    types, csv_name, page, socials (for people only)
    label: 1 for organization, 0 for people
In the trigger_api, we basically need:
    url, query, string, headers, response
'''
def trigger_fct(label, since_time = None, sort_order = None, page = 1, name = None, query = None, domain_name = None, locations = None, types = None, socials = None):
    # Used to store the information of the clients
    headers = {
        'x-rapidapi-host': "crunchbase-crunchbase-v1.p.rapidapi.com",
        'x-rapidapi-key': RAPIDAPI_KEY
        }
    # Depending on the input label, adjust the "querystring" and "url".
    if label == 1:
        # For organizations
        querystring = {
        "updated_since": str(since_time), # Number
        "sort_order": sort_order, 
        "page": page, 
        "name": name, 
        "query": query,
        "domain_name": domain_name,
        "locations": locations,
        "types": types
        }
        url = url = "https://crunchbase-crunchbase-v1.p.rapidapi.com/odm-organizations"
    elif label == 0:
        # For people
        querystring = {
        "updated_since": str(since_time), # Number
        "sort_order": sort_order, 
        "page": page, 
        "name": name, 
        "query": query,
        "locations": locations,
        "types": types,
        "socials": socials
        }
        url = "https://crunchbase-crunchbase-v1.p.rapidapi.com/odm-people"
    
    # Get Response object for an HTTP request
    response = requests.request("GET", url, headers=headers, params=querystring)
    # Check the response's status_code to check whether the query is successful or not
    # 200: the query is successful; others: return None
    if(200 == response.status_code):
        return json.loads(response.text)
    else:
        return None
