#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 14:22:14 2021

@author: localusername
"""
def matchString(x,content):
    newlist=[]
    for i in content:
        if x in i:
            domain = i.replace(x,'')
            newlist.append(domain)
        else:
            newlist.append(i)
        
   
    #print('list:', newlist)
    return newlist

import numpy as np
import pandas as pd
from datetime import datetime
import math
import json
import csv

# from simple_salesforce import Salesforce, SalesforceLogin, SFType

# loginInfo = json.load(open('login.json'))
# username = loginInfo['username']
# password = loginInfo['password']
# security_token = loginInfo['security_token']
# domain = 'login'

# session_id, instance = SalesforceLogin(username=username, password=password, security_token=security_token, domain=domain)
# sf = Salesforce(instance=instance, session_id=session_id)


# SearchList = open('callhanMatch.txt','r')
# content = SearchList.readlines()
# print('content # ', len(content))

el = ['http://','https://','www.','\n']

# finallist = matchString(el[0], content)
# finallist = matchString(el[1], finallist)   
# finallist = matchString(el[2], finallist)
# finallist = matchString(el[3], finallist)   

path = '/Users/localusername/GithubDocs/example/'
# mergeby = 'AccId2'
#get the conference list and SFDC master report
# confList = pd.read_csv(path + 'AccId.csv')
# print('Conference List: ')
# print(confList)
SFcontList = pd.read_csv(path + 'SFDC_AllContacts2021_10_06_13_28_05.csv')
print('SFDC List: ')
print(SFcontList)

#check column names
# print('Conference List Column Names: ')
# print(confList.columns)
print('SFDC List Column Names: ')
print(SFcontList.columns)

SFcontList=SFcontList.dropna(subset=['AccountId'])


#If we want to have the results in the original dataframe with specific names, we can add as new columns like shown below.
SFcontList[['EName','Domain']] = SFcontList.Email.str.split("@",expand=True,)

# sorting by first name
#SFcontList.sort_values("Domain", inplace = True)

#SFcontList.drop_duplicates(subset ="Domain", keep = False, inplace = True)



SFcontList.to_csv(path + 'AllSF_EmailDomain.csv',index=False)

"""
SOSL Query Call"""

# output = []
# noMatch = []

# for i in finallist:
#     try:
#         i = str(i)
#         #records = sf.search('FIND {'+i+'} RETURNING Contact (Name, Email, Id, AccountId, Account.Name, Account.Website, Account.Industry, Account.OwnerId)')
#         records = sf.search('FIND {'+i+'} RETURNING Account(Name, Id, Website, Industry, OwnerId, Partner_Relationship__c)')
#         sf_records = pd.DataFrame(records.get('searchRecords'))
#         output.append(sf_records)
#     except:
#         noMatch.append(i)
#         pass
# print(output)
# output = pd.concat(output, axis=0)
# print(type(output))
# task = 'MatchWebsite2AccID'
# output.to_csv(task +'SearchOutput.csv')
# df = pd.DataFrame(noMatch,columns=['Name'])
# df.to_csv('noMatchLeverage.csv',index=False)
