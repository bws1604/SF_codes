#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 16:54:01 2021

@author: localusername
"""

import numpy as np
import pandas as pd
from datetime import datetime
import math

path = '/Users/localusername/GithubDocs/OutboundDist/'
mergeby = 'AccId'
#get the conference list and SFDC master report
confList = pd.read_csv(path + 'AccId.csv')
print('Conference List: ')
print(confList)
SFcontList = pd.read_csv(path + 'SFDC_AllAccounts2022_01_10_09_39_24.csv')
print('SFDC List: ')
print(SFcontList)

#check column names
print('Conference List Column Names: ')
print(confList.columns)
print('SFDC List Column Names: ')
print(SFcontList.columns)

"""Lists clean up process:"""
#Separate the rows with empty values, so we can asses them manually later
#blankemail = confList[confList.isna().any(axis=1)]
# print(blankemail)

#get emails to lowecase to prevent false negatives
#confList['Email'] = confList['Email'].str.lower()

# print('Conference: ')
# for x in confList.columns:
#     print(x)

# print('SFData: ')
# for x in confList.columns:
#     print(x)
    
# #fix columns names
# confList = pd.DataFrame(confList)
# #fix columns names
#SFcontList['Id'] = SFcontList['Id'].str[:-3]
#SFcontList.to_csv(path + mergeby + 'test1.csv')

#confList.rename(columns={"AccountID":"Id"}, inplace=True)
# #delete Nan values from Email column
# confList = confList.dropna(subset=['Email'])
# #delete empty columns
# confList = confList.drop(columns=['Account ID', 'Account Owner_Name','Account: Record owner'])


# #check column names
# print('Conference:')
# for x in confList.columns:
#     print(x)

# print('SFData:')
# for x in confList.columns:
#     print(x)

# # emailSF = SFcontList['Email'].tolist()
# # n = 0
# # AccId = []
# confList['Email'] = confList['Email'].str.lower()
# print(confList)



#get emails from confList and see if they match the SFcontList and return Account Info
merge_inner = pd.merge(confList, SFcontList,on='Id',how='inner')
print('Merge Inner:')
print(merge_inner)
output = merge_inner.to_csv(path + mergeby + 'Merge_inner_output.csv')#list of matching contacts with SFDC

non_match_contacts = confList[~confList.Id.isin(merge_inner.Id)]
print('Merge Non MATCH:')
print(non_match_contacts)
non_match_output = non_match_contacts.to_csv(path + mergeby + 'Non_match_output.csv')

