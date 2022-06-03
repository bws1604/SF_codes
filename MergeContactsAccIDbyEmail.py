#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 16:03:09 2021

@author: barbarawilsonsoto
"""

import numpy as np
import pandas as pd
from datetime import datetime
import math

path = '/Users/barbarawilsonsoto/GithubDocs/CleanUP/'

#get the conference list and SFDC master report
confList = pd.read_csv(path + 'Email.csv')
print('Conference List: ')
print(confList)
SFcontList = pd.read_csv(path + 'SFDC_AllContacts2021_11_23_06_53_30.csv')
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
#confList.rename(columns={"Email Address":"Email"}, inplace=True)
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
merge_inner = pd.merge(confList, SFcontList,on='Email',how='inner')
print('Merge Inner:')
print(merge_inner)
output = merge_inner.to_csv(path + 'LeadsAccMerge_inner_output.csv')#list of matching contacts with SFDC

non_match_contacts = confList[~confList.Email.isin(merge_inner.Email)]
print('Merge Non MATCH:')
print(non_match_contacts)
non_match_output = non_match_contacts.to_csv(path + 'LeadsAccNon_match_output4.csv')