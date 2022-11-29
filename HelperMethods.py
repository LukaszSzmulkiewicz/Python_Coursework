#!/usr/bin/env python
#!/bin/env python

import json
import re

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
  
    # method to load json with a regex pattern
    def load_json_re(self,file_name, regex_name):
        issuu_user_data = []
        try:
                with open('data/' + file_name, encoding='utf-8') as f:
                        for jsonObj in f:
                            if (re.search(regex_name, jsonObj)):
                                user_data = json.loads(jsonObj)
                                issuu_user_data.append(user_data) 
                                
        except:
            pass 
            
        return issuu_user_data

    # to load a specific object from json file
    def load_json_specific(self, file_name, object_name):

        issuu_user_data = []
        try:
            with open('data/' + file_name, encoding='utf-8') as f:
                    for jsonObj in f:
                        user_data = json.loads(jsonObj)
                        issuu_user_data.append(user_data[object_name]) 
        except:
            pass 
            
        return issuu_user_data

