#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 12:56:42 2021

@author: barbarawilsonsoto
"""

import json
import pandas as pd
from datetime import datetime

from simple_salesforce import Salesforce, SalesforceLogin, SFType

#specify the location where to save the output documents in a folder outside the Github folder
path = '/Users/barbarawilsonsoto/GithubDocs/Minnesota/'
login_path = '/Users/barbarawilsonsoto/GithubDocs/login/'

loginInfo = json.load(open(login_path + 'login.json'))
username = loginInfo['username']
password = loginInfo['password']
security_token = loginInfo['security_token']
domain = 'login'

session_id, instance = SalesforceLogin(username=username, password=password, security_token=security_token, domain=domain)
sf = Salesforce(instance=instance, session_id=session_id)

#set the values or attributes to query
#values = ['Name', 'AccountId', 'Email', 'OwnerId', 'Account.Website', 'Account.OwnerId', 'Account.Number_of_Open_Opportunities__c', 'Account.LastActivityDate', 'Account.LastModifiedById', 'Account.LastModifiedDate', 'Account.Industry']
#values = ['Name', 'Id', 'Website', 'OwnerId','Number_of_Open_Opportunities__c','Industry','Current_ARR__c','LastActivityDate','Account_Status__c', 'Callahan_ID__c', 'FDIC_Certificate__c', 'FDIC_Certificate_Number__c', 'Assets_Under_Management__c']
#values = ['Name', 'Id', 'OwnerId','ParentId','Website','Industry','Number_of_Open_Opportunities__c','Account_Status__c','Current_ARR__c','Assets_Under_Management__c','Insurance_type__c','BillingCountry','LastActivityDate'] 
#values = ['Name', 'Id', 'Website', 'OwnerId','Industry','Number_of_Open_Opportunities__c','Account_Status__c','Current_ARR__c','LastActivityDate','LastModifiedById','BDR_Status__c','BillingCountry','ParentId']
#values = ['Name', 'Id','Industry','Insurance_type__c','BillingCountry']

querySOQL = """SELECT (SELECT AccountId, ActivityDate, Subject, OwnerId, PrimaryWhoId from ActivityHistories WHERE ActivityDate > 2018-01-01 AND ActivityDate < 2018-04-01) FROM Account"""

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
#dfActHist = df_records['ActivityHistories'].apply(pd.Series).drop(labels='attributes', axis=1, inplace=False)
#dfActHist.columns = ('ActHist.{0}'.format(name) for name in dfActHist.columns)

#erase the account and tributes columns
#df_records.drop(labels=['ActivityHistories','attributes'], axis=1, inplace=True)

#join both records contacts and account objects
#dfAccActHist = pd.concat([df_records, dfActHist], axis=1)
#dfAccActHist.to_csv(path + 'SFDC_AllActvivityHistory' + str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + '.csv', index=False)
df_records.to_csv(path + 'SFDC_AllActvivityHistory' + str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + '.csv', index=False)
