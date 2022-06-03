#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 09:49:54 2021

@author: barbarawilsonsoto
"""
import json
from datetime import datetime
import pandas as pd

from simple_salesforce import Salesforce, SalesforceLogin, SFType

#specify the location where to save the output documents in a folder outside the Github folder
path = '/Users/barbarawilsonsoto/GithubDocs/CleanUp/'
login_path='/Users/barbarawilsonsoto/GithubDocs/login/'


loginInfo = json.load(open(login_path+'login.json'))
username = loginInfo['username']
password = loginInfo['password']
security_token = loginInfo['security_token']
domain = 'login'

session_id, instance = SalesforceLogin(username=username, password=password, security_token=security_token, domain=domain)
sf = Salesforce(instance=instance, session_id=session_id)

idList = pd.read_csv(path + 'deleteLeads.csv')
print('Id List: ')
print(idList)

lead = SFType('Lead', session_id, instance)

Lead_Id = []
SF_response = []
for i in idList['Id']:
    try:
        response = lead.delete(str(i))
        print(str(i) + " " + str(response))
        Lead_Id.append(i)
        SF_response.append(response)
    except Exception as e:
        print(str(i) + " " + str(e))
del_result = pd.DataFrame({'Id': Lead_Id, 'SF Del response': SF_response})
del_result_output = del_result.to_csv(path + 'SFdelResponse.csv')
   