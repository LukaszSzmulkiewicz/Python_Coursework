#!/usr/bin/env python
#!/bin/env python

import json

class HelperMethods:
  
  def load_json(self, file_name):

      issuu_user_data = []
      try:
        with open('data/' + file_name, encoding='utf-8') as f:
                for jsonObj in f:
                    user_data = json.loads(jsonObj)
                    issuu_user_data.append(user_data) 
      except:
            print("Incorrectly defined Json file")
      return issuu_user_data

