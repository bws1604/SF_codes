#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 16:35:59 2021

@author: localusername
"""

import numpy as np
import pandas as pd
from datetime import datetime
import math
import json
import csv

from simple_salesforce import Salesforce, SalesforceLogin, SFType

path = '/Users/localusername/GithubDocs/JeffKTask/'
login_path='/Users/localusername/GithubDocs/login/'

loginInfo = json.load(open(login_path + 'login.json'))
username = loginInfo['username']
password = loginInfo['password']
security_token = loginInfo['security_token']
domain = 'login'

session_id, instance = SalesforceLogin(username=username, password=password, security_token=security_token, domain=domain)
sf = Salesforce(instance=instance, session_id=session_id)

SearchBy="CompName"

SearchList = open(path+SearchBy+'.txt','r')
content = SearchList.read()

print("break")

search = content.splitlines()
#print(search)
print('search content # ', len(search))

"""
SOSL Query Call"""

output = []
noMatch = []

for i in search:
    try:
        i = str(i)
        #records = sf.search('FIND {'+i+'} IN Name Fields RETURNING Contact (Name, AccountId, Email, OwnerId, Account.Website, Account.Name, Account.OwnerId, Account.Number_of_Open_Opportunities__c, Account.Account_Status__c, Account.Current_ARR__c, Account.Industry)')
        records = sf.search('FIND {'+i+'} RETURNING Account (Name, Id, Website, Industry, OwnerId, Number_of_Open_Opportunities__c, Account_Status__c, Current_ARR__c )')# Number_of_Open_Opportunities__c, LastActivityDate, LastModifiedById, LastModifiedDate, Current_ARR__c')
        sf_records = pd.DataFrame(records.get('searchRecords'))
        output.append(sf_records)
    except:
        noMatch.append(i)
        pass
print("output: ", output)
print("NOT found", len(noMatch))
print("NOT found", noMatch)
output = pd.concat(output, axis=0)

#describe goal of the search
output.to_csv(path+SearchBy+'SearchOutput' +'.csv')
df = pd.DataFrame(noMatch,columns=['Name'])
df.to_csv(path+SearchBy+'NoMatchSearchoutput' +'.csv',index=False)

