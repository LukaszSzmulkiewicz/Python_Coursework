#!/usr/bin/env python
#!/bin/env python
# Simple regular expression examples

import sys
import fileinput
import re
import string
import matplotlib.pyplot as plt
import pandas as pd
import json
import CountryContinentViewer as CCV

ccv = CCV.CountryContinentViewer()

# getting a dataframe from a class
df_user_data = ccv.df_user_data
# file_name = input("Enter File Name:")
# print("File name is: " + file_name)

# loading the issuu user data 
issuu_user_data = ccv.load_json()

# getting country codes from the json objects 
country_codes = ccv.load_country_codes(issuu_user_data)

# loading dictionary with country names data with country code as a key
dict_country_and_code = ccv.load_countries_to_dictionary()

# loading dictionary with countries and continent names 
dict_country_and_continent = ccv.load_continents_to_dictionary()
            
# creating a data frame with country codes, countries and continents which will be used for plotting  
df_user_data = ccv.assign_countries_and_continents(country_codes, dict_country_and_code, dict_country_and_continent )        

# print(df_user_data)

# for key, value in dict_country_and_continent.items() :
#     print (key)

# plotting results 
ccv.plot_country()
ccv.plot_continent()



