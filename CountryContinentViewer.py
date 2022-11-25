#!/usr/bin/env python
#!/bin/env python

import matplotlib.pyplot as plt
import pandas as pd

class CountryContinentViewer:

  # df_user_data = pd.DataFrame(columns=[ 'country_code', 'country', 'continent', 'counts'])

  def load_country_codes(self, issuu_user_data):
    country_codes = []
    for country in issuu_user_data:
        country_codes.append(country["visitor_country"])
    return country_codes
    
  def load_countries_to_dataframe(self):
    df_country_and_code = pd.read_csv("data/countries.csv")
    return df_country_and_code
  
  def load_continents_to_dataframe(self):
    df_continent_and_code = pd.read_csv("data/continents.csv")
    return df_continent_and_code

  def list_to_dataframe(self, country_codes):
    df_country_codes = pd.DataFrame.from_dict(country_codes)
    return df_country_codes

  def count_country_codes_occurrences(self, df_country_codes):
    df_country_codes_new = df_country_codes.value_counts().rename_axis('country_code').reset_index(name='counts')  
    return df_country_codes_new

  def count_continents_occurrences(self, df_continent_and_country):   
    df_continent_and_country_new = df_continent_and_country.groupby(["continent"]).sum().reset_index()  
    return df_continent_and_country_new

  def assign_countries_to_country_codes(self, df_country_codes_new, df_country_and_code):
    df_user_data_result = pd.merge(df_country_codes_new, df_country_and_code, on="country_code")
    return df_user_data_result

  def assign_continents_to_country_codes(self, df_country_codes_new, df_continent_and_code):
    df_user_data_result = pd.merge(df_country_codes_new, df_continent_and_code, on="country_code")
    return df_user_data_result


  def plot_country(self, df_user_data):
    
    names = df_user_data['country']
    values = df_user_data['counts']
    fig, (ax1) = plt.subplots(figsize=(25, 15))
    ax1.bar(names, values)
    ax1.set_xticklabels(names, rotation=55, ha='right')
    plt.show()


  def plot_continent(self, df_user_data):

    names = df_user_data['continent']
    values = df_user_data['counts']
    fig, (ax1) = plt.subplots(figsize=(25, 15))
    ax1.bar(names, values)
    ax1.set_xticklabels(names, rotation=55, ha='right')
    plt.show()


