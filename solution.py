#!/usr/bin/env python
#!/bin/env python
# Simple regular expression examples


import argparse
import CountryContinentViewer as CCV

ccv = CCV.CountryContinentViewer()

# function to task 2 setup
def task_2_setup(issuu_user_data):
    df_user_data = ccv.df_user_data
      
    # getting country codes from the json objects 
    country_codes = ccv.load_country_codes(issuu_user_data)

    # loading dictionary with country names data with country code as a key
    dict_country_and_code = ccv.load_countries_to_dictionary()

    # loading dictionary with countries and continent names 
    dict_country_and_continent = ccv.load_continents_to_dictionary()
                
    # creating a data frame with country codes, countries and continents which will be used for plotting  
    ccv.assign_countries_and_continents(country_codes, dict_country_and_code, dict_country_and_continent )  



def run(args):
  user_uuid = args.user_uuid # user UUID
  doc_uuid = args.doc_uuid # document UUID
  task_id = args.task_id # task id
  file_name = args.file_name # file name
  
  # loading the issuu user data 
  issuu_user_data = ccv.load_json(file_name)
  # getting a dataframe from a class
      

  if task_id == "2a":
      task_2_setup(issuu_user_data)
      return ccv.plot_country()
  elif task_id == "2b":
      task_2_setup(issuu_user_data)
      return ccv.plot_continent()
  elif task_id == "3a":
    return print("task 3a is running")
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