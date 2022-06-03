#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 22:31:39 2021

@author: barbarawilsonsoto
"""
import numpy as np
import pandas as pd
from datetime import datetime
import math

path = '/Users/barbarawilsonsoto/GithubDocs/Digin2022/'
mergeby = 'Edomain'
#get the conference list and SFDC master report
confList = pd.read_csv(path + 'Edomain.csv')
print('Conference List: ')
print(confList)

SFcontList = pd.read_csv(path + 'SFDC_AllContacts2022_06_01_12_57_51.csv')
print('SFDC List: ')
print(SFcontList)

#check column names
print('Conference List Column Names: ')
print(confList.columns)
print('SFDC List Column Names: ')
print(SFcontList.columns)

"""Lists clean up process:"""

SFcontList[['Ename','Edomain']] = SFcontList['Email'].str.split('@',expand=True)
print("Split")
SFcontList = SFcontList.drop(columns=['Email','Ename'])
print(SFcontList)
print(SFcontList.columns)

print("Drop")
print(SFcontList.shape)
SFcontList = SFcontList.drop_duplicates(subset='Edomain')
print(SFcontList)
print(SFcontList.columns)

print("Final")
print(SFcontList)
print(SFcontList.columns)

#get emails from confList and see if they match the SFcontList and return Account Info

merge_inner = pd.merge(confList, SFcontList,on='Edomain',how='inner')
print('Merge Inner:')
print(merge_inner)
output = merge_inner.to_csv(path + mergeby + 'Merge_inner_output.csv')#list of matching contacts with SFDC

non_match_contacts = confList[~confList.Edomain.isin(merge_inner.Edomain)]
print('Merge Non MATCH:')
print(non_match_contacts)
non_match_output = non_match_contacts.to_csv(path + mergeby + 'Non_match_output.csv')

