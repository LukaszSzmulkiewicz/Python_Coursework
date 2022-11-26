import pandas as pd
import matplotlib.pyplot as plt

class ReaderCounter:

  # method to load readers to a dataframe
  def load_readers(self, issuu_user_data):
    readers = []
    for user_id in issuu_user_data:
        if not (user_id.get('visitor_username')  is None):
            readers.append([user_id['visitor_ip'], user_id['visitor_username'], user_id['visitor_uuid'], user_id['event_readtime']])
        else:
            readers.append([user_id['visitor_ip'], 'no username', user_id['visitor_uuid'], user_id['event_readtime']])
    return readers     
    
  # method to assign column names to the readers dataframe
  def assign_column_names_to_df(self, dict_user_data):
    df_user_ids = pd.DataFrame.from_dict(dict_user_data)
    df_user_ids.columns =['visitor_ip', 'visitor_username', 'visitor_uuid', 'event_readtime']
    return df_user_ids
    
  # method to return best readers
  def best_readers_count(self, df_readers):
    df_user_ids = df_readers.groupby(["visitor_uuid", 'visitor_username']).sum().reset_index()
    df_result = df_user_ids.sort_values(by="event_readtime", ascending=False)
    return df_result

  def return_10_best_readers(self, df_readers):
    df_result = df_readers[0:10]
    return df_result

  
  def plot_readers(self, df_user_data):
    names = df_user_data['visitor_uuid']
    values = df_user_data['event_readtime']
    fig, (ax1) = plt.subplots(figsize=(25, 15))
    ax1.bar(names, values)
    ax1.set_xticklabels(names, rotation=55, ha='right')
    plt.show()        

