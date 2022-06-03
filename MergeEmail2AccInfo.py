#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 09:17:07 2021

@author: barbarawilsonsoto
"""

import numpy as np
import pandas as pd
from datetime import datetime
import math

path = '/Users/barbarawilsonsoto/GithubDocs/Maryland2022/'

#get the conference list and SFDC master report
confList = pd.read_csv(path + 'Email.csv')
print('Conference List: ')
print(confList)
SFcontList = pd.read_csv(path + 'SFDC_AllContacts2022_05_31_12_02_49.csv')
print('SFDC List: ')
print(SFcontList)

#check column names
print('Conference List Column Names: ')
print(confList.columns)
print('SFDC List Column Names: ')
print(SFcontList.columns)

"""Lists clean up process:"""
#Separate the rows with empty values, so we can asses them manually later

#get emails to lowecase to prevent false negatives
confList['Email'] = confList['Email'].str.lower()

#get emails from confList and see if they match the SFcontList and return Account Info
merge_inner = pd.merge(confList, SFcontList,on='Email',how='inner')
print('Merge Inner:')
print(merge_inner)
output = merge_inner.to_csv(path + 'Email_merge_inner_output.csv')#list of matching contacts with SFDC

non_match_contacts = confList[~confList.Email.isin(merge_inner.Email)]
print('Merge Non MATCH:')
print(non_match_contacts)
non_match_output = non_match_contacts.to_csv(path + 'Email_non_match_output.csv')