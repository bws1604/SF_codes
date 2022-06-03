#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:23:03 2021

@author: barbarawilsonsoto
"""

import numpy as np
import pandas as pd
from datetime import datetime
import math

path = '/Users/barbarawilsonsoto/GithubDocs/CleanUP/'
# mergeby = 'EEAccId'
#get the conference list and SFDC master report
# confList = pd.read_csv(path + 'EEAccId.csv')
# print('Conference List: ')
# print(confList)
SFcontList = pd.read_csv(path + 'SFDC_AllContacts2021_12_15_08_23_48.csv')
print('SFDC List: ')
print(SFcontList)

#SFcontList['Id'] = SFcontList['Id'].str[:-3]
#df['filename'] = [x[:-4] for x in df['filename']]
#df["A"].str[:-1]

#check column names
# print('Conference List Column Names: ')
# print(confList.columns)
print('SFDC List Column Names: ')
print(SFcontList.columns)
print(SFcontList.head)


# #check two columns values and return a TRUE/FALSE value depending if they are equal or not
#SFcontList['OwnerMatch'] = np.where(SFcontList['OwnerId'] == SFcontList['Account.OwnerId'],'True','False')

# SFcontList.to_csv(path + 'SFDC_AllContacts_AOMatchCO.csv', index=False)
#get new  dataframe where 'OwnerMatch' == 'True'
#MatchTrueSFcontList = SFcontList[SFcontList['OwnerMatch'] == 'True']
# print(MatchTrueSFcontList)
#MatchTrueSFcontList.to_csv(path + 'SFDC_AllContacts_AOMatchCOTrueNov.csv', index=False)

#get new  dataframe where 'OwnerMatch' == 'False'
#MatchFalseSFcontList = SFcontList[SFcontList['OwnerMatch'] == 'False']
# print(MatchFalseSFcontList)
#MatchFalseSFcontList.to_csv(path + 'SFDC_AllContacts_AOMatchCOFalseNov.csv', index=False)

#Get contacts that opted OUT from Emails outreach
OptedOUT_SFcontList = SFcontList[SFcontList['HasOptedOutOfEmail'] == True]
OptedOUT_SFcontList.to_csv(path + 'SFDC_AllContacts_OptedOUT.csv', index=False)

print(OptedOUT_SFcontList)

#Get contacts that opted IN from Emails outreach
OptedIN_SFcontList = SFcontList[SFcontList['HasOptedOutOfEmail'] == False]
OptedIN_SFcontList.to_csv(path + 'SFDC_AllContacts_OptedIN.csv', index=False)

print(OptedIN_SFcontList)

