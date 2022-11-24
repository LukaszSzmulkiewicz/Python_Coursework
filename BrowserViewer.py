#!/usr/bin/env python
#!/bin/env python

import matplotlib.pyplot as plt
import pandas as pd

class BrowserViewer:

  # df_user_data = pd.DataFrame(columns=[ 'country_code', 'country', 'continent', 'counts'])

  def load_browser_codes(self, issuu_user_data):
    browser_codes = []
    for browser in issuu_user_data:
        browser_codes.append(browser["visitor_useragent"])
    return browser_codes

  def list_to_dataframe(self, browser_codes):
    df_browser_codes = pd.DataFrame.from_dict(browser_codes)
    return df_browser_codes

  def count_browser_codes_occurrences(self, df_browser_codes):
    df_browser_codes_new = df_browser_codes.value_counts().rename_axis('browser_code').reset_index(name='counts')  
    return df_browser_codes_new

  def plot_browsers(self, df_user_data):
    names = df_user_data['visitor_useragent']
    values = df_user_data['counts']
    fig, (ax1) = plt.subplots(figsize=(25, 15))
    ax1.bar(names, values)
    ax1.set_xticklabels(names, rotation=55, ha='right')
    plt.show()