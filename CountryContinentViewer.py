#!/usr/bin/env python
#!/bin/env python

import matplotlib.pyplot as plt
import pandas as pd
import json

class CountryContinentViewer:

  df_user_data = pd.DataFrame(columns=[ 'country_code', 'country_name', 'continent'])

  def load_country_codes(self, issuu_user_data):
    country_codes = []
    for country in issuu_user_data:
        country_codes.append(country["visitor_country"])
    return country_codes
    
  def load_countries_to_dictionary(self):
    df_country_and_code = pd.read_csv("data/countries.csv")
    dict_country_and_code = dict(zip(df_country_and_code.country_code , df_country_and_code.name))
    return dict_country_and_code
  
  def load_continents_to_dictionary(self):
    df_country_and_continent = pd.read_csv("data/continents.csv")
    dict_country_and_continent = dict(zip(df_country_and_continent.country , df_country_and_continent.continent))
    return dict_country_and_continent

  def assign_countries_and_continents(self, country_codes, dict_country_and_code, dict_country_and_continent):
    for country in country_codes:
          if dict_country_and_code[country]:
              if dict_country_and_continent[dict_country_and_code[country]]:
                  
                  new_row = {
                      'country_code': country,
                      'country_name': dict_country_and_code[country],
                      'continent': dict_country_and_continent[dict_country_and_code[country]]
                  }
                  df_new_row = pd.DataFrame([new_row])
                  self.df_user_data = pd.concat([self.df_user_data, df_new_row], axis=0, ignore_index=True)
          else:
              continue
    return self.df_user_data
          

  def plot_country(self):
    df_countries_count = self.df_user_data['country_name'].value_counts().rename_axis('country_name').reset_index(name='counts')

    names = df_countries_count['country_name']
    values = df_countries_count['counts']
    fig, (ax1) = plt.subplots(figsize=(20, 9))
    ax1.bar(names, values)
    ax1.set_xticklabels(names, rotation=55, ha='right')
    plt.show()


  def plot_continent(self):
    df_continent_count = self.df_user_data['continent'].value_counts().rename_axis('continent').reset_index(name='counts')

    names = df_continent_count['continent']
    values = df_continent_count['counts']
    fig, (ax1) = plt.subplots(figsize=(20, 9))
    ax1.bar(names, values)
    ax1.set_xticklabels(names, rotation=30, ha='right')
    plt.show()



