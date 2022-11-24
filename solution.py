#!/usr/bin/env python
#!/bin/env python


import argparse
import CountryContinentViewer
import BrowserViewer
import HelperMethods

ccv = CountryContinentViewer.CountryContinentViewer()
bv = BrowserViewer.BrowserViewer()
hm = HelperMethods.HelperMethods()

# function to task 2 setup
def task_2_setup(issuu_user_data, taks_number):
    # getting country codes from the json objects 
    country_codes = ccv.load_country_codes(issuu_user_data)
   
    # converting list of country codes to dataframe
    df_country_codes = ccv.list_to_dataframe(country_codes)
   
    # count country codes occurrences
    df_country_codes_count = ccv.count_country_codes_occurrences(df_country_codes)
                
    if taks_number == '2a':
      # loading dataframe with country names 
      df_country_and_code = ccv.load_countries_to_dataframe()

      # creating a data frame with country codes and countries which will be used for plotting  
      df_user_data = ccv.assign_countries_to_country_codes(df_country_codes_count, df_country_and_code)
    elif taks_number =='2b':
      # loading dataframe with continent names 
      df_continents = ccv.load_continents_to_dataframe()

      # creating a data frame with country codes and continents   
      df_continent_and_country = ccv.assign_continents_to_country_codes(df_country_codes_count, df_continents)

      # counting continent occurrences
      df_user_data = ccv.count_continents_occurrences(df_continent_and_country)

    return df_user_data

#function to task 3 setup
def task_2_setup(issue_user_data, taks_number):
    #getting user agent code from the json objects
    browser_codes = bv.load_browser_codes(issue_user_data)
    
    #converting list of browser codes to dataframe
    df_browser_codes = bv.list_to_dataframe(browser_codes)

    #count browser code occurences
    df_browser_codes_count = bv.count_browser_codes_occurrences(df_browser_codes)

    if taks_number == '3a':
      #loading dataframe with browser codes
      df_browser_data = df_browser_codes_count



def run(args):
  user_uuid = args.user_uuid # user UUID
  doc_uuid = args.doc_uuid # document UUID
  task_id = args.task_id # task id
  file_name = args.file_name # file name
  
  # loading the issuu user data 
  issuu_user_data = hm.load_json(file_name)
  # getting a dataframe from a class
      

  if task_id == "2a":
      df_user_data = task_2_setup(issuu_user_data, task_id)
      return ccv.plot_country(df_user_data)
  elif task_id == "2b":
      df_user_data = task_2_setup(issuu_user_data, task_id)
      return ccv.plot_continent(df_user_data)
  elif task_id == "3a":
      df_browser_data = task_2_setup(issuu_user_data, task_id)
      return bv.plot_browsers(df_browser_data)
  elif task_id == "3b":
    return print("task 3b is running")
  elif task_id == "4":
    return print("task 4 is running")
  elif task_id == "5d":
    return print("task 5d is running")
  elif task_id == "6":
    return "task 6 is running"
  elif task_id == "7":
    return "task 7 is running"

def main():
  parser=argparse.ArgumentParser(description="Run a coursework with a command line interface")
  parser.add_argument("-u",help="user_uuid" ,dest="user_uuid", type=str, required=False)
  parser.add_argument("-d",help="doc_uuid" ,dest="doc_uuid", type=str, required=False)
  parser.add_argument("-t",help="task_id" ,dest="task_id", type=str, required=True)
  parser.add_argument("-f",help="file_name", dest="file_name", type=str, required=True)
  parser.set_defaults(func=run)
  args=parser.parse_args()
  args.func(args)

if __name__=="__main__":
	main()