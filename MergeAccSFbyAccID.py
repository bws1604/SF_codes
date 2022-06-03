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

path = '/Users/localusername/GithubDocs/Digin2022/'
mergeby = 'AccId'
#get the conference list and SFDC master report
confList = pd.read_csv(path + 'Id.csv')
print('Conference List: ')
print(confList)
SFcontList = pd.read_csv(path + 'SFDC_AllAccounts2022_06_01_14_05_55.csv')
print('SFDC List: ')
print(SFcontList)

#check column names
print('Conference List Column Names: ')
print(confList.columns)
print('SFDC List Column Names: ')
print(SFcontList.columns)

"""Lists clean up process:"""

#get emails from confList and see if they match the SFcontList and return Account Info
merge_inner = pd.merge(confList, SFcontList,on='Id',how='inner')
print('Merge Inner:')
print(merge_inner)
output = merge_inner.to_csv(path + mergeby + 'Merge_inner_output.csv')#list of matching contacts with SFDC

non_match_contacts = confList[~confList.Id.isin(merge_inner.Id)]
print('Merge Non MATCH:')
print(non_match_contacts)
non_match_output = non_match_contacts.to_csv(path + mergeby + 'Non_match_output.csv')

