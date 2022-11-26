import pandas as pd

class ReaderCounter:

  # method to load readers to a dataframe
  def load_readers(self, issuu_user_data):
    readers = []
    for user_id in issuu_user_data:
        readers.append([user_id['visitor_uuid'], user_id['event_readtime']])
    df_readers = pd.DataFrame.from_dict(readers)
    df_readers.columns =['visitor_uuid', 'event_readtime']
    return readers           

  # method to return best 10 readers
  def return_10_best_readers(self, df_readers):
    df_user_ids = df_readers.groupby(["visitor_uuid", 'visitor_username']).sum().reset_index()
    df_result = df_user_ids.sort_values(by="event_readtime", ascending=False)
    return df_result[:10]           

