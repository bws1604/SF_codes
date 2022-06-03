#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 11:59:40 2021

@author: localusername
"""

import json
import pandas as pd
from datetime import datetime

from simple_salesforce import Salesforce, SalesforceLogin, SFType

#specify the location where to save the output documents in a folder outside the Github folder
path = '/Users/localusername/GithubDocs/SF_Users/'
login_path = '/Users/localusername/GithubDocs/login/'

loginInfo = json.load(open(login_path + 'login.json'))
username = loginInfo['username']
password = loginInfo['password']
security_token = loginInfo['security_token']
domain = 'login'

session_id, instance = SalesforceLogin(username=username, password=password, security_token=security_token, domain=domain)
sf = Salesforce(instance=instance, session_id=session_id)

querySOQL = """SELECT Id, Name, UserRole.Name, IsActive FROM User Where IsActive = True"""

#save the query results
response = sf.query(querySOQL)
lstRecords = response.get('records')
#when results are more than 200 they will be saves as next records
nextRecordsUrl = response.get('nextRecordsUrl')

#keep getting records until the response.get('done') returns as True
while not response.get('done'):
    #use query more to get the nextRecordsUrl
    response = sf.query_more(nextRecordsUrl, identifier_is_url=True)
    #use extend method to join all the records
    lstRecords.extend(response.get('records'))
    nextRecordsUrl = response.get('nextRecordsUrl')

#pass th records to a pandas data frame
df_records = pd.DataFrame(lstRecords)

#make the account atributes their own columns instead of a nested dictionary
#dfAccount = df_records['Account'].apply(pd.Series).drop(labels='attributes', axis=1, inplace=False)
#dfAccount.columns = ('Account.{0}'.format(name) for name in dfAccount.columns)

#erase the account and tributes columns
#df_records.drop(labels=['Account','attributes'], axis=1, inplace=True)

#join both records contacts and account objects
#dfContAcct = pd.concat([df_records, dfAccount], axis=1)
#dfContAcct.to_csv(path + 'SFDC_AllContacts' + str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + '.csv', index=False)
df_records.to_csv(path + 'SFDC_All_SF_Users.csv', index=False)
