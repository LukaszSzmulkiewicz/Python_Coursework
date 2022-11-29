import matplotlib.pyplot as plt
import pandas as pd
import re
from ua_parser import user_agent_parser
import pprint
import HelperMethods
from user_agents import parse

class BrowserViewer:

  # def user_agent_parser(self, string):
  #   pp = pprint.PrettyPrinter(indent=4)
  #   ua_string = string
  #   parsed_string = user_agent_parser.ParseUserAgent(ua_string)
  #   return_string = pp.pprint(parsed_string)
  #   return return_string

  def parse_user_agents(self,issuu_user_data):
    # pp = pprint.PrettyPrinter(indent=4)
    # ua_string = string
    country_codes = []
    for country in issuu_user_data:
      ua_string = country
      user_agent = parse(ua_string)
      # parsed_string = user_agent_parser.ParseUserAgent(country)
      # return_string = pp.pprint(parsed_string)
      # string = str(country)
      # country2 = BrowserViewer.user_agent_parser()
      country_codes.append(user_agent.browser.family)
    return country_codes

  def split_list_on_brackets(self, issuu_user_data):
    browsers = []
    for browser in issuu_user_data:
        browsers.append(re.split('(\(.*?\))|(\[.*?\])', browser ))
    return browsers

  def remove_short_and_none(self, dict_user_data):
    browsers = []
    for x in dict_user_data:
        for y in x:
            if not (y is None):
                if(len(y) > 3):
                    browsers.append(y)
    return  browsers
  
  def browsers_to_dataframe(self, list):
    df = pd.DataFrame(list)
    df.columns = ['browsers']
    return df


  def remove_data_with_brackets(self, dataframe):
    dataframe = dataframe[dataframe['browsers'].str.contains("\\(|\\[") == False]
    return dataframe

  def count_browser_codes_occurrences(self, dataframe):
    dataframe = dataframe.value_counts().rename_axis('browser_code').reset_index(name='counts')
    return dataframe
    
  def plot_browsers(self, df_user_data):
    names = df_user_data['browser_code']
    values = df_user_data['counts']
    fig, (ax1) = plt.subplots(figsize=(25, 15))
    ax1.bar(names, values)
    ax1.set_xticklabels(names, rotation=55, ha='right')
    plt.show()

# bv = BrowserViewer()
# hm = HelperMethods.HelperMethods()

# data = hm.load_json_specific('sample_3m_lines.json', 'visitor_useragent')
# string = bv.parse_user_agents(data)
# print(len(string))