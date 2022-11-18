#!/usr/bin/env python
#!/bin/env python

import json

class HelperMethods:
  
  def load_json(self, file_name):

    issuu_user_data = []

    with open('data/' + file_name) as f:
            for jsonObj in f:
                user_data = json.loads(jsonObj)
                issuu_user_data.append(user_data) 
    return issuu_user_data

