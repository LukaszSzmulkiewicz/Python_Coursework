#!/usr/bin/env python
#!/bin/env python


import argparse
import CountryContinentViewer
import HelperMethods
import ReaderCounter
import BrowserViewer
import tkinter as tk

ccv = CountryContinentViewer.CountryContinentViewer()
hm = HelperMethods.HelperMethods()
rc = ReaderCounter.ReaderCounter()
bv = BrowserViewer.BrowserViewer()

# function to task 2 setup
def task_2_setup(file_name, taks_number):
   # loading the issuu user data 
  issuu_user_data = hm.load_json(file_name)

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
def task_3_setup(file_name, taks_number):
    # loading the issuu user data 
    issuu_user_data = hm.load_json_specific(file_name, 'visitor_useragent')
   
    if taks_number == "3a":
      #converting list of browser codes to dataframe
      df_browser_codes = bv.browsers_to_dataframe(issuu_user_data)

      #count browser code occurences
      df_browser_codes_count = bv.count_browser_codes_occurrences(df_browser_codes)

      return df_browser_codes_count
    elif taks_number == "3b":
      #getting user agent code from the json objects
      list_browser_codes = bv.parse_user_agents(issuu_user_data)

      #converting list of browser codes to dataframe
      df_browser_codes = bv.browsers_to_dataframe(list_browser_codes)

      #count browser code occurences
      df_browser_codes_count = bv.count_browser_codes_occurrences(df_browser_codes)

      return df_browser_codes_count

# method to setup data for plotting of task 4
def task_4_setup(file_name):
  #loading data from json
  issuu_user_data = hm.load_json_re(file_name, 'event_readtime')

  # loading readers from a list retrieved from json
  list_user_data = rc.load_readers(issuu_user_data)
  
  # assignment of column names to df
  df_readers = rc.assign_column_names_to_df(list_user_data)

  # returning readers count
  df_readers_count = rc.best_readers_count(df_readers)

  df_result = rc.return_10_best_readers(df_readers_count)
  return df_result

def task_7_setup():
  

  def get_task2a_command():
    df_user_data = task_2_setup(file_name.get(), '2a')
    return ccv.plot_country(df_user_data)
  
  def get_task2b_command():
    df_user_data = task_2_setup(file_name.get(), '2b')
    return ccv.plot_continent(df_user_data)
    
  def get_task3a_command():
    df_user_data = task_3_setup(file_name.get(), '3a')
    return bv.plot_browsers(df_user_data)
  
  def get_task3b_command():
    df_user_data = task_3_setup(file_name.get(), '3b')
    return bv.plot_browsers(df_user_data)
  
  def get_task4_command():
    df_user_data = task_4_setup(file_name.get())
    return rc.plot_readers(df_user_data)
  
  def get_task5_command():
    print("task 5 to be done")
  
  def get_task6_command():
    print("task 6 to be done")
  
  
  root = tk.Tk()
  root.geometry("300x500")
  root.title("Coursework_issuu_10")

  label = tk.Label(root, text="File Name", font=("Arial",16))
  label.pack()

  file_name = tk.Entry(root)
  file_name.pack()

  button_Task2a = tk.Button(root, text="Task 2a", font=("Arial",16), command=lambda: get_task2a_command())
  button_Task2a.pack(padx=10, pady=10)
  button_Task2b = tk.Button(root, text="Task 2b", font=("Arial",16), command=lambda: get_task2b_command())
  button_Task2b.pack(padx=10, pady=10)
  button_Task3a = tk.Button(root, text="Task 3a", font=("Arial",16), command=lambda: get_task3a_command())
  button_Task3a.pack(padx=10, pady=10)
  button_Task3b = tk.Button(root, text="Task 3b", font=("Arial",16), command=lambda: get_task3b_command())
  button_Task3b.pack(padx=10, pady=10)
  button_Task4 = tk.Button(root, text="Task 4", font=("Arial",16), command=lambda: get_task4_command())
  button_Task4.pack(padx=10, pady=10)
  button_Task5 = tk.Button(root, text="Task 5d", font=("Arial",16), command=lambda: get_task5_command())
  button_Task5.pack(padx=10, pady=10)
  button_Task6 = tk.Button(root, text="Task 6", font=("Arial",16), command=lambda: get_task6_command())
  button_Task6.pack(padx=10, pady=10)

    

  root.mainloop()


def run(args):
  user_uuid = args.user_uuid # user UUID
  doc_uuid = args.doc_uuid # document UUID
  task_id = args.task_id # task id
  file_name = args.file_name # file name
      

  if task_id == "2a":
    df_user_data = task_2_setup(file_name, task_id)
    return ccv.plot_country(df_user_data)
  elif task_id == "2b":
    df_user_data = task_2_setup(file_name, task_id)
    return ccv.plot_continent(df_user_data)
  elif task_id == "3a":
    df_user_data = task_3_setup(file_name, task_id)
    return bv.plot_browsers(df_user_data)
  elif task_id == "3b":
    df_user_data = task_3_setup(file_name, task_id)
    return bv.plot_browsers(df_user_data)
  elif task_id == "4":
    df_user_data = task_4_setup(file_name)
    return rc.plot_readers(df_user_data)
  elif task_id == "5d":
    return print("task 5d is running")
  elif task_id == "6":
    return "task 6 is running"
  elif task_id == "7":
    return task_7_setup()

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