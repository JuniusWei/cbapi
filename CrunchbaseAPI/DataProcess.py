# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 14:40:05 2020

Goal: After getting the api_response from the trigger_api module
    process the data into a dataframe, and write it into a csv file.
@author: Zhiyue June Wei
"""
import pandas as pd
import threading
from CrunchbaseAPI.trigger_api import trigger_fct

# Global variable (the data frame that store the records)
df_result = []

# Function that will be called in the Thread object (input the id of the page)
def thread_function(page_id, label, since_time, sort_order, name, query, domain_name, locations, types, socials):
    print("This is {}-th page reading!".format(page_id))
    global df_result
    
    # Obatin the raw data in the page specified by the page_id
    total_data = trigger_fct(label, since_time, sort_order, page_id, name, query, domain_name, locations, types, socials)
    
    for data_pt in total_data["data"]["items"]:
        # Extract the properties of each satisfied data point
        pro_info = data_pt["properties"]
        df_result = df_result.append(pro_info, ignore_index = True)
    

# Method: return a number of records (the number needs to be specific)
def get_data(label, number = 0, since_time = None, sort_order = None, page = 1, name = None, query = None, domain_name = None, locations = None, types = None, socials = None):
    global df_result
    
    # Call the trigger_fct function to get the api_response
    raw_result = trigger_fct(label, since_time, sort_order, page, name, query, domain_name, locations, types, socials)
    
    # The number of the records that are going to be returned
    total_number = raw_result["data"]["paging"]["total_items"]
    number_per_page = raw_result["data"]["paging"]["items_per_page"]
    
    # Check the validity of the input number of the results
    if number < 0:
        print("WARNING: Please input a valid query number (non-negative)!")
        return
    elif number == 0:
        print("WARNING: The number is zero, will return no result!")
        return
    else:
        # Create an empty dataframe for returning the results
        df_result = pd.DataFrame(columns = raw_result["data"]["items"][0]["properties"].keys())
        
        # Adjust the input number
        if number >= total_number:
            number = total_number
        
        # Handling the pages
        page_number = number // number_per_page
        if number % number_per_page:
            last_page = number % number_per_page
        #print(page_number, last_page)
        
        # Using multi-threading to handle the page reading
        threads = list()
        for page in range(page_number):
            print("This is the {}-th page".format(page + 1))
            x = threading.Thread(target = thread_function, args = (page + 1, label, since_time, sort_order, name, query, domain_name, locations, types, socials))
            threads.append(x)
            x.start()
        
        for thread_element in threads:
            thread_element.join()
        
        # Handle the last_page
        last_page_data = trigger_fct(label, since_time, sort_order, page_number + 1, name, query, domain_name, locations, types, socials)
        count = 0
        for last_item in last_page_data["data"]["items"]:
            if count >= last_page:
                break
            #print(last_item["properties"])
            df_result = df_result.append(last_item["properties"], ignore_index = True)
            count += 1
        
        return df_result
